
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
print("Name\t\tFather's Name\t\tClass\t\t\tRoll No\t\t\tCGPA")

for student in students:
    print(f"{student[0]}\t\t{student[1]}\t\t\t{student[2]}\t\t\t\t{student[3]}\t\t\t\t{student[4]}")
print("\n\n====================================================================================")
user=int(input("Do You Want To Search Details:"))
if(user == "y" or "Y"):
    roll=int(input("Enter Student RollNo:"))
    for roll in roll
        print(f"{student[0]}\t\t{student[1]}\t\t\t{student[2]}\t\t\t\t{student[3]}\t\t\t\t{student[4]}")

else:
    print("Thanks for your Response")
