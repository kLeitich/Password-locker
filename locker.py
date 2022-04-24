from click import pass_context


class User:

    user_list=[{"username":"kevin","password":"1421"},]

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)
    
    @classmethod
    def log_in(cls,username,password):
        for user in cls.user_list:
            if user.username == username:
                if user.password == password:
                    print("You are logged in "+ username)
                else:
                    print("Try again")
            else:
                print("username not found")
    