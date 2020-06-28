import unittest

from locker import User

class TestUsers(unittest.TestCase):
    '''
    Class to test application behaviour
    '''

    def setUp(self):
        '''
        Set's up user details
        '''

        self.new_account = User("Twitter", "minion", "21213")
    
    def tearDown(self):
        '''
        tearDown method that does a clean up after each test case has run
        '''
        User.store = []
    
    def test_init(self):
        self.assertEqual(self.new_account.account_name, "Twitter")
        self.assertEqual(self.new_account.account_user, "minion")
        self.assertEqual(self.new_account.account_password, "21213")
    
    def test_save_details(self):
        '''
        Test to see if the credentials are saved
        '''

        self.new_account.save_details()
        self.assertEqual(len(User.store), 1)
    
    def test_view_details(self):
        '''
        Test to see if you can view stored details
        '''

        self.assertEqual(User.view_details(), User.store)
    
    def test_view_detail(self):
        # self.new_account.new_details()
        test_detail = User("Instagram", "styles", "password")
        test_detail.save_details()

        viewing = User.view_detail("Instagram")
        
        self.assertEqual(viewing.account_user, test_detail.account_user)
    
    def test_delete_detail(self):
        User.delete_detail("Twitter")

        self.assertEqual(len(User.store), 0)

if __name__ == '__main__':
    unittest.main()