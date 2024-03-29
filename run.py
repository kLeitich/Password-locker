from collections import UserList
from user import User
import random
import string


def create_user(input_username,input_pin):
    """
    this function create a new user with his or her password and save it in user_list
    """
    
    new_user=User(input_username,input_pin)
    new_user.save_user()
    print(User.user_list)
    print("User created")
    login()
    # return new_user

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
    choice4=str(input("Enter the account you want to delete?\n"))
    User.Credential.delete_credential(choice4)
    print("Succefully deleted")



def user_credentials():

    """
    this function is used to either display user credentials already in file,edit a account credentials,remove an account credentials,
    or save a new credit to a specific user.
    """
    print("Welcome to Credentials.Enter:\nd-to display save credentials\ne-to edit credentials\nr-to delete a credential\ns-save a new credentials\nexit-to exit the program.")
    choice2=input()
    
    if choice2=="d":
            print(" these are your save credentials\n"+ str(User.Credential.Credential_list))
            user_credentials()

    elif choice2=="e":
            print("coming soon")
            user_credentials()
    elif choice2=="r":
            if len(User.Credential.Credential_list)==0:
                print("There is no account to delete")
                user_credentials()
            else:
                delete_account()
                user_credentials()
                
    elif choice2=="s":
        generate_password()  
        user_credentials()

    elif choice2=="exit":
        exit()
        
                    
    else:
        print("Invalid entry,please try again")



def generate_password():
    """
    this function create a random password with all characters and the length is the password is 8
    """
    
    choice3=input("To create a credentials account enter:\nc- to create a custom password\ng-generate a custom password\n")
    if choice3=="c":
        account=input("Enter the account name?\n")
        password=str(input("Enter a custom a password?"))
        create_credentials(account,password)
                 
    elif choice3=="g":
        account=input("Enter the account name?\n")
        randompass = [random.choice(string.printable)for _ in range(8) ]
        password =""
        for char  in randompass:
            password+= char
    
        create_credentials(account,password)
            
               
    else:
                print("Invalid entry, please enter 'c' or 'g'")    
            
    
    
def login():
    """
    this function is used to autheticate the user using either already existing username and pin or one that he/she
    will create,after that as a existing user you will be able to access credentials accounts, if new user credentials will be empty
    """
    print("To log in to password Locker enter 'l' or to create a new user enter 'c'")
    choice1=input()
    if choice1=="l":

        login_name=input("Enter your Username>> ")
        for user in User.user_list:
            
            if login_name == user["username"]:
                login_pin=input("Proceed to enter you pin>>")
                if login_pin==user["pin"]:
                    print(login_name+" sucessfully logged in")
                    user_credentials()
                else:
                    print("You enter the wrong pin")
        print("Username not found,try again")
                
                
    elif choice1=="c":
        input_username=input("What username do you want to use?>>")
        input_pin=input("enter you preffered pin?>>")
        create_user(input_username,input_pin)
      
    else:
        print("Invalid input,please try again\nEnter the right input either c or l?")
        login()


    

    



def exit():
    print("Thank you for using Password Locker")



def main():
    print("Welcome to password locker")
    login()
    # exit()
    
    
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
