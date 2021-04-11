#Create a list and swap the second half of the list with
#the first half of the list and print this list on the screen
while True:
        try:
                userList = input("Enter the items you want in your list using commas(i.e 1,2,3,4): ").split(",")

                if(len(userList) % 2 == 0):
                        middlePoint = len(userList)//2
                        userList = userList[middlePoint:] + userList[:middlePoint]

                        print(userList)
                        break
                
                else:
                        print("Make sure the length of your list is even")

        except:
                print("An error occured. Please try again.")






