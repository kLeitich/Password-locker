from httplib2 import Credentials


class User:

    user_list=[]

    def __init__(self,user_name,pin):
        self.username = user_name
        self.pin = pin

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)
    
    @classmethod
    def find_by_username(cls,username):
        for user in cls.user_list:
            if user.username==username:
                return user
    class Credential:
        Credentials=[]

        def __inti__(self,account,password):
            self.account = account
            self.password=password

        def
    