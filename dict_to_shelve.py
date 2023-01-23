import shelve
university = shelve.open('university_file')
university['schedules'] =  {
        'monday_schedule': ['Math', 'English Language', 'System programming', 'Python'],
        'tuesday_schedule': ['English Language', 'HTML', 'Python', 'Football'],
        'wednesday_schedule': ['Math', 'Biology', 'System programming', 'Python'],
        'thursday_schedule': ['Physics', 'English Language', 'System programming', 'Running'],
        'friday_schedule': ['Math', 'Java', 'System programming', 'Chemistry']
    }
university['tutors'] = {
        'Math': ['Jack White', 'Jim Black'],
        'Python': ['Davis Redfield', 'Joseph Wilder']
    }
x = university['schedules']
print(type(x))
print(university['schedules']['wednesday_schedule'])
print(university['tutors']['Python'])
university.close()
# university = {
#     'schedules': {
#         'monday_schedule': ['Math', 'English Language', 'System programming', 'Python'],
#         'tuesday_schedule': ['English Language', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Math', 'Biology', 'System programming', 'Python'],
#         'thursday_schedule': ['Physics', 'English Language', 'System programming', 'Running'],
#         'friday_schedule': ['Math', 'Java', 'System programming', 'Chemistry']
#     },
#     'tutors': {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['Davis Redfield', 'Joseph Wilder']
#     }
# }

# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['Python'])