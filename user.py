class User:

    user_list=[
        {
            "username":"kevin",
            "pin":"1234"
        }
        ]

    def __init__(self,user_name,pin):
        self.username = user_name
        self.pin = pin

    def save_user(self):
        # print(self)
        # print(self.username)
        # print(self.pin)
        
        User.user_list.append({
            "username": self.username,
            "pin": self.pin
        })

    def delete_user(self):
        User.user_list.remove(self)
    
    
    class Credential:
        Credential_list=[
            {
                "user":"kevin",
                "credentials":{
                    
                "twitter":"tweet@1234",
                "facebook":"fb@9101",
                "tiktok":"tik@3141"
            
                }
            }
        ]

        def __init__(self,account,password):
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

    