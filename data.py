mport pandas as pd

class data:

    def __init__(self, input_file):
        x = pd.read_csv(input_file, low_memory=False)
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
        people_stack = pd.concat([self.Lastname, self.Firstname, self.status, self.salary, self.hours, self.title], axis=1)
        return people_stack

    def agency_record(self):
        agency_stack = pd.concat([agency, location], axis=1)
        return agency_stack


    def jobs_record(self):
        jobs_stack = pd.concat([title, base_salary], axis=1)
        return agency_stack 
    
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

'''
manhattan_housing = 1290000
manhattan_rent = 3785
brooklyn_housing = 969000
brooklyn_rent = 3350
queens_housing = 699000
queens_rent = 2242
staten_island_housing = 579908
staten_island_rent = 1500
bronx_housing = 550000
bronx_rent = 1800'''
