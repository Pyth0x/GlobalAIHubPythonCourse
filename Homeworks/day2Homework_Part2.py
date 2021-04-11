#Ask the user to input a single digit integer to a variable 'n'.
#Then, print out all of the even numbers from 0 to n(including n)

while True:
        try:
                num = int(input("Number: "))
                break

        except ValueError:
                print("Please enter a number.")

print(",".join([str(i) for i in range(num+1) if i % 2 == 0]))
