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
    
    def test_save_details(self):
        '''
        Test to see if the credentials are saved
        '''

        self.new_account.new_details()
        self.assertEqual(len(User.store), 1)
    
    def test_view_details(self):
        '''
        Test to see if you can view stored details
        '''

        self.assertEqual(User.view_details(), User.store)

if __name__ == '__main__':
    unittest.main()