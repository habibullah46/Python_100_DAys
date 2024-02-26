# import random
# random.randint(20,30)
# jackpot = random.randint(20,30)
# guess = int(input("chal guess kar :"))
# counter = 1
# while guess !=jackpot:
#     if guess < jackpot:
#         print("Guess Lower")
#     guess = int(input("Chal Guess kar"))
#     counter +=1
# print("Sahi Jawab")
# print("You took",counter,"attempt")
print("===================================================")
print("\n\n\t\t\t\tStudent Details")
total = int(input("Number of Students You Want To Add:"))
students = []  # List to store details of all students

i = 1
while i <= total:
    print(f"\nEnter details for Student {i}:")
    name = input("Enter Your Name:")
    FatherName = input("Enter Your Father's Name:")
    Class = input("Enter Your Class:")
    Roll_NO = int(input("Enter Your Roll No:"))
    CGPA = float(input("Enter Your CGPA:"))
    # Store details of each student in a tuple
    student_details = (name, FatherName, Class, Roll_NO, CGPA)
    # Append the tuple to the list of students
    students.append(student_details)
    print("====================================================")
    i += 1

print("\n\n\t\t\t\tRegistered Student Details")
print("Name\t\t\tFather's Name\t\t\tClass\t\t\tRoll No\t\t\tCGPA")

# Iterate over the list of students and print their details
for student in students:
    print(f"{student[0]}\t\t\t{student[1]}\t\t\t{student[2]}\t\t\t{student[3]}\t\t\t{student[4]}")
