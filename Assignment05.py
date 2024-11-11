# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Katherine Sather, 11/10/2024, Modified script started by RRoot
# ------------------------------------------------------------------------------------------ #

import json # import code from Python's json module into my script

# Define the data, ensuring student_data is a dictionary

student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Initialize as an empty string
file = None  # Holds a reference to an opened file.
menu_choice: str = '' # Hold the choice made by the user.

FILE_NAME: str = "Enrollments.json"

#Start the program by reading current file contents

try:
    file = open(FILE_NAME, "r")# Open the JSON file for reading
    students = json.load(file) #load the json
    # Now 'data' contains the parsed JSON data as a Python list of dictionaries
    # Now we'll print contents of the Enrollments file
    for student in students:
        print(f"First name: {student['FirstName']}, Last name: {student['LastName']}, Course name: {student['CourseName']}") #printing the contents of the file
except Exception as e:
    print("Something went wrong. Make sure the file exists and has valid json content and try again. \n")
    print("-- Technical Error Message -- ")
    print(e)          # Print the exception object (typically includes the error message)
    print(type(e))    # Print the type of the exception object
    print(e.__doc__)  # Print the documentation string of the exception type
    print(e.__str__())  # Print the string representation of the exception

# Defining another data constant

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, #key followed by value, for a key-value pair
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
        except Exception as e:
            print("An error occurred when registering a student. Please check your input and try again. \n")
            print("-- Technical Error Message -- ")
            print(e)  # Print the exception object (typically includes the error message)
            print(type(e))  # Print the type of the exception object
            print(e.__doc__)  # Print the documentation string of the exception type
            print(e.__str__())  # Print the string representation of the exception
        continue


    # On menu choice 2, the presents a string by formatting the collected data using the print() function.
    # Data collected for menu choice 1 is added to a two-dimensional list table (list of dictionaries).
    # All data in the list is displayed when menu choice 2 is used.

    #show current data when the user chooses menu choice 2
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50) #prints out a series of dashes as part of formatting the display message
        for student in students: #this is a for loop and we are defining student. Each time the loop iterates through students, student will be populated with data of each element in students
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")#f-strings for formatting of content
        print("-"*50)
        continue



    # On menu choice 3, the program opens a file named "Enrollments.json" in write mode using the open() function.
    # It writes the content of the students variable to the file using the dump() function, then file is closed using the close() method.
    # Then displays what was stored in the file.

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()

            print("The following data was saved to file!")
            file = open(FILE_NAME, "r") #opens the file and reads all content
            contents = file.read() #stores contents in a variable called contents
            print(contents) #prints contents
            file.close()
        except Exception as e:
            print("Something went wrong saving student data. Try again!\n")
            print("-- Technical Error Message -- ")
            print(e)  # Print the exception object (typically includes the error message)
            print(type(e))  # Print the type of the exception object
            print(e.__doc__)  # Print the documentation string of the exception type
            print(e.__str__())  # Print the string representation of the exception

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
