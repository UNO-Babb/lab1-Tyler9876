#MadLib.py
#Name: Tyler menke
#Date: 08/28/24
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  location1 = input("Give a location: ")
  noun1 = input("Give an noun: ")
  action1 = input("Give an action: ")
  action2 = input("give an action: ")
  person1 = input("Give a person: ")
  hobby1 = input("Give a fun hobby: ")
  #Print the story with the user supplied words.
  print("Tuesday, I took a trip to the", location1, "with some friends, when we suddenly saw a", noun1, "on the side of the road.")
  print("We were not quite sure what it was, but we decided to",action1, " away from it.", "Man am I glad we decided to", action1, "but I wonder what would have happened if we had decide to", action2, "instead.")
  print("I think this will make for an excelent story to tell", person1, "if I get the chance. They will definitly enjoy it. Speaking of, I should check up on them and see if they are still into", hobby1)



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
