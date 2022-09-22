#singup for the user (Done)
#login for the user (Done)
#make a unique account number (Done)
#make a choice between current or saving account (Done)
#Allow user to withdraw and deposit to his account(Done)
#display welcome page for user (Done)
#login for admin (Done)
#Let the admin edit user's data except name and ID(Done)
# Make validation for withdraw for saving and current accounts (Done)

def id_generator():
    global id
    db = open("users.txt", "r")
    sm = db.read()
    aa = sm.split("\n")
    id = 0
    for line in aa:
        if line:
            id += 1
    
    id += 1
id_generator()

def admin():
  
    admin_access = input("Please enter Administration Username: ")
    admin_pass_access = input("Please enter Administration Password: ")

    db = open("Admin.txt", "r")
    for line in db.readlines():
        line = line.split(",")
        line = line[0].split(" ")
        Admin_name = line[0]
        Admin_pass = line[1]

    if admin_access == Admin_name:
        if Admin_pass == admin_pass_access:

            Choose = input("1: print all Users data." "\n" "2: Search for User." "\n" "3: To edit user's data" "\n")
    
            if Choose == "1":
                VC = open("Data.txt", "r")
                VC = VC.readlines()
                print(VC)

            if Choose == "2":
                passport = input("Please enter ID of the user: ")
                MO = open("Money.txt", "r")
                for line in MO.readlines():
                    line = line.split(",")
                    line = line[0].split(" ")
                    Balance = line[1]
                VC = open("users.txt", "r")
                for line in VC.readlines():
                    line = line.split(",")
                    line = line[0].split(" ")
                    user_id = line[0]
                    user_passport = line[4]
                    username = line[1]
                    password =line[2]
                    age = line[5]
                    status = line[6]
                    if passport == user_id:
                        return print("Name: "+ username+ "\n " + "Passport number: "+ user_passport+ "\n" + "Password: "+ password + "\n" + "Age: "+ age + "\n" + "Balance: " + Balance + "\n" + "Account Status: " + status) 
            
            if Choose == "3":
                return edit_User()
            return
        return print("Administration data entered wrong ")
    return print("Administration data entered wrong ")

def edit_User():
    print("*****User Edit*****")

    choice = input("1: To change user's Password \n 2: To change user's Passport Number \n 3: To change user's age \n")


    if choice == "1":
        
        # Open as read only to import lines into Py
        with open("users.txt", "r", encoding='utf-8') as file:
            allLinesList = file.readlines()

        f = open("users.txt", "r+")
        user_id1 = input("Please enter user's ID: ")
        for line in f.readlines():
            lineIndivArr = line.split(",")
            lineColArr = lineIndivArr[0].split(" ")
            id = lineColArr[0]
            # print(id)
            username1 = str(lineColArr[1])
            pass1 = str(lineColArr[2])
            pass2 = str(lineColArr[3])
            passport1 = str(lineColArr[4])
            age = str(lineColArr[5])
            
            if user_id1 == id:
                print("Your old password is ", pass1)
                
                new_pass = input("Please enter your new user name: ")

                # Edit the line where the user's id is
                allLinesList[int(id) - 1] = f"{str(id)} {str(username1)} {new_pass} {new_pass} {passport1} {age}, \n"
                
                # Open file as write only
                with open('users.txt', 'w', encoding='utf-8') as file:
                    file.writelines(allLinesList)

                f.close()            
            
                print("Your new password is: ",new_pass)
    

    if choice == "2":
        # Open as read only to import lines into Py
        with open("users.txt", "r", encoding='utf-8') as file:
            allLinesList = file.readlines()

        f = open("users.txt", "r+")
        user_id1 = input("Please enter user's ID: ")
        for line in f.readlines():
            lineIndivArr = line.split(",")
            lineColArr = lineIndivArr[0].split(" ")
            id = lineColArr[0]
            # print(id)
            username1 = str(lineColArr[1])
            pass1 = str(lineColArr[2])
            pass2 = str(lineColArr[3])
            passport1 = str(lineColArr[4])
            age = str(lineColArr[5])
            
            if user_id1 == id:
                print("Your old passport/ic is ", passport1)
                
                new_passort = input("Please enter your new user's passport number: ")

                # Edit the line where the user's id is
                allLinesList[int(id) - 1] = f"{str(id)} {str(username1)} {pass1} {pass2} {new_passort} {age}, \n"
                
                # Open file as write only
                with open('users.txt', 'w', encoding='utf-8') as file:
                    file.writelines(allLinesList)

                f.close()            
            
                print("Your new Passport number is: ",new_passort)
    
    if choice == "3":
        # Open as read only to import lines into Py
        with open("users.txt", "r", encoding='utf-8') as file:
            allLinesList = file.readlines()

        f = open("users.txt", "r+")
        user_id1 = input("Please enter user's ID: ")
        for line in f.readlines():
            lineIndivArr = line.split(",")
            lineColArr = lineIndivArr[0].split(" ")
            id = lineColArr[0]
            # print(id)
            username1 = str(lineColArr[1])
            pass1 = str(lineColArr[2])
            pass2 = str(lineColArr[3])
            passport1 = str(lineColArr[4])
            age = str(lineColArr[5])
            
            if user_id1 == id:
                print("Your old Age is ", age)
                
                new_age = input("Please enter your new user's Age: ")

                # Edit the line where the user's id is
                allLinesList[int(id) - 1] = f"{str(id)} {str(username1)} {pass1} {pass2} {passport1} {new_age}, \n"
                
                # Open file as write only
                with open('users.txt', 'w', encoding='utf-8') as file:
                    file.writelines(allLinesList)

                f.close()            
            
                print("Your new Age is: ",new_age)

def create_admin():

    Admin_username = input("Create Username for new admin: ")
    Admin_password = input("Create password for new Admin: ")
    db = open("Admin.txt", "a")
    data = f"{Admin_username} {Admin_password} , \n"
    db.write(data)
    db.close()
    print("Admin's account created successfully")

def super_admin():
    print("****Welcome to super admin department****")
    Username = "SuperAdmin"
    Password = "superadmin"
    print("********************")
    user_name = input("Enter Adminstraion username: ")
    pass_word = input("Enter Adminstraion password: ")
    print("********************")
    if user_name == Username:
        if pass_word == Password:
            return create_admin()
        return print("*Wrong password*")
    return print("*Wrong Username*")

def login():
    print("To login: ")
    Username = input("Please enter your account number: ")
    Password = input("please enter your password: ")
    
    global user_money
 
    db = open("users.txt", "r")
    for line in db.readlines():
        line = line.split(",")
        line = line[0].split(" ")
        user_id = line[0]
        user_password = line[2]
        
        if Username == user_id:
            if Password == user_password:
                print("Login successfully")
                acc = input("1: To see your profile " + "\n" + "2: To make a deposit " + "\n" + "3: To withdraw" + "\n")

            if acc == "1":
                profile()
                return

            if acc == "2":
                deposit()
                return

            if acc == "3":
                return withdraw()  
            
    print("invalid credentials")
    return

def profile():
    print("*User Profile*")


    data = open("users.txt", "r")
    for d in data:
        d = d.split(",")
        d = d[0].split(" ")
        user_id = d[0]
        user_name = d[1]
        user_age = d[5]
        user_passport = d[4]
        acc_status = d[6]

    mon = open("Money.txt", "r")
    for line in mon:
        line = line.split(",")
        line = line[0].split(" ")
        id = line[0]
        money = line[1]  


        if user_id == id:
            print("------------------------" + "\n" + "Username: " + user_name + "\n" + "Age: " + user_age + "\n" + "Passport/IC Number: " + user_passport + "\n" + "Balance: " + money + "\n" + "Account Status: " + acc_status + "\n"+ "------------------------")
 
def deposit():
    print("*****Deposit Money*****")
    
    db = open("users.txt", "r")
    for line in db.readlines():
        line = line.split(",")
        line = line[0].split(" ")
        user_id = line[0]

    # Open as read only to import lines into Py
    with open("Money.txt", "r", encoding='utf-8') as file:
        allLinesList = file.readlines()

    f = open("Money.txt", "r+")
    for line in f.readlines():
        lineIndivArr = line.split(",")
        lineColArr = lineIndivArr[0].split(" ")
        id = lineColArr[0]
        # print(id)
        Money = int(lineColArr[1])
        if user_id == id:
            print("Your balance is", Money)
            Amount = int(input("Please enter amount you want to deposit: "))
            Balance = Money + Amount

            # Edit the line where the user's id is
            allLinesList[int(id) - 1] = f"{str(id)} {str(Balance)}, \n"
            
            # Open file as write only
            with open('Money.txt', 'w', encoding='utf-8') as file:
                file.writelines(allLinesList)

            f.close()            
        
            print("Your new balance: ",Balance)
    f.close()   

def withdraw():

    print("*Welcome to withdraw department*")

    db = open("users.txt", "r")
    for line in db.readlines():
        line = line.split(",")
        line = line[0].split(" ")
        user_id = line[0]
        acc_status = line[6]
    

    # Open as read only to import lines into Py
    with open("Money.txt", "r", encoding='utf-8') as file:
        allLinesList = file.readlines()

    f = open("Money.txt", "r+")
    for line in f.readlines():
        lineIndivArr = line.split(",")
        lineColArr = lineIndivArr[0].split(" ")
        id = lineColArr[0]
        # print(id)
        Money = int(lineColArr[1])
        if user_id == id:
            if acc_status == "Saving":
                if Money > 100:
                    print("Your balance is", Money)
                    Amount = int(input("Please enter amount you want to withdraw: "))
                    Balance = Money - Amount

                    # Edit the line where the user's id is
                    allLinesList[int(id) - 1] = f"{str(id)} {str(Balance)}, \n"
                    
                    # Open file as write only
                    with open('Money.txt', 'w', encoding='utf-8') as file:
                        file.writelines(allLinesList)

                    f.close()            
                
                    print("Your new balance: ",Balance)
                else:
                    print("Not enough balance")

            if acc_status == "Current":
                if Money > 500:
                    print("Your balance is", Money)
                    Amount = int(input("Please enter amount you want to withdraw: "))
                    Balance = Money - Amount

                    # Edit the line where the user's id is
                    allLinesList[int(id) - 1] = f"{str(id)} {str(Balance)}, \n"
                    
                    # Open file as write only
                    with open('Money.txt', 'w', encoding='utf-8') as file:
                        file.writelines(allLinesList)

                    f.close()            
                
                    print("Your new balance: ",Balance)
                else:
                    print("Not enough balance")
    f.close()   

def register():
    print("To register a new account:")
    db = open("users.txt", "a")


    Username = input("Enter your name: ")
    Password = input("Create Password: ")
    Password1 = input("Confirm Password: ")
    Passport = input("Enter your passport/IC number: ")
    Age = int(input("Enter your age: "))
    Acc_money = input("Enter amount of money: ")
    Acc_status = input("1: Current account \n 2: Saving account \n")

    db = open("users.txt", "r")
    if Passport in db.readline():
        print("Passport/IC number already exist")
        register()
        
    if Password != Password1:
        print("Passwords aren't matching")
        register()
    
    if len(Password) < 8:
        print("Password should be 8 characters minimum")
        register() 

    if Acc_status == "1":
        Current ="Current"
        db = open("users.txt", "a")
        data = f"{id} {Username} {Password} {Password1} {Passport} {Age} {Current}, \n"
        db.write(data)
        db.close()

        data = open("Data.txt", "a")
        dt = f"-------------------- \n user ID:{id} \n Username: {Username} \n User Password: {Password} \n User Passport: {Passport} \n Age: {Age} \n Account status: {Current}\n -------------------- \n "
        data.write(dt)
        data.close()
    elif Acc_status == "2":
        Saving = "Saving"
        db = open("users.txt", "a")
        data = f"{id} {Username} {Password} {Password1} {Passport} {Age} {Saving}, \n"
        db.write(data)
        db.close()

        data = open("Data.txt", "a")
        dt = f"-------------------- \n user ID:{id} \n Username: {Username} \n User Password: {Password} \n User Passport: {Passport} \n Age: {Age} \n Account status: {Saving}\n -------------------- \n "
        data.write(dt)
        data.close()
    else:
        print("option not found")
        Acc_status()        



    my = open("Money.txt", "a")
    mon = f"{id} {Acc_money}, \n"
    my.write(mon)
    db.close()
    
    id_user = open("id.txt", "a")
    id_ = f"{id} , \n"
    id_user.write(id_)
    id_user.close()
    
    print("your ID is: " + str(id))

def choice():

    user = input("1: Login as user." "\n" "2: Login as Admin" "\n" "3: Login as Super admin" "\n")
    if user == "1":
        return login()
    
    if user == "2":
        return admin()
    
    if user == "3":
        return super_admin()

def home(option = None):
   
    id_ch = ""
    print("Welcome to our Banking services system")
    option = input("login | signup: ")
    if option == "login":
        choice()
       #print("login")
    elif option == "signup":
        id_ch = "signup"
        register()
       # print("register")
    else:
        print("Please choose an option")
        home()

home()