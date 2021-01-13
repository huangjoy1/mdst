"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    value = random.randint(1,9)
    while (1):
        guess = input("Guess a number from 1 to 9: ")
        if (guess == "exit"):
            break
        elif (int(guess) < value):
            print("your guess is too low")
        elif (int(guess) > value):
            print("your guess is too high")
        else:
            print("your guess is exactly right!")
           
           
           
           


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    for x in range(len(string) // 2):
        if (string[x] != string[len(string) - 1 - x]):
            print("false")
            return None
    print("true")
            


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    enc_user_bytes = username.encode("ascii")
    enc_user_64bytes = base64.b64encode(enc_user_bytes)
    encUsername = enc_user_64bytes.decode("ascii")



    enc_pwd_bytes = password.encode("ascii")
    enc_pwd_64bytes = base64.b64encode(enc_pwd_bytes)
    encPassword = enc_pwd_64bytes.decode("ascii")

    
    f = open(filename, "a")
    f.write(encUsername)
    f.write("\n")
    f.write(encPassword)
    f.close()

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f = open(filename, "r")
    data = f.readlines()
    
    dec_user = data[0]
    dec_pwd = data[1]

    dec_user = dec_user.encode("ascii")
    dec_user = base64.b64decode(dec_user)
    dec_user = dec_user.decode("ascii")
    print(dec_user)

    dec_pwd = dec_pwd.encode("ascii")
    dec_pwd = base64.b64decode(dec_pwd)
    dec_pwd = dec_pwd.decode("ascii")
    print(dec_pwd)

    f.close()

    if (password != None):
        print('Your password has been changed to ' + password)
        password = password.encode("ascii")
        password = base64.b64encode(password)
        password = password.decode("ascii")

        data[1] = password
        f = open(filename, "w")
        f.writelines(data)
        
        f.close()

   





if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
