import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
       
        self.new_user = User("test","1234")

    def test_init(self):
        """
            this function create a new user for testing
        """
        self.assertEqual(self.new_user.username,"test")
        self.assertEqual(self.new_user.pin,"1234")
    
    def test_save_user(self):
        """
            this function test to see if the new user is being saved
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
class TestCredential(unittest.TestCase):
        def setUp(self):
            self.new_credentials = User.Credential("test","1234")

       
        def test_init(self):
            """
            this function create new credentials to be tested

            """
            self.assertEqual(self.new_credentials.account,"test")
            self.assertEqual(self.new_credentials.password,"1234") 
        
        
        def test_save_credentials(self):
            """
            this function test to see if the new created credentials has been saved

            """

            self.new_credentials.save_credential()
            self.assertEqual(len(User.Credential.Credential_list),4)

        

        # def test_del_credential(self):

        #     """
        #     this function test to see if the newly created user can be deleted

        #     """
        #     # self.new_credentials.save_credential()
        #     # test_account=User.Credential("test","1234")
        #     # test_account.save_credential()

        #     # self.new_credentials.delete_credential()
        #     # self.assertEqual(len(User.Credential.Credential_list),4)
        #     self.new_credentials.save_credential()
        #     test_credentials = User.Credential("Test","45678") # new credentials
        #     test_credentials.save_credential()

        #     self.new_credentials.delete_credential()# Deleting a credential object
        #     self.assertEqual(len(User.Credential.Credential_list),6)
    
    

        


if __name__ == '__main__':
    unittest.main()