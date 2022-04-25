from user import User
import random
import string


def create_user(user_name,password):
    new_user=User(user_name,password)
    new_user.save_user()
    print("User created")
    return new_user

def create_credentials(username,account,password):
    new_credential=User.Credential(username,account,password)
    new_credential.save_credential()
    print(new_credential.Credential_list)

def delete_account():
    print("nko hapa")


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
                # user_credentials()
        elif choice2=="s":
            username=user["user"]
            account=input("Enter the account name?\n")
            choice3=input("To create a password enter:\nc- to create a custom password\ng-generate a custom password\n")
            if choice3=="c":
                password=input("Enter a custom a password?")
            elif choice3=="g":
                password=generate_password()
            else:
                print("Invalid entry, please enter 'c' or 'g'")    
            create_credentials(username,account,password)
            # user_credentials()        
        else:
            print("Invalid entry,please try again")



def generate_password():
    randompass = [random.choice(string.printable)for _ in range(8) ]
    password =""
    for char  in randompass:
        password+= char
    print(password)
def login():
    choice1=input()
    if choice1=="l":
        for user in User.user_list:
            login_name=input("Enter your Username>> ")
            # print(user["username"])
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
