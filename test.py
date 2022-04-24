import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
       
        self.new_user = User("test","1234")

    def test_init(self):
        self.assertEqual(self.new_user.username,"test")
        self.assertEqual(self.new_user.pin,"1234")
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
    def tearDown(self):

        User.user_list=[]
    def test_delete_user(self):
        self.new_user.save_user()
        test_user=User("test","1234")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
    def test_find_user_by_username(self):
        self.new_user.save_user()
        test_user=User("test","1234")
        test_user.save_user()

        found_user=User.find_by_username("test")
        self.assertEqual(found_user.username,test_user.username)
        




if __name__ == '__main__':
    unittest.main()