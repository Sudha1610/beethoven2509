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



create_salary(1000)
create_salary(2000)
create_salary(3000)
create_salary(4000)
create_salary(5000)

 #result_salaries = read_all()

#for salary in salaries:
    #print(salary)


#print(read_by_salary(1000))
#print(read_by_salary(4000))
#print(salaries[read_by_salary(8000)])

update(8000,8500)
print(read_all())
delete_by_salary(1000)
print(read_all())




