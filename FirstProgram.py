#FirstProgram.py
#Name: Tyler Menke
#Date: 08/28/24
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print("hello, what a beautiful day it is today")
  #Ask for the user's name
  name = input("What is your name? ")
  #Use the user's name in the program.
  print("nice to see you", name)
  #Ask the user for their age.
  age = input ("How old are you?")
  #Tell the user what year they were born in.
  age = int(age)
  birthYear = 2024 - age
  #Assume that they have not had their birthday yet this year.
  print("you were born in: ", birthYear)


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
