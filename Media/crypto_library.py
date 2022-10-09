def autor()->str:
    return '''Maria Daniela Arias Camargo
UWC ISAK student, G11
Class of 2024
'''

def validate_int_input(prompt:str)->int:
    end_code = "\033[00m"
    red = "\033[0;31m"
    num = input (prompt)
    while not num.isdigit():
        num = input (f"{red}ERROR! Enter a number (e.g. 4).\n{prompt}{end_code}")

    return int(num)

def validate_choice_input(prompt:str)->str:
    end_code = "\033[00m"
    red = "\033[0;31m"
    letter = input(prompt)
    letter = letter.lower()
    while not letter in ["a","b","c","d"]:
        letter = input (f"{red}ERROR! Enter a letter (e.g. a).{prompt}{end_code}\n")

    return letter

def validate_month(prompt:str)->str:
    """..."""
    end_code = "\033[00m"
    red = "\033[0;31m"
    month = input(prompt)
    month = month.lower()
    while not month in ["jan", "feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]:
        month = input (f"{red}ERROR! The month must be written with the first 3 letters of the month (e.g oct).{prompt}{end_code}\n")

    return month


def simple_login(user:str, password:str)->str:
    '''
    Simple authentication, needs file users.csv
    :param user: string
    :param password: string
    :return: string
    '''
    colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;34m"]
    end_code = "\033[00m"
    with open("crypto_password.cvs") as file:
        database = file.readlines()
    output = ""
    for line in database:
        line_cleaned = line.strip() #remove backslash n
        user_pass= line_cleaned.split(",")
        if user == user_pass [0] and password == user_pass[1]:
            output = f"{colors[3]}ACCESS GRANTED! Welcome back Ms. Sato{end_code}\n"
        else:
            output = quit(f"{colors[1]}INCORRECT PASSWORD! Try again.{end_code}")
            break

    return output

def validate_category(prompt:str)->str:
    """..."""
    end_code = "\033[00m"
    red = "\033[0;31m"
    category = input (prompt)
    category = category.lower()
    while not category.isalpha():
        category = input (f"{red}ERROR! The category must be written in letters (e.g. food).{prompt}{end_code}")
    return category




