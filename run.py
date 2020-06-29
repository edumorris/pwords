from locker import Credentials
from locker import User

def login():
    '''
    Login function
    '''
    return Credentials.user_login()

def create_account(acc_name, acc_user, acc_password):
    '''
    New account function
    '''
    new_account = User(acc_name, acc_user, acc_password)
    return new_account

def save_account(account):
    '''
    Function to save new account details
    '''

    User.save_details()


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