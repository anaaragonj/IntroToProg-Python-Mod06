# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Ana Aragon,9/3/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

#Processing
class fileProcessor:

    def read_data_from_file(file_name: str, student_data: list):#reads from json file and make it a list of dictionary rows
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_message(message = "Error: There was a problem with reading the file.", exception=e)
        
        finally:
          if file.closed == False:
            file.close()
        return student_data
    
    def write_data_from_file(file_name: str, student_data: list):#writes data to a json file 
        try: 
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_and_course_name(student_data=student_data)
        except Exception as e:
            message = "Error: Please try again\n"
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()
#Presentation
class IO:
    @staticmethod
    def output_error_message(message: str, error: Exception = None) : #custom error messages to the user
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error._doc_, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str): #menu of choices
        print() #space
        print(menu)
        print() #more space

    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
                IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message\
        return choice
        
    @staticmethod
    def output_student_and_course_name(student_data: list):
    # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        try:
        # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            # using a nested try block to capture when an input cannot be changed to a float
            course_name = input("What is the course name? ")
            student = {"FirstName": student_first_name,
                    "LastName": student_last_name,
                    "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="That value is not the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a non-specific error!", error=e)
        return student_data


while (True):

    # Present the menu of choices
    #print(MENU)
    IO.output_menu(menu=MENU)
    #menu_choice = input("What would you like to do: ")
    menu_choice = IO.input_menu_choice()


    # Input user data
    if menu_choice == "1":

        students=IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_name(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        fileProcessor.write_data_from_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
