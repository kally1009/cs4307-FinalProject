import os
import pandas as pd


class Data:

    def __init__(self, input_file):
        x = pd.read_csv(input_file)
        df = pd.DataFrame(x)
        self.Lastname = df['Last Name']
        self.Firstname = df['First Name']
        self.status = df['Leave Status as of June 30']
        self.salary = df['Regular Gross Paid']
        self.hours = df['Regular Hours']
        self.title = df['Title Description']
        self.agency = df['Agency Name']
        self.location = df['Work Location Borough']
        self.base_salary = df['Base Salary']

    def people_record(self):
        people_stack = pd.concat(
            [self.Lastname, self.Firstname, self.status, self.salary, self.hours, self.title], axis=1)
        return people_stack

    def agency_record(self):
        agency_stack = pd.concat([self.agency, self.location], axis=1)
        return agency_stack

    def jobs_record(self):
        jobs_stack = pd.concat([self.title, self.base_salary], axis=1)
        return jobs_stack

    def getLastname(self):
        return self.Lastname

    def getFirstname(self):
        return self.Firstname

    def getStatus(self):
        return self.status

    def getSalary(self):
        return self.salary

    def getHours(self):
        return self.hours

    def getJobTitle(self):
        return self.title

    def getAgencyName(self):
        return self.agency

    def getBaseSalary(self):
        return self.base_salary

    def getLocation(self):
        return self.location


def make_people_table(firstname, lastname, status, job_title, salary, hours, agency_name, location):
    os.system(
        f'python3 people.py {firstname} {lastname} {status} {job_title} {salary} {hours} {agency_name} {location}')


def make_agency_table(agency_name, agency_borough):
    os.system(f'python3 agency.py {agency_name} {agency_borough}')


def make_housing():
    os.system(f'python3 housing.py')


def make_jobs(job_title, agency_name, base_salary, location):
    os.system(
        f'python3 jobs.py {job_title} {agency_name} {base_salary} {location}')


def main():

    os.system('rm nyc.db')  # Remove at end
    os.system('sqlite3 nyc.db < schema.sql')
    data = Data("Citywide_Payroll_Data__Fiscal_Year_.csv")
    lastname_df = data.getLastname()
    firstname_df = data.getFirstname()
    status_df = data.getStatus()
    title_df = data.getJobTitle()
    salary_df = data.getSalary()
    hours_df = data.getHours()
    agency_df = data.getAgencyName()
    location_df = data.getLocation()
    base_salary_df = data.getBaseSalary()
    lst = []

    make_housing()

    for i in range(5):
        lastname = '"'+lastname_df[i]+'"'
        firstname = '"'+firstname_df[i]+'"'
        status = status_df[i]
        title = '"'+title_df[i]+'"'
        salary = salary_df[i]
        hours = hours_df[i]
        agency = '"'+agency_df[i]+'"'
        location = location_df[i]
        location_string = '"'+location_df[i]+'"'
        base_salary = base_salary_df[i]

        make_agency_table(agency, location)
        make_jobs(title, agency, base_salary, location)
        make_people_table(firstname, lastname, status, title,
                          salary, hours, agency, location)


if __name__ == '__main__':
    main()
