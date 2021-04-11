my_list = []   
for i in range(5):
    studentName= input('Please enter your name: ')
    midtermGrade = float(input('Please enter your midterm grade: '))
    projectGrade = float(input('Please enter your project grade: ' ))
    finalGrade = float(input('Please enter your final grade: ' ))
    passingGrade = (midtermGrade*(0.3) + projectGrade*(0.3) + finalGrade*(0.4))
    d = {'student' : studentName , 'midtermGrade' : midtermGrade, 'sprojectGrade': projectGrade, 'finalGrade' : finalGrade , 'passingGrade': passingGrade }
    print(d)
    print(my_list.append(passingGrade))

print(my_list)
new_list = sorted(my_list,reverse = True)
print(new_list)