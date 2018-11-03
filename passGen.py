#! Generating passwords with set length
import random

def passGen (length = 10):
    if length <= 0:
        return
    letters = [chr(ch) for ch in range(97,123)]
    password = letters[random.randrange(0,26)]
    for _ in range(length):
       if random.randint(0,1) == 0:
           l = letters[random.randrange(0,26)]
           password += l if random.randint(0,1) == 0 else l.upper()
       else:
            password += str(random.randrange(0,10))
    return password

if __name__ == "__main__":
    passSheet = open("passwords.txt", "w")
    print("Generating 50 passwords (width lenght of 10) to the passwords.txt")
    passSheet.write(passGen())
    for i in range(59):
        passSheet.write("\n" + passGen())
    passSheet.close()