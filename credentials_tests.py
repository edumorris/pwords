import unittest

from locker import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Class to test application's credentails behaviour
    '''
    def setUp(self):
        '''
        Set's up variable to be used
        '''

        self.new_user = Credentials("minion", "123456")

    def test_user_login(self):
        '''
        Test to see if a user can login in
        '''
        
        self.assertEqual(self.new_user.username, "minion")
        self.assertEqual(self.new_user.password, "123456")
    
    def test_save_user(self):
        '''
        Test to see if new user is being saved
        '''

        self.new_user.create_user()
        self.assertEqual(len(Credentials.login_details), 1)

    def test_login(self):
        self.existing_user.user_login()
        self.assertEqual(Credentials.user_login(), True)


        

if __name__ == '__main__':
    unittest.main()