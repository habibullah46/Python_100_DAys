#corrrect email-habibullah
#password -1234
email = "habibullah"
email2="@gmail.com"
email=input("Apna email bata")
password = input("Apna password bhi bata")
if email==email+email2 and password == "1234":
    print("Welcome")
elif email==email+email2 and password !="1234":
    print("Ap ka email theak ha password khalat ha \n is lia ap password dobarah try kren")
    password = input("password phr sa bolan")
    if password == "1234":
         print("Good ab ap password theak karnay me kamyab hogia ha \n mubarak ho apko ")
    else:
         print("Ap na phr sa ghalat password enter kia ha ")

else:
    print("Incorrect credentials")
print("----------------------------------------------- \n -----------------------------------------------")
emaill = "habibullah"
emaill2 = "@gmail.com"
emaill3 = input("Enter Your Email:")
password = input("Enter Your Password:")
if emaill == emaill and emaill2 and password == "1234":
    print("well come")
elif emaill==email and emaill != emaill2:
    print("please enter @gmail.com ")
elif emaill == email and emaill2 and password != "1234":
    print("Please Enter correct password")
elif emaill != emaill and  emaill2 and password == "1234":
    print("Please Enter Correct your email")
elif emaill != emaill and password != "1234":
    print("Please Enter Correct your email and password")