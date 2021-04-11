studentsInfo = {}

for i in range(5):
        name = input(f"Enter student {i+1}'s name: ")

        #Get input from user and check if it is valid.
        while True:
                try:
                        midtermGrade, projectGrade, finalGrade = map(float ,input(f"Enter student {i+1}'s midterm, project, and final grades in this order using spaces: ").split())
                        break

                except ValueError:
                        print("Please enter a number.")

        passingGrade = float(format((midtermGrade * 0.3) + (projectGrade * 0.3) + (finalGrade * 0.4), ".2f"))

        #Add the new student to the dictionary.
        studentsInfo.update({f"Student {i+1}": {"Name": name, "Midterm Grade": midtermGrade, "Project Grade": projectGrade, 
				         "Final Grade": finalGrade, "Passing Grade": passingGrade}})
        
        print(f"Student {i+1}'s passing grade is {passingGrade}. \nStudent {i+1}'s data has been added.")

passingGrades = sorted([grade.get("Passing Grade") for grade in studentsInfo.values()], reverse=True)

print(f"Here is the list of the students' passing grades from highest to lowest. \n{passingGrades}")
