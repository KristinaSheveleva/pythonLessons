#FOR loops
# цикличная функция
#делает повторяюшие действия

# list_of_items=[]

# for item in list_of_items:
#     do something

# fruits=['apples', 'peach', 'pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit+' pie')

# for fruit in fruits:
#     if fruit=='peach':
#         print("It's a peach")
#     else:
#         print("It's an apple or a pear")

# student_scores=input("Give me the scores of students:")
# score_list=student_scores.split(" ")

# for chislo in range(0, len(score_list)):
#     score_list[chislo]=int(score_list[chislo])
    
  
# highest_score=0

# for number in score_list:
#     if number>highest_score:
#         highest_score=number
# print(f"The highest score is: {highest_score}")

student_height=input("Give me a list of heights:")
height_list=student_height.split(" ")

for heights in range(0, len(height_list)):
    height_list[heights]=int(height_list[heights])

sum=0

for height in height_list:
    sum+=height
print(f"The average height is: {int(round(sum/len(height_list),0))}")

