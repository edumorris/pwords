import hashlib
from getpass import getpass



class Credentials:
    '''
    Class that checks the login details of the user
    '''
    login_details = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_user(self):
        print("Select a username:")
        print()
        username = input()
        print("Enter password:")
        password = getpass()
        print("Verify password:")
        password_ver = getpass()

        if password == password_ver:
            new_user = Credentials(username, password)
            print("Success! User created")
            Credentials.login_details.append(self)
        else:
            print("Password Mismatch!")
            create_user()

    def user_login(self):
        def passwordChecker(self):
            userInput = getpass()
            password = hashlib.md5()
            password.update(userInput.encode("utf-8"))

            return password.hexdigest()

        def passwordStore(self):
            userPassword = "12345678"
            sWord = hashlib.md5()
            sWord.update(userPassword.encode("utf-8"))

            return sWord.hexdigest()

        def verifier(self):
            if passwordChecker() == passwordStore():
                return True
                # Call to login user
            else:
                return False
                print("\n Try again")
                print()
        
        verifier()


class User:
    '''
    Class that get's the user details
    '''

    store = []

    def __init__(self, account_name, account_user, account_password):
        self.account_name = account_name
        self.account_user = account_user
        self.account_password = account_password
    
    def new_details(self):
        print("Add new account to your locker!\n")
        print("Enter account name: ")
        accountName = input()
        print("\n")
        print("Enter account username: ")
        accountUserName = input()
        print("\n")
        print("Enter account password: ")
        accountPassword = input()
        print("\n")

        new_account = User(accountName, accountUserName, accountPassword)
        User.store.append(self)
        

    @classmethod
    def view_details(cls):
        '''
        Method to display stored user accounts
        '''

        return cls.store
    
    @classmethod
    def view_detail(cls, platform):
        '''
        Method to view a single account detail
        '''

        for account in cls.store:
            if account.account_name == platform:
                return account

    @classmethod
    def delete_detail(cls, account_name):
        '''
        Method to delete account detail
        '''
