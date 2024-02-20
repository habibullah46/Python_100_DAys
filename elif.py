print("Hostel Management System")
print("-------------------------------------------------")
print("1st Flour Details")
print("2nd Flour Details")
print("3rd Flour Details")
print("--------------------------------------------------")
choice = int(input("Enter Your Choice:"))
print("---------------------------------------------------")
if(choice == 1):
    print("Well Come To First Flour  ")
    print("------------------------------------------------")
    print("Room NO: 101\n Room No: 102 \n Room No: 103 \n Room No:104 ")
    choice = int(input("\n Please Select The Room Number"))
    print("-------------------------------------------------")
    if(choice == 101):
        print("1-Habibullah\n 2-Inayat Ali \n3-Hasnain ali")
        print("---------------------------------------------")
        choice= int(input("For Details person Person number according to your Requirement"))
        if(choice==1):
            print("----------------------------------------------------------------")
            print("Habibullah Details")
            print("Name: Habibullah \n FatherName: Abdul khaliq \n contact: 03436399697 \n address: vilalge kunis district ghanche gilgit baltistan")

        elif(choice==2):
            print("----------------------------------------------------------------")
            print(" Inayat Ali Details")
            print("Name: Inayat Ali \n FatherName: Ali Muhammad \n contact: 03456399697 \n address: vilalge marcha district ghanche gilgit baltistan")
        elif(choice==3):
            print("----------------------------------------------------------------")
            print("Hasnain Ali Details")
            print("Name: Hasnain Ali \n FatherName: Rozi Ali \n contact: 03436397869 \n address: vilalge Partuk district ghanche gilgit baltistan")
     elif(choice==102):
         print("1-fida \n 2-Raza \n3-waseem")
         print("---------------------------------------------")
         choice = int(input("For Details person Person number according to your Requirement"))
         if (choice == 1):
             print("----------------------------------------------------------------")
             print("fida Details")
             print( "Name: fida \n FatherName: Mehdi \n contact: 03434567697 \n address: village kunis district ghanche gilgit baltistan")

         elif (choice == 2):
             print("----------------------------------------------------------------")
             print(" RAZA Details")
             print("Name: Raza \n FatherName: Hussain \n contact: 03456399697 \n address: village harikon district ghanche gilgit baltistan")
         elif (choice == 3):
             print("----------------------------------------------------------------")
             print("Hasnain Ali Details")
             print( "Name: Hasnain Ali \n FatherName: Rozi Ali \n contact: 03434537869 \n address: village balghar district ghanche gilgit baltistan")




