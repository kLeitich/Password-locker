class User:

    user_list=[
        {
            "username":"kevin",
            "pin":"1234"
        }
        ]

    def __init__(self,user_name,pin):
        """
            this function create a new
        """
        self.username = user_name
        self.pin = pin

    def save_user(self):
        """
            this function save a new user that is being created in user list
        """
        User.user_list.append({
            "username": self.username,
            "pin": self.pin
        })

    # def delete_user(self):
    #     User.user_list.remove(self)
    
    
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
            """
            this function create a new account and password to be saved in credentials

            """
            self.account = account
            self.password=password
              
            

        def save_credential(self):
            """
            this function save the new created account credentials
            """
            self.Credential_list.append( 
                    {
                        self.account,self.password
                    }
                
            )
            
    