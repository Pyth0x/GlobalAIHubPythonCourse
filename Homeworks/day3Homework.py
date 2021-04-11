#Login without using dictionary
def loginWithoutDict():
        username = "berk"
        password = "123456"

        inputedUsername = str(input("Username: ")).strip()
        inputedPassword = str(input("Password: ")).strip()

        while((inputedUsername != username) or (inputedPassword != password)):
                print("Wrong username or password. Please try again.")
                inputedUsername = str(input("Username: "))
                inputedPassword = str(input("Password: "))

        print(f"Welcome {username.capitalize()}!")

if __name__ == "__main__":
        loginWithoutDict()

