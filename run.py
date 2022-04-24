from user import User


def create_user(user_name,password):
    new_user=User(user_name,password)
    return new_user

def save_user(user):
    user.save_user()

def del_user(user):
    user.del_user()

def find_user(user_name):

    return User.find_by_username(user_name)

def check_username_exist(user_name):
    return User.user_exist(user_name)


def main():
    print("Welcome to password locker")
    print("To log in to password Locker enter 'l' or to create a new user enter 'c'")
    login_input=input().lower()
    if login_input=='l':
        print("Enter your Username?")
        
        loginuser=input()
        if check_username_exist(loginuser):
            search_username= find_user(loginuser)
            print(search_username)


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
