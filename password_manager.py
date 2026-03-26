from cryptography.fernet import Fernet



'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key", "rb") # read bites rf
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)

# key + password + text to encrypt = random text 
# random text + key _ password = text to encrypt


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User:", user, " , Password:",
                  fer.decrypt(passw.encode()).decode())
            


def add():
    name = input('Account name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") # takes bytes of string and decode it to the byte string 




while True:        
    mode = input("Would you like to add a new password or view the existing ones (view, add)?, press q to quit?").lower()
    if mode == "q":
        break
    
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
