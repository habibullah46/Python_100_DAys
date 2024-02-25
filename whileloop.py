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
total=int(input("Number of Student You Want To Add:"))
i=1;
while i <=total:
    name=input("Enter Your Name:")
    FatherName=input("Enter Your FatherName:")
    Class=input("Enter Your Class:")
    Roll_NO=int(input("Enter Your Roll No:"))
    CGPA=float(input("Enter Your CGPA:"))
    print("====================================================")
    i+=1
print("\n\n\t\t\t\tRegister Student Details")
print("Name\t\t\tFatherName\t\t\tClass\t\t\tRollNo\t\t\tCGPA")

for i in range(1,total):
    print(name,"\t\t\t",FatherName,"\t\t\t",Class,"\t\t\t",Roll_NO,"\t\t\t",CGPA)
