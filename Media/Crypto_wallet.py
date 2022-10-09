#Importing functions from crypto_library
from crypto_library import validate_int_input, autor, simple_login, validate_month, validate_category, validate_choice_input

#Adding colors
colors =  ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;34m", "\33[0;33m","\33[0;35m","\33[0;35m"]
bold = ["\33[1;37m","\33[1;32m","\33[1;31m"]
underline = ["\33[4;37m","\33[4;36m","\33[4;32m","\33[4;31m","\33[4;34m","\33[4;31m	","\33[45m"]
background = ["\33[43m","\33[46m","\33[42m","\33[41m","\33[40m"]
end_code = "\033[00m"
#Adding emojis
emoji = ["\U0001F911","\U0001FAE1","\U0001F609","\U00002705"]

#Printing welcome message for the user
intro_msg = f"{colors[3]} {emoji[0]}Welcome to Crypto Wallet!{emoji[0]} {end_code}"
print(intro_msg.center(50, "-"))

#Asking user for username and password
username = input(f"{colors[4]}{background[4]}Please enter your username:{end_code} {end_code}")
password = input(f"{colors[4]}{background[4]}Please enter your password:{end_code} {end_code}")

#Calling function to check username and password
out = simple_login(user=username,password=password)
print(f"{out}{emoji[1]}")

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

    #OPTION 1: I WANT TO LEARN MORE ABOUT CARDANO
    if option == 1:
    #Printing menu of options for the user
        menu_2 = f"""{colors[6]}A. What is Cardano?
B. What is Cardano's goal?
C. When was Cardano created and by who?
D. Value of Cardano as of Sunday, Oct 2, 2022
{end_code}"""
        print(f"\n{background[4]}{'Options'.center(50)}{end_code}")
        print(menu_2)

        # validating user's input calling the function validate_int_input from crypto_library
        option = validate_choice_input("Please enter an option [A-D]:　")
        while not option in ["a", "b", "c", "d"]:
            option = validate_choice_input(f"{colors[1]}{option} is incorrect. Please enter an option [A-B]: {end_code}")

            # Reading Cardano_info.cvs file
        with open("Cardano_info.cvs", "r") as file:
            crypto_data = file.readlines()
            info_output = ""

        # Options to learn more about Cardano
        if option == "a":
            info_output = (f"\n{colors[3]}{crypto_data[0]}{crypto_data[1]}{crypto_data[2]}{end_code}")
        elif option == "b":
            info_output = (f"\n{colors[3]}{crypto_data[3]}{crypto_data[4]}{crypto_data[5]}{end_code}")
        elif option == "c":
            info_output = (f"\n{colors[3]}{crypto_data[6]}{end_code}")
        else:
            info_output = (f"\n{colors[3]}{crypto_data[7]}{end_code}")

        print(info_output)


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

    #OPTION 3: WITHDRAW TRANSACTION
    if option == 3:

        # Asking input from the user
        category = input(f"\n{underline[0]}Enter the category:{end_code} ")
        amount = validate_int_input(f"{underline[0]}Enter the amount:{end_code} ")
        month = validate_month(f"{underline[0]}Enter the month (First 3 letters of month: e.g. Oct):{end_code} ")

        #Reading database.csv
        with open("database.csv", "a") as file:
            file.writelines([f"{month},{-abs(amount)},{category}\n"])

        #Explaining the user that the transaction was withdrawn
        print(f"\n{bold[1]}{emoji[3]}Transaction withdrawn successfully!{emoji[3]}{end_code}\n")

    #OPTION 4: MY PAST TRANSACTIONS
    if option == 4:
        # Reading database.csv file
        with open("database.csv", "r") as file:
            crypto_data = file.readlines()
        border = "-"*30
        print(border)
        print(f"{colors[4]}| MONTH | AMOUNT | CATEGORY |{end_code}")
        print(border)
        i = 0
        for line in crypto_data:
            if i > 0:
                # strip removes the \n from the string
                line = line.strip()
                all_data = line.split(",")
                print(f"{colors[3]}|  {all_data[0]}  |   {all_data[1]}  |  {all_data[2]} |{end_code}")
            i += 1
        print(border)

    #OPTION 5: STATISTICS
    if option == 5:
        # Printing menu of options for the user
        menu = f"""{colors[6]}1. Transactions by month
2. Mean balance as of last transaction.
{end_code}"""
        print(f"\n{background[4]}{'Options'.center(50)}{end_code}")
        print(menu)

        # validating user's input calling the function validate_int_input from crypto_library
        option = validate_int_input("Please enter an option [1-2]: "+"\n")
        while option > 2 or option < 1:
            option = validate_int_input(f"{colors[1]}{option} is incorrect. Please enter an option [1-2]: {end_code}")

        #OPTION 1: TRANSACTION BY MONTH
        if option == 1:
            #Asking input from user and validating with function validate_month
            in_month = validate_month("Enter the month you would like to see the transactions from (First 3 letters of month: e.g. Oct): ")
            with open("database.csv", "r") as file:
                crypto_data = file.readlines()
            i=0
            sum_mon=0
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

        #OPTION 2: CURRENT MEAN BALANCE AS OF LAST TRANSACTION
        if option == 2:
            # Reading database.csv file
            with open("database.csv", "r") as file:
                crypto_data = file.readlines()
            i = 0
            sum = 0
            counter = 0
            for line in crypto_data:
                if i > 0:
                    line_striped = line.strip()
                    line_changed = line_striped.split(",")
                    value = line_changed[1]
                    value = int(value)
                    sum = sum + value
                    mean = sum/i
                i += 1

            print(f"{colors[1]}Your mean balance as of the las transaction is {end_code}{bold[2]}{mean}{end_code}{colors[1]} Cardano coins.{end_code}\n")


    #OPTION 6: CURRENT BALANCE
    if option == 6:
        # Reading database.csv file
        with open("database.csv", "r") as file:
            crypto_data = file.readlines()
        i =  0
        sum = 0
        for line in crypto_data:
            if i > 0:
                line_striped = line.strip()
                line_changed = line_striped.split(",")
                value = line_changed[1]
                value = int(value)
                sum = sum + value
            i += 1

        print(f"{colors[1]}Your current balance is {end_code}{bold[2]}{sum}{end_code}{colors[1]} Cardano coins.{end_code}\n")

    #OPTION 7: MORE ABOUT AUTHOR
    if option == 7:
            print(f"{colors[1]}{autor()}{end_code}\n")

#OPTION 8: EXIT
exit(f"{emoji[2]}Thank you for using Crypto Wallet!{emoji[2]}")









