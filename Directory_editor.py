from distutils.file_util import write_file
import os
print("Welcome to the Data File adder.")
def main():
    #inputs are for finding the directory, creating a name for the file, and adding data to the file
    directory = input("Which directory would you like the file to go to?")
    file= input("Whats the name of the file that your would like to add?")
    name = input("What is your name?")
    address = input("What is your address")
    number = input("What is your phone number")
    #If statement is to see if the directory exists
    if os.path.isdir(directory):
        #This is to open a new file based on which directory was entered and what the name of the file is. 
        #The 'w' is to tell python that you want the file in write mode
        Newfile = open(os.path.join(directory, file),'w')
        #This is a print of what will be writed on to the file after the inputs.
        Newfile.write(name+ "'s address is " +address+" and their phone number is "+number+".")
        #Closes the file
        Newfile.close()
        print("This file contains the following:")
        #This variable is set up for showing what is in the file.
        #'r' is written here to tell python to put the file in read mode
        readFile = open(os.path.join(directory,file),'r')
        #This is a loop to print each line from readFile
        for line in readFile:
            print(line)
    else:
        print("The directory entered was not found")
main()