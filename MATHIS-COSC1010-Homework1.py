#Ben Mathis
# UWYO COSC 1010
#10/12/24
# HW 01
# Lab Section: 3
# Sources, people worked with, help given to: asked a syntax question to my friend Caleb (who knows Python)


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

gpas = {} #Setting the new dictionary that I will add everything into later. 
students = [
    {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
    {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
    {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
    {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
]

#setting variables to hold the values of "scores" and "name" so they can be used and 
#added into the gpas dictionary
#Figuring out the syntax here took some time, I was trying to acess the values directly with code like this
#for student in students.values()
#   students[student]['scores']
#This didn't work, obviously. 
for student in students:
    scores = student["scores"].values()
    names = student["name"]
    gpas[names] = sum(scores) / len(student["scores"].values())


#Compairing avg score to 80, then printing name of student
#this part was nice and easy
for winner, grade in gpas.items():
   if grade >= 80:
       print(winner)






    
    