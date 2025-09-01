salaries = []
salaries.append(1000)
salaries.append(5000)
salaries.append(6000)
print(salaries)
search = 5000
index = -1
i = 0
for salary in salaries:
    if salary == search:
        index = 1
        break
    i += 1
print(index)
salaries.remove(search)
print(salaries)
