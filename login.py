import hashlib
from getpass import getpass

class LoginVerification:
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
        else:
            return False
            print("\n Try again")
            print()
        verifier()