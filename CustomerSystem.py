# Throughout this project, the use of data structures are not permitted
# Minimal built in functions are to be used and the majority of functions must be
# created yourself
# More packages may be imported in the space below if approved by your instructor
def printMenu():
  print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')


'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''


def enterCustomerInfo():
  firstName = ""
  lastName = ""
  city = ""
  postalCode = ""
  creditCardNum = ""
  valid = False

  #First Name
  print("Enter First Name:")
  firstName = getCustomerInfo(firstName)
  #Last Name
  print("Enter Last Name:")
  lastName = getCustomerInfo(lastName)
  #City
  print("Enter City:")
  city = getCustomerInfo(city)

  #Postal Code
  while valid == False:
    print("Enter Postal Code:")
    postalCode = getCustomerInfo(postalCode)
    try:
      valid = validatePostalCode(postalCode)
      if valid == True:
        print("Postal Code Valid.")
    except:
      print("Invalid Postal Code. Please enter a valid postal code!")

  #Credit Card
  valid = False
  while valid == False:
    print("Enter Credit Card Number:")
    creditCardNum = getCustomerInfo(creditCardNum)
    valid = validateCreditCard(creditCardNum)
    if valid == True:
      print("Credit Card Valid.")
    else:
      print("Invalid Credit Card. Please enter a valid credit card number.")

  #Add the stuff into a temperary customer data file.
  userId = getUserId()
  f = open("CustomerData.csv", "a")
  f.writelines("\n")
  f.writelines("User " + str(userId) + " | " + firstName + " | " + lastName +
               " | " + city + " | " + postalCode + " | " + creditCardNum)
  f.close()


'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''


def validatePostalCode(postalCode):
  valid = False
  #Check if the length is less than 3
  if findLength(postalCode) < 3:
    return valid
  else:
    with open("postal_codes.csv") as file:
      for line in file:
        if postalCode[0:3] == line[0:3]:
          valid = True
          return valid
  return valid


'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''


def validateCreditCard(creditCard):
  valid = True
  try:
    #Find the length
    if findLength(creditCard) < 9:
      valid = False
    else:
      #Reverse Card Number
      creditCard = reverseNumber(creditCard)
      #For odd numbers
      oddPartialSum = 0
      for x in range(findLength(creditCard)):
        #Since x starts from 0, every even x is an odd digit
        if x % 2 == 0:
          oddPartialSum = oddPartialSum + int(creditCard[x])
      #For even numbers
      evenPartialSum = 0
      numCheck = 0
      for x in range(findLength(creditCard)):
        numGood = False
        #Every even digit
        if x % 2 != 0:
          numCheck = int(creditCard[x]) * 2
          if numCheck < 9:
            evenPartialSum = evenPartialSum + numCheck
          else:
            while numGood == False:
              numCheck = str(numCheck)
              #Add the two digits
              numCheck = int(numCheck[0]) + int(numCheck[1])
              #Check if the new number is good
              if numCheck < 9:
                numGood = True
            evenPartialSum = evenPartialSum + numCheck
      #Final number to check
      finalSum = evenPartialSum + oddPartialSum
      if finalSum % 10 == 0:
        valid = True
      else:
        valid = False
  except:
    #If there is any error in the input
    valid = False
  return valid


'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''


def generateCustomerDataFile():
  #Allow the user to create their own file name and choose the file location 
  fileName = input("Enter file name: ")
  fileName = fileName + ".csv"
  fileLocation = input("Enter file location: ")
  filePath = fileLocation + fileName

  #Copy everything from customer data csv to the user's own file
  with open('CustomerData.csv', 'r') as firstfile, open(filePath, 'a') as secondfile:
    # read content from first file
    for line in firstfile:
      # append content to second file
      secondfile.write(line)


####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################

def getUserId():
  global userId
  count = 0
  with open('CustomerData.csv', 'r') as file:
    for line in file:
      count += 1
  userId = count - 1
  return userId
      
#Reverse a number
def reverseNumber(thing):
  reversed = ""
  length = findLength(thing)
  for x in range(1, length + 1):
    x = x * (-1)
    reversed = reversed + thing[x]
  return reversed

#Find length of thing
def findLength(text):
  count = 0
  for char in text:
    count += 1
  return count

#Ask for input and confirm if thats what user meant to type
def getCustomerInfo(info):
  confirmation = False
  confirm = ""
  #Last Name
  while confirmation == False:
    invalid = True
    #Ask for user input
    info = input("-> ")
    while invalid == True:
      #Ask for user to double check their info
      print("Is " + info + " correct? [Yes/No]")
      confirm = input("Yes or No: ")
      if confirm == "Yes":
        invalid = False
        confirmation = True
      if confirm == "No":
        invalid = False
      if confirm != "Yes" and confirm != "No":
        invalid = True

  return info


####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below
userId = 1

while userInput != exitCondition:
  printMenu()  # Printing out the main menu
  userInput = input()
  # User selection from the menu

  if userInput == enterCustomerOption:
    # Only the line below may be editted based on the parameter list and how you design the method return
    # Any necessary variables may be added to this if section, but nowhere else in the code
    enterCustomerInfo()

  elif userInput == generateCustomerOption:
    # Only the line below may be editted based on the parameter list and how you design the method return
    generateCustomerDataFile()

  else:
    print("Please type in a valid option (A number from 1-9)")

#Exits once the user types
print("Program Terminated")