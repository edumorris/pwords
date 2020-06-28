import hashlib

def passwordChecker():
    userInput = input(str("Please enter password!"))
    password = hashlib.md5()
    password.update(userInput.encode("utf-8"))

    return password.hexdigest()

def passwordStore():
    userPassword = "12345678"
    sWord = hashlib.md5()
    sWord.update(userPassword.encode("utf-8"))

    return sWord.hexdigest()

def verifier():
    if passwordChecker() == passwordStore():
        print(True)
    else:
        print(False)
        print("\n Try again")
        print()
        verifier()

verifier()