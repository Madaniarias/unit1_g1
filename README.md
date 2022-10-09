# Crypto Wallet

![giphy](https://user-images.githubusercontent.com/111761417/194739829-e8c96274-ca8d-41d0-94b4-1601a1ad986e.gif)

<sub>Illustration by Crypto GIF</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

Design statement:
I will design and make a Crypto Wallet for a client who is local trader. The project will be about designing a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics and is constructed using the software Python 3.10.7. It will take about 3 weeks to make and will be evaluated according to the criteria below.

For this project, the cryptocurrency used will be Cardano.

Cardano is one of the biggest cryptocurrencies by market cap. It’s designed to be a flexible, sustainable, and scalable blockchain platform for running smart contracts — which will allow the development of a wide range of decentralized finance apps, new crypto tokens, games, and more. Cardano’s goal is to be the most environmentally sustainable blockchain platform. It uses a unique proof-of-stake consensus mechanism called Ouroboros, as opposed to the energy-intensive proof-of-work system currently used by Bitcoin and Ethereum. (Ethereum is also moving to a proof-of-stake system via the ETH2 upgrade). Cardano was launched in September 2017 by Ethereum co-founder Charles Hoskinson, and aims to be a third-generation blockchain (or blockchain 3.0) project — building on top of the technology pioneered by Bitcoin (first gen) and Ethereum (second gen). Cardano’s goal is to be a highly scalable and energy-efficient smart contract platform. In the second quarter of 2021, smart contract functionality is scheduled to arrive on the Cardano platform. Developers have also announced that the blockchain will become compatible with Ethereum-based smart contracts later in the year — potentially allowing it to run a wide range of existing apps and allowing developers to work on Cardano projects using the familiar Solidity programming language ([1])(https://www.coinbase.com/learn/crypto-basics/what-is-cardano)
The values of Cardano as of Sunday, October 9 is around 61.24 Japanese yen.

1. What is Cardano? Coinbase. September 23, 2022. https://www.coinbase.com/learn/crypto-basics/what-is-cardano

Justify the tools/structure of your solution

The following arguments make python a good tool for the solution of this project:
- It is a free software, which means there will not be any additional cost for the user regarding software usage for the creating of the electronic ledger.
- Python is cross-platform and will work on Windows, macOS, and Linux, which means that it will be accesible to download from almost any computer.
- The software does not take much space and it is easy and quick to download (It can be download from their webpage in a matter of minutes).

CODE OF THE PROGRAM IS IN THE MEDIA FILE ALONG WITH THE FUNCTIONALITY TEST.
username: Sato
Password: mssato

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger displays records of transactions by month.
5. The electronic ledger diplays current mean income as of last transaction made.
6. The electronic ledger is protected by a password to gain access to the data.

# Criteria B: Design

## System Diagram

![image](https://user-images.githubusercontent.com/111761417/194739407-aeb7a1a7-aad3-451c-a7a5-07efc3689de7.png)
<sub>System Diagram is divided in Keyboard and Screen (Connected). Following by the computer (MacBook Air) and Processor (Dual-Core Intel Core i5 1.8GHz 8GB. Next, the Operating System (OS: MacOS 12.5 (21G72). For the software we are using Python 3.10.7. Lastly, inside the software we have 2 python files and 3 csv (comma separated value) files.
  
## Flow Diagrams

### FUNCTION VALIDATE_INT_INPUT

![image](https://user-images.githubusercontent.com/111761417/194739562-326b85ad-57e6-4a8c-a67b-834aaf3a60ec.png)
  
<sub>The function VALIDATE_INT_INPUT is used to validate the user is entering a number for the input. 

### FUNCTION VALIDATE_MONTH

![image](https://user-images.githubusercontent.com/111761417/194739540-9d33d699-437c-4f3f-9f73-c0e3462654bf.png)
<sub>The function VALIDATE_MONTH is used to validate the user is entering a the month in the correct format for the input.

### FUNCTION SIMPLE_LOGIN
  
![image](https://user-images.githubusercontent.com/111761417/194739593-194266e3-b51f-4d49-a832-80487fe5e613.png)
![image](https://user-images.githubusercontent.com/111761417/194739615-a0a8327e-3976-43a0-8a1d-4cf479d42670.png)
<sub>The function SIMPLE_LOGIN is used to grant o deny access the user validate the user and password they enter for the input.

## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram                                         | To have a clear idea of the hardware and software requirements for the proposed solution  | 10min         | Sep 22                 | B         |
| 2.      | Flow diagram login.  |   Created a flow diagram for the login system to better see and plan the code of the login system | 10 min | Sep 27 | B
| 3.      | Code and test login  | Coded a simple login system with a function called simple_login and tested it with a set password (mssato) and username (Sato). Add messages when you give acces or deny it. | 50 min | Sep 27 | C
| 4.      | Test login and add message for user　　　　　　| Login system runs properly, displays message when acces is granted or denied.            | 2 min  | Sep 27 | D
|5.       |Code validate functions | Create functions to validate user input: 1) validate_int_input: to validate that the input entered by the user is an integer. 2) validate_choice_input: to validate that the user input maches one of the option given that are in string format (options A to D) 3) validate_category: to validate that the user's input is a string. 4) validate_month: to validate the user's inut matched the month format used in the prgogram| 3 hours | Oct 9 | C
|6.       | Flow diagram for validate functions | Created a flow diagram for the validate functions | 30 min | Oct 9 | B
|7.       | Create other functions | Create author function: to display information about the author of the program | 5 min | Oct 9 | C
|8.       | Code menus for options | Code a menus that display the options to the user after login so it can be easy to identify what the user wants to do| 30 min | Oct 9 | C
|9.       | Code options form the menu | Code each option from the menu so when the user selects it, it runs in the terminal what the user wants to do | 10 hours | Oct 9 | C
|10.       | Alpha-Testig  | Test every opion from the menu and look for mistakes that may be causing a bad experience to the user | 5 min | Oct 9 | D
|11.      | Beta-Testing | Ask external person to test the program and give feedback. It was tested by some classmates and housemates. Feedback: Print menu again, more colors, add emojis. | 20 min | Oct 9 | D
|12.      | Fix errors.  | Fix errors pointed by the user during the beta-testing and do alpha-testing again | 1 hour | Oct 9 | C
|13.      | Alpha-testing again | Test the porgram again to check it is running anf the issues pointed in the beta-testing were fixed | 1 hour | Oct 9 | D

 # CRITERIA C: Development
 
 CODE OF THE PROGRAM IS IN THE MEDIA FILE ALONG WITH THE FUNCTIONALITY TEST.
 username: Sato
 Password: mssato
  
 ## Existing tools
  - For loops
  - Functions
  - While loops
  - If statements
  - Input validation
  - Unicodes (color/emojis/background/underline/bold)
  - Reading/Appending/writting csv files
  
  ## Sources
  Emoji Unicodes
  - https://unicode.org/emoji/charts/full-emoji-list.html#1f609
  
 ## FUNCTIONS
 Some of the main function running in the Crypto Wallet are:
 
  ### Validate_int_input
  
  ```.py
  def validate_int_input(prompt:str)->int:
    end_code = "\033[00m"
    red = "\033[0;31m"
    num = input (prompt)
    while not num.isdigit():
        num = input (f"{red}ERROR! Enter a number (e.g. 4).\n{prompt}{end_code}")

    return int(num)
  ```
  This function is validating that the input entered by the user is an integer. The assigned name for the function is "validate_int_input" and it will recieve a prompt in form of a str but will return an integer. Inside the function there is unicodes for the color red and to end the color so we can make the ERROR message more noticeable and obvious to the user. Then, we assign the variable name "num" to the prompt given and use a while loop to ask the program that while the what got stored in the variable "num" is not a number, show an ERROR message to the user and, at the same time, ask once agian for input form the user. Lastly, we return "num" as an integer.
  
### One use of the validate_int_input function in the Crypto wallet
  ```.py 
#MAIN OPTION MENU
  
#Printing menu of options for the user
menu_initial = f"""{colors[5]}1. I want to learn more about Cardano
2. Enter transaction
3. Withdrawn transaction
4. My past transactions
5. Statistics
6. Current balance
7. More about the author
8. exit
{end_code}"""

option = -1
# OPTION 8: EXIT
while option != 8:
    # validating user's input calling the function validate_int_input from crypto_library
    option = validate_int_input(f"{background[4]}{'Options'.center(50)}{end_code}\n{menu_initial}{background[3]}Please enter an option [1-8]:{end_code}　")
    while option > 8 or option < 1:
        option = validate_int_input(f"{colors[1]}ERROR! {option} is incorrect.{end_code}\n{'Options'.center(50)}\n{menu} Please enter an option [1-8]: {end_code}")
 ```
In this occassion we are validating the users input with the function validate_int_input to make sure that he is indeed entereing a number between the range 1 to 8. We are using the function not only when we first ask to select an option but, after the while loop, it will again validate the users input.
In this piece of code we are also incorporating the use of the while loop to create an exit option that will allow the user to exit the program whenever they want to.
This piece of code prints the main menu after the user logs in. Then, while the option is not 8, we are storing in the variable name "option" the input from the user ans uusing the validate_int_input function to check if it is an integer. Lastly, while the user inputs a number out of teh range 1-8, an error message will show asking to try again and validating once again the input from the user.
                                   
 ### Validate_month
  
 ```.py
  def validate_month(prompt:str)->str:
    """..."""
    end_code = "\033[00m"
    red = "\033[0;31m"
    month = input(prompt)
    month = month.lower()
    while not month in ["jan", "feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]:
        month = input (f"{red}ERROR! The month must be written with the first 3 letters of the month (e.g oct).{prompt}{end_code}\n")

    return month
```
   This function is validating that the input entered by the user is a string that is within a certain list of strings. The assigned name for the function is validate_month and it will recieve a prompt in form of a string and will return it as a string as well. Inside the function there is unicodes for the color red and to end the color so we can make the ERROR message more noticeable and obvious to the user. Then, we assign the variable name "month" to the prompt given and use a while loop to ask the program that while the what got stored in the variable "month" is not a within the list of strings (months of the year), show an ERROR message to the user and, at the same time, ask once agian for input form the user. Lastly, we return "month" as a string.
 
 ### One use of the validate_month function in the Crypto wallet
 
 ```.py
 #OPTION 1: TRANSACTION BY MONTH
        if option == 1:
            #Asking input from user and validating with function validate_month
            in_month = validate_month("Enter the month you would like to see the transactions from (First 3 letters of month: e.g. Oct): ")
            with open("database.csv", "r") as file:
                crypto_data = file.readlines()
            i=0
            heading = '-' * 24
            print(f"{heading}\n", end="")
            print(f"{colors[1]}|  AMOUNT  |  CATEGORY  |{end_code}")
            print(f"{heading}\n", end="")
            for line in crypto_data:
                if i>0:
                    # strip removes the \n from the string
                    line = line.strip()
                    month, amount, cat = line.split(",")
                    if in_month in month:
                        print(f"{colors[4]}|   {amount}   |  {cat}  |{end_code}")
                i+=1
            print(f"{heading}\n", end="")
 
 ```
 In this piece of code we are establishing that, if option is equal to 1 then we will display the transaction of a specific month that the user wannts. We first ask for the user for the month and validate that the entry has the correct format used along the program with the function "validate_month", assigning the variable name "in_month". Then we read the data in the csv file "database.csv". Following that, we set that i is equal to 0 (helping us latter to skip the fisrt line in database.csv). To help create the lines for the chat we set heading as "-" multiplied by 24 to create the ilusion of a line. Later we use this to create a line at the top, the botton and to separate between the titles and the data. We print the tiltes in between the line that we created and then we say for every line in "crypto_data", if i is bigger than 0 (this will skip the first line in database.csv file), we will get rid of the line break with the .strip() and separe the values in month, amount and category by using the .split(","). Then, if the month entered by the user is in the month form the database we will print the category and amount for that transaction.
 
 ### Validate_category
 
  ```.py
 #Validate category is a string
 def validate_category(prompt:str)->str:
    """..."""
    end_code = "\033[00m"
    red = "\033[0;31m"
    category = input (prompt)
    category = category.lower()
    while not category.isalpha():
        category = input (f"{red}ERROR! The category must be written in letters (e.g. food).{prompt}{end_code}")
    return category
    ```

This function is validating that the input entered by the user is a string. The assigned name for the function is validate_category and it will recieve a prompt in form of a string and will return it as a string as well. Inside the function there is unicodes for the color red and to end the color so we can make the ERROR message more noticeable and obvious to the user. Then, we assign the variable name "category" to the prompt given and use a while loop to ask the program that while the what got stored in the variable "category" is not a string, show an ERROR message to the user and, at the same time, ask once agian for input form the user. Lastly, we return category as a string.

### One use of the validate_category function in the Crypto wallet

```.py
#OPTION 2: ENTER TRANSACTION
    if option == 2:

        #Asking input from the user
        category = validate_category(f"\n{underline[0]}Enter the category:{end_code} ")
        amount = validate_int_input(f"{underline[0]}Enter the amount:{end_code} ")
        month = validate_month(f"{underline[0]}Enter the month (First 3 letters of month: e.g. oct):{end_code} ")

        #Reading database.csv
        with open("database.csv", "a") as file:
            file.writelines([f"{month},{amount},{category}\n"])

        #Explaining the user that the transaction was saved
        print(f"\n{bold[1]}{emoji[3]}Transaction saved successfully!{emoji[3]}{end_code}\n")
 ```
 In this piece of code we can see the "validate_category" function as well as the "validate_int_input" and "validate_month" functions. Here, if the option is equal to two, then we will ask the user for three inputs: category, amount and month; validating with their respective validate functions. After that, we open and append in the file database.csv, adding a new line of data savinf the month, amount and category of the transaction made by the user. Laslty, implementing the good coding practices, a message letting the user know the transaction was sucessfully saved will print. This piece of code is a perfect example of why functions are so useful and important in this electronic ledger. This is because we are constanly asking for input from the user and, to make sure the program runs corrently, we need this input in the correct format. Becuase the user may make mistakes or misunderstand the instructions given, having functions that we are able to recall along the code multiple times to check the input is quite useful. This will help the program run much smoother and with less errors.
 
 ## Test Plan
  | Test No | Type of Test                                                |  Date                                                                                               | Procedure | Expected Outcome |  |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Functional: testing function validate_int_input                                         | Oct 9  | Open a file called test.py > import the function validate_int_input > ask the user for an input > print the input.         | It will print the input, which will be a number.                 |          |
| 2.      | Functional: testing function validate_choice_input  |   Oct 9 | Open a file called test2.py > import the function validate_choice_input > ask the user for an input > print the input. | It will print the input, which will be a letter. | 
| 3.      | Functional: testing function simple_login  | Oct 9 | Open a file called test3.py > import the function single_login > ask the user for an username and password > grant or deny access | Enter correct username and password will grant access, enter incorrect username and password will deny access 
| 4.      | Non-Functional: Capabilty for the user to use program efficiently　　　　　　| Oct9             | Open crypto_wallet.py > aske the user to run it for 5 minutes > see how far it gets to use it.  | The user will use at least 5 out of options  | 
|5.       | Non-Functional: Capability for the user to understand instructions of the program | Oct 9 | Open crypto_wallet.py > ask the user to run it for 5 minutes > see how many errors the user gets. | The user will get less than 3 errors.
|6.       | Non-Functional: Capability for the user to run it with out having to exit the program | Oct 9 | Open crypto_wallet.py > ask the user to run it for 5 minutes > see how many time the user exits the program innecesarily. | The user will exit innecesarily no more than one time.

