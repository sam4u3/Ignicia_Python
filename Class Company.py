class Company(object):
    def __init__(self, company_id, company_name, company_type, company_email):
        self.Company_id = company_id
        self.Company_name = company_name
        self.company_type = company_type
        self.company_email = company_email

    def __str__(self):
        return "Company Name = {0}\nCompany Email = {1}".format(self.Company_name, self.company_email)

class Employee(Company):
    def __init__(self, company_id, company_name, company_type, company_email, emp_id, emp_name, emp_salary, emp_desg, emp_email):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_desg = emp_desg
        self.emp_email = emp_email
        Company.__init__(self,company_name,company_type,company_email,company_email)

    def __str__(self):
        return "\nEmployee ID = {}\nEmployee Name ={}\nEmployee email ={}".format(self.emp_id, self.emp_name,
                                                                                            self.emp_email)



comp = Employee(102, "Facebook", "Social networking site", "facebook.com",102,"stepahn",23000, "dev", "stephan@fb.com")
print(comp)