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

    locker.save_user()

def login():
    '''
    Function to login user in
    '''
    return Credentials.user_login()


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
    account.save_details()

def view_account(account):
    '''
    Function to view account
    '''
    return account.view_detail()

def view_accounts():
    '''
    Function to view saved accounts
    '''
    return User.view_details()



def main():
    '''
    Main function
    '''
    print("!!!Welcome to the Password Locker!!!\n")
    print("Use the follwing shortcodes to continue: \n")
    print("lg - login\ncl - create locker")
    print("Enter a code to continue: ")
    short_code = input().lower()

    if short_code == 'cl':
        print("Create your new password locker: \n")
        print("Enter your preffered username: ")
        username = input()
        print("Enter your preffered password: ")
        passcode = getpass()
        print("Confirm password: ")
        pass_conf = getpass()

        if passcode == pass_conf:
            save_locker(create_new_locker(username, passcode))
            save_account_entry(create_account_entry("password_locker", username, passcode))
            print(f"New locker under username: {username}, has been created\nYou can now login using your details. Use shortcode 'lg' to login")
            main()
        else:
            print("Passwords don't match! Try again!\n")
            main()
    elif short_code == 'lg':
        login()
        if True:
            print("Welcome to your locker. Use the following shortcodes for navigation:\n")
            print("ca - create a new entry \nva - View saved accounts \nsl - search for a saved account \nda - Delete account entry\nex -exit")
            code = input().lower()
            if code == "ca":
                print("Enter new account details:\n")
                print("Plaform name: ")
                p_name = input()
                print('\n')
                print("Enter username: ")
                p_user = input()
                print('\n')
                print("Enter password: ")
                p_pwd = input()
                print('\n')

                save_account_entry(create_account_entry(p_name, p_user, p_pwd))
                print(f"New account detail created: {p_name}, {p_user}")
                print('\n')
            elif code == "va":
                print("Accounts in locker:\n")

                for account in view_accounts():
                    print(f"{account.accountName}, {account. accountUserName}, {account.accountPassword}")     
            elif code == "sl":
                print("Enter account you want to search for: ")
                platform_name = input()
                account_info = view_account(platform_name)
                print(f"{account_info.accountName}, {account_info.accountUserName, account_info.accountPassword}")
            elif code == "da":
                # Code to delete account entry
                print("Enter name for account to delete: \n")
                del_acc = input()
            elif code == "ex":
                print("Application closed!")
                
            else:
                print("Invalid code entered!")
            # Codes for account navigation
        else:
            print("Username or password error!")

if __name__ == '__main__':
    
    main()