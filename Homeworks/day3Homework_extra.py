#Login with using dictionary
def loginWithDict():
        userInfos = {
                "berk": "123456",
                "ali": "1234",
                "fatma": "123",
                "ayşe": "12"}

        userInput = {str(input("Username: ")): str(input("Password: "))}

        check = True
        while check:
                for key in userInfos:
                        if(key in userInput and userInfos[key] == userInput[key]):
                                print(f"Welcome {key.capitalize()}!")
                                check = False
                                break
                        else:
                                print("Wrong username or password. Please try again.")
                                userInput = {str(input("Username: ")): str(input("Password: "))}
                                break

if __name__ == "__main__":
        loginWithDict()
