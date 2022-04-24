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
        Credential_list=[]

        def __inti__(self,account,password):
            self.account = account
            self.password=password

        def save_credential(self):
            self.Credential_list.append(self)


        def delete_credential(self):
            self.Credential_list.remove(self)
        
        @classmethod
        def find_by_account(cls,account):
            for cred in cls.Credential_list:
                if cred.account==account:
                    return cred

    