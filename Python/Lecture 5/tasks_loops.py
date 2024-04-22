# 1. Make an associative list (Dictionary) to store the name of 5 students and iterate with a for loop.
# std =  {'std1': 'Ali', }
# for student in std:
#     print(std[student])


# Create a list of associative lists (dictionaries) to store the information of 2 students (to store the information of at least 2 students and access them as hard-coded.
#     Information to store:
#         A- Name, age, registration number, course, favorite programming languages (should be a normal list), Marks of 5 different subjects (should be an associative list).
#     The operations to perform:
#         B- Display every single value for any student.
#         C- Display the first and last favorite programming languages of any student.
#         D- Display the marks of any two subjects for any student.

# """


students = [
    {
         'name': 'Ali',
         'age': 27,
         'reg_no': '12345',
         'frov_program_lanaguage' : ['JavaScript','Python','HTML'],
         'marks' : {
            'math': 66,
            'english': 88,
            'urdu': 70
         }
    },
    {
         'name': 'umer',
         'age': 27,
         'reg_no': '12342',
         'frov_program_lanaguage' : ['JavaScript','Python','HTML'],
         'marks' : {
            'math': 67,
            'english': 87,
            'urdu': 787
         }
    },
]  
print(students[0]['name'])

print ("First lanaguage:" ,students[0]['frov_program_lanaguage'][0])

print ("Marks of one student",students[1]['marks']['english'])