from locker import Credentials
from locker import User

def login():
    '''
    Login function
    '''
    return Credentials.user_login()

def create_account(self):
    '''
    New account function
    '''
    return Credentials.create_user()

def main():
    '''
    Main Program run
    '''
    print()
    print("Welcome to the password manager!\n")
    print("Please select an option from the short codes below:\n")
    print(" lg - login\n cl - Create new locker")
    print()
    print("Enter short code:")
    shortcode = input().lower()

    if shortcode == 'cl':
        print("Create your new account")
        create_account()
    elif shortcode == 'lg':
        print("Login")
        login()   


if __name__ == "__main__":
    main()