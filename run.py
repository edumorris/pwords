import hashlib
from getpass import getpass

from locker import Credentials
from locker import User

def create_new_locker(uname, pwd):
    '''
    Function to create a new locker
    '''

    new_locker = Credentials(uname, pwd)

def save_locker(locker):
    '''
    Function to save contact
    '''

    Credentials.save_user()

def login():
    '''
    Function to login user in
    '''
    Credentials.user_login()


def create_account_entry(acc, acc_uname, acc_pwd):
    '''
    Function to create account
    '''
    new_account = User(acc, acc_uname, acc_pwd)
    return new_account

def save_account_entry(account):
    '''
    Function to save account entry
    '''
    User.save_details()

def view_account(account):
    '''
    Function to view account
    '''
    return User.view_detail(account)

def view_accounts():
    '''
    Function to view saved accounts
    '''
    return User.view_details()



def main():
    '''
    Main function
    '''

if __name__ == "__main__":
    main()