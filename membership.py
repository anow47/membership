
admins = ["Faris","Awad","Tigani","Hamad","Yasir","Samani","Hamouda","Wajdi","musab","Amjed"]

name = input("please enter your name!").strip().capitalize()

if name in admins :
    print(f"Hello {name} Wellcome back")

    option = input("Delete or Update your account?").strip().capitalize()
    if option == 'Update' :
        theNewName = input("type your new name!")
        admins [admins.index(name)] = theNewName
        print ("account updated")
    elif option == "Delete" :
        admins.remove(name)
        print("account deleted")
    else:
        print("wrong option try again!")

else:
    status = input("you don\'t have account. type Y to Join N to cancel").strip().capitalize()
    if status == "Yes" or status == "Y" :
        admins.append(name)
        print("you have been added")
        print(admins)
    else:
        if status == "N" or status == "N" :
            print("your requist has been canceled")

    
