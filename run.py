from user import User
import random
import string


def create_user(user_name,password):
    """
    this function create a new user with his or her password and save it in user_list
    """
    new_user=User(user_name,password)
    new_user.save_user()
    print("User created")
    return new_user

def create_credentials(account,password):

    """
    this function create a account credentials and save it in credentials under in credentials_list
    """
    new_credential=User.Credential(account,password)
    new_credential.save_credential()
    print(new_credential.Credential_list)

def delete_account():
    """
    this function delete an account from credentials list
    """
    print("nko hapa")


def user_credentials():

    """
    this function is used to either display user credentials already in file,edit a account credentials,remove an account credentials,
    or save a new credit to a specific user.
    """
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
            # create_credentials()
            # username=user["user"]
            account=input("Enter the account name?\n")
            choice3=input("To create a password enter:\nc- to create a custom password\ng-generate a custom password\n")
            if choice3=="c":
                # account=input("Enter the account name?\n")
                password=str(input("Enter a custom a password?"))
                print(account,password)
                # create_credentials(account,password)
                # 
            elif choice3=="g":
                # account=input("Enter the account name?\n")
                password=generate_password()
                print(account,password)
                # create_credentials(account,password)
                # create_credentials(username,account,password)
            else:
                print("Invalid entry, please enter 'c' or 'g'")    
            
                    
        else:
            print("Invalid entry,please try again")



def generate_password():
    """
    this function create a random password with all characters and the length is the password is 8
    """
    randompass = [random.choice(string.printable)for _ in range(8) ]
    password =""
    for char  in randompass:
        password+= char
    # print(password)
def login():
    """
    this function is used to autheticate the user using either already existing username and pin or one that he/she
    will create,after that as a existing user you will be able to access credentials accounts, if new user credentials will be empty
    """
    
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
