# Your Name Here
# UWYO COSC 1010
# Submission Date
# HW 01
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here

# Homework Question:
# 
# You are given a list of dictionaries where each dictionary represents a student and their scores 
# in different subjects.
# 
# Student Data:
# students = [
#     {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
#     {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
#     {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
#     {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
# ]

#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.

# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

#Solution

#A test to see if I could accurately get the mean
grade_point = 0
sample_gpa = {"Zipple": 84, "Gop": 70, "FiddleFoo": 98}
for gpa in sample_gpa.values():
    grade_point = grade_point + gpa
grade_point = grade_point / len(sample_gpa.values())
print(len(sample_gpa.values()))
print(grade_point)
gpas = []
students = [
    {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
    {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
    {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
    {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
]
grade_point = 0

for student in students:
    scores = student["scores"].values()
    print(scores.sum())
    # grade_point = grade_point + scores
    # gpas.append(grade_point)
    # grade_point = 0

print(gpas)

# scores = [dictionary["scores"].values() for dictionary in students]
# print(scores)
# gpa = 0

# for score in scores:
#     gpa = gpa + score
#     for grades in gpas:
#         gpas[]

# for index in range(len(students)):
#     gpa = 
    # for key in students[index]:
    #     for grade in key:
    #         print(students[index][key][grade])
        #gpa = gpa + students[index][key] 
        #gpa = gpa / len(students)

#print(gpa)



# gpas = {"Alice": 0, "Bob": 0, "Charlie": 0, "David": 0}

    
    