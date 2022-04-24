from user import User


def create_user(user_name,password):
    new_user=User(user_name,password)
    new_user.save_user()
    print("User created")
    return new_user


def del_user(user):
    user.delete_user()


def user_credentials():
    print("Welcome to Credentials.Enter:\nd-to display save credentials\ne-to edit credentials\nr-to delete a credential\ns-save a new credentials.")
    choice2=input()
    for user in User.Credential.Credential_list:
       
        if choice2=="d":
            print(str(user["user"])+" these are your save credentials\n"+str(user["credentials"]))

        elif choice2=="e":
            print("coming soon")
        elif choice2=="r":
            if user["credentials"]==0:
                print("There is no account to delete")
            else:
                delete_account()
        elif choice2=="s":
            new_credentials()        
        else:
            print("Invalid entry,please try again")

def login():
    choice1=input()
    if choice1=="l":
        for user in User.user_list:
            login_name=input("Enter your Username>> ")
            print(user["username"])
            if login_name == user["username"]:
                login_pin=input("Proceed to enter you pin>>")
                if login_pin==user["pin"]:
                    print(login_name+" sucessfully logged in")
                    user_credentials()
                else:
                    print("You enter the wrong pin")
            else:
                print("Username not found,try again")
    elif choice1=="c":
        input_username=input("What username do you want to use?>>")
        input_pin=input("enter you preffered pin?>>")
        create_user(input_username,input_pin)
        # save_user(user)
        print("Enter l to log in or c to create another user?>>")
        login()
    else:
        print("Invalid input,please try again")
        login()
    



    


def main():
    print("Welcome to password locker")
    print("To log in to password Locker enter 'l' or to create a new user enter 'c'")
    login()
    
    
    # login_input=input().lower()
    # if login_input=='l':
    #     print("Enter your Username?")
        
    #     loginuser=input()
    #     if check_username_exist(loginuser):
    #         search_username= find_user(loginuser)
    #         print(search_username)


            # if loginuser==user:
            #     user = User.user_list
            #     # print(User.username)
            #     print(f"Welcome back {loginuser}")


        # if check_username_exist(loginuser):
        #     search_user=find_user(loginuser)
        #     print("{search_user.username}")
            # if loginuser == username:
            #     if user.password == password:
            #         print("You are logged in "+ username)
            #     else:
            #         print("Try again")
            # else:
            #     print("username not found")


if __name__=='__main__':
    main()
