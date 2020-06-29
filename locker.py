import hashlib
from getpass import getpass

class Credentials:
    '''
    Class that checks the login details of the user
    '''
    
    def __init__(self):
        self.username = username
        self.password = password
    
    login_details = []

    def create_user(self, username, password):
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
            Credentials.save_user()
            User.store = [] # Creates an empty store
            user_locker = User("password-locker", username, password) # Save the locker instance as a new account entry
            User.store.append(user_locker)
        else:
            print("Password Mismatch!")
            create_user()
    
    def save_user(self):
        '''
        Function to save contact
        '''
        Credentials.login_details.append(self)

    
    def passwordChecker(self):
        userName = input()
        print('\n')
        userInput = getpass()
        password = hashlib.md5()
        password.update(userInput.encode("utf-8"))
        creds = [userName, password.hexdigest()]

        return creds

    def passwordStore(self):
        uname = 'minion'
        userPassword = "12345678"
        sWord = hashlib.md5()
        sWord.update(userPassword.encode("utf-8"))
        cred_store = [uname, sWord.hexdigest()]

        return cred_store

    def verifier(self):
        if passwordChecker() == passwordStore():
            return True
            # Call to login user
        else:
            return False
            print("\n Try again")
            print()

    def user_login(self):
        '''
        Function to call user login functions
        '''

        return verifier()

class User:
    '''
    Class that get's the user details
    '''

    def __init__(self, account_name, account_user, account_password):
        self.account_name = account_name
        self.account_user = account_user
        self.account_password = account_password
    
    store = []
    
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
        User.save_details()
    
    def save_details(self):
        '''
        Function to save details
        '''
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
    def delete_detail(cls, platform):
        '''
        Method to delete account detail
        '''
        for account in cls.store:
            if account.account_name == platform:
                User.store.remove(account)