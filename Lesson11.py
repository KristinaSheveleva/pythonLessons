#Dictionaries
# my_dict= {
#     "Bug": "Problem that occurs during the execution of the code",
#     "Error": "The problem that occurs when its impossible to proceed the code",
#     "Warning": "The problem whe you can't execute the code but with some mistake",
# }

# print(my_dict["Bug"])

# for thing in my_dict:
#     print(thing)
#     print(my_dict[thing])


# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# student_grades={}


# # TODO-2: Write your code below to add the grades to student_grades.👇
# for keys in student_scores:
#     score=student_scores[keys]
#     if score >90:
#         student_grades[keys]="It is excellent"
#     elif score >80:
#         student_grades[keys]="It is very good"
#     elif score >70:
#         student_grades[keys]="It is not bad"
#     elif score >60:
#         student_grades[keys]="It is bad"


# # 🚨 Don't change the code below 👇
# print(student_grades)

travel_list=[
    {
        "Country": "France",
        "visited_cities": ["Paris", "Leon", "Exan-Provance"],
        "total_visited": 7
    },
    {
        "Country": "Italy",
        "Visited": ["Milan", "Rome", "Tuscany"],
        "Total_visited_cities": 10
    }
]

print(travel_list[0]["visited_cities"][2])

dict1= {
    "France": {
        "visited_cities": ["Paris", "Leon", "Exan-Provance"],
        "total_visited": 7
    },
    "Italy": {
        "Visited": ["Milan", "Rome", "Tuscany"],
        "Total_visited_cities": 10
    }
}