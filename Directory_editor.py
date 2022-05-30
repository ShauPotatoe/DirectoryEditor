import os

print("Welcome to the Data File adder.")

def main():
    """Creates a file with Name address and phone number"""

    # inputs are for finding the directory, creating a name for the file, and adding data to the file
    directory = input("Which directory would you like the file to go to?")
    file = input("Whats the name of the file that your would like to add?")
    name = input("What is your name?")
    address = input("What is your address?")
    number = input("What is your phone number?")

 
    
    
    # See if the directory exists
    if os.path.isdir(directory):

        """
        This is to open a new file based on which directory was entered and what the name of the file is. 
        The 'w' is to tell python that you want the file in write mode
        """
        Newfile = open(os.path.join(directory, file),'w')

        # This is a print of what will be writed on to the file after the inputs.
        Newfile.write(name+ "'s address is " +address+" and their phone number is "+number)

        # Closes the file
        Newfile.close()

        print("This file contains the following:")

        # This variable is set up for showing what is in the file.
        # 'r' is written here to tell python to put the file in read mode
        readFile = open(os.path.join(directory,file),'r')

        # Print each line from readFile
        for line in readFile:
            print(line)
    
    elif not os.path.exists(directory):
        #This is the directory that will be created using your main directory
        directory = os.path.join("C:\\","temp","python")
        #This is the message created when the directory is not found
        print("The directory entered was not found and will be created under C:\temp\python")
        
        os.mkdir(directory)

        
        """
        This is to open a new file based on which directory was entered and what the name of the file is. 
        The 'w' is to tell python that you want the file in write mode
        """
        Newfile = open(os.path.join(directory, file),'w')

        # This is a print of what will be writed on to the file after the inputs.
        Newfile.write(name+ "'s address is " +address+" and their phone number is "+number)

        # Closes the file
        Newfile.close()

        print("This file contains the following:")

        # This variable is set up for showing what is in the file.
        # 'r' is written here to tell python to put the file in read mode
        readFile = open(os.path.join(directory,file),'r')

        # Print each line from readFile
        for line in readFile:
            print(line)



main()
#Refrence:
#Python directory. Python Tutorial - Master Python Programming For Beginners from Scratch. (2021, July 7). 
#Retrieved May 30, 2022, from 
#https://www.pythontutorial.net/python-basics/python-directory/#:~:text=To%20create%20a%20new%20directory,the%20c%3A%5Ctemp%20directory. 

#Matthes, E. (2019). Python crash course: A hands-on, project-based introduction to programming (2nd ed.). No Starch Press. 