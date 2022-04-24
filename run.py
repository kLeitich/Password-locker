from user import User


def create_user(user_name,password):
    new_user=User(user_name,password)
    new_user.save_user()
    print(new_user.user_list)
    print("User created")
    return new_user

# def save_user(user):
#     user.save_user()

def del_user(user):
    user.delete_user()

# def find_user(user_name):

#     return User.find_by_username(user_name)

# def check_username_exist(user_name):
#     return User.user_exist(user_name)
def user_credentials():
    print("Welcome to Credentials.Enter:\nd-to display save credentials\ne-to edit credentials\nr-to delete a credential\ns-save a new credentials. ")
def login():
    choice1=input()
    if choice1=="l":
        login_name=input("Enter your Username>> ")
        if login_name == User.user_list[0]:
            login_pin=input("Proceed to enter you pin>>")
            if login_pin==User.user_list[1]:
                print(login_name+" sucessfully logged in")
                user_credentials()
            else:
                print("You enter the wrong pin")
        else:
            print("Username not found")
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
