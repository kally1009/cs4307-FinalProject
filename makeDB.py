import os
import data from data.py

lastname_df = data.getLastname()
firstname_df = data.getFirstname()
status_df = data.getStatus()
title_df = data.getJobTitle()
salary_df = data.getSalary()
hours_df = data.getHours()
agency_df = data.getAgencyName()
location_df = data.getLocation()
lst = []

def make_people_table(firstname, lastname, status, job_title, salary, hours, agency):
    os.system(f'python3 people.py {firstname} {lastname} {status} {job_title} {salary} {hours} {agency}')    
    
def make_agency_table(agency_name, agency_borough):
    os.system(f'python3 agency.py {agency_name} {agency_borough}')
    

    for i in range(len(lst)):
        
def main():
    os.system('sqlite3 socialMedia.db < schema.sql')
    for i in range(len(lastname_df)):
        make_people_table(lastname_df[i], firstname_df[i], status_df[i], title_df[i], salary_df[i], hours_df[i], agency_df[i])
        make_agency_table(agency_df[i], location_df[i] )
        

