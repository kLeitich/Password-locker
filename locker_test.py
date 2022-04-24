import unittest
from Locker import User

class TestUser(unittest.TestCase):
    def setUp(self):
       
        self.new_user = User("test","1234")

    def test_init(self):
        self.assertEqual(self.new_user.username,"test")
        self.assertEqual(self.new_user.password,"1234")
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),3)
    
    def test_delete_user(self):
        self.new_user.save_user()
        test_user=User("test","1234")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),2)



if __name__ == '__main__':
    unittest.main()