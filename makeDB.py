import os
import data from data.py

lastname_df = data.getLastname()
firstname_df = data.getFirstname()
status_df = data.getStatus()
title_df = data.getJobTitle()
salary_df = data.getSalary()
hours_df = data.getHours()
agency_df = data.getAgency()

def make_people_table(lastname, firstname, status, job_title, salary, hours, agency):
    os.system(f'python3 people.py {lastname} {firstname} {status} {job_title} {salary} {hours} {agency}')    

def main():
    os.system('rm nyc.db')
    os.system('sqlite3 socialMedia.db < schema.sql')
    for i in range(len(lastname_df)):
        make_people_table(lastname_df[i], firstname_df[i], status_df[i], title_df[i], salary_df[i], hours_df[i], agency_df[i])

