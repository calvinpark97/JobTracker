#!/usr/bin/env python3
import bs4, requests
from openpyxl import Workbook

wb = Workbook()

ws = wb.active
ws.title = "Jobs"

jobtitleslist = []
joblocationlist = []
jobcompanylist = []

jobTitle = input("What job are you looking for? ")
jobLoc = input("Where are you looking to work? (City State): ")
jobType = input("What type are you looking for? (Fulltime, Contract, Parttime): ")
jobLevel = input("What level are you looking for? (Entry level, Mid level, Senior level): ")

jobUrl = ('https://www.indeed.com/jobs?q=' + jobTitle + '&l=' + jobLoc + '&jt=' + jobType + '&explvl=' + jobLevel)
page = requests.get(jobUrl)
soup = bs4.BeautifulSoup(page.text, 'lxml')

#print(soup.prettify())

jobTitles = soup.select("h2 > span")
for titles in jobTitles:
    jobtitleslist.append(titles.text)


jobLocation = soup.find_all("div", class_="companyLocation")
for location in jobLocation:
    joblocationlist.append(location.text)

jobCompany = soup.find_all("span", class_="companyName")
for company in jobCompany:
    jobcompanylist.append(company.text)


ws.append(jobcompanylist)
ws.append(jobtitleslist)
ws.append(joblocationlist)
wb.save('Jobs.xlsx')

