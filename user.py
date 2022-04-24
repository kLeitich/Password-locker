class User:

    user_list=["kevin","1234"]

    def __init__(self,user_name,pin):
        self.username = user_name
        self.pin = pin

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)
    
    @classmethod
    def loginuser(username,pin):
        userloggedin="kevin"
        loggedin= False
        for user in User.user_list:
            if username==user.user_name and pin == user.pin:
                userloggedin =user
                loggedin=True
        return[userloggedin,loggedin]



    class Credential:
        Credential_list=[
            {
                "twiiter":""
            }
        ]

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

    