#read by salary
salaries = []
#crud - create ,read all, read by id, update, delete
def create_salary(salary):
    global salaries
    salaries.append(salary)
def read_all():
    return salaries

def read_by_salary(salary):#range(stop) | range(start,stop) |range(start,stop,step) # return first occurance index of salary
    for i in range(len(salaries)):#len(salaries)=5, i=0,1,2,3,4
        if salaries [i] == salary:
            return i
        return -1
def update(old_salary, new_salary):
    global salaries
    index = read_by_salary(old_salary)
    salaries[index] = new_salary

def delete_by_salary(salary):
    global salaries
    index= read_by_salary(salary)
    salaries.pop(index)
    