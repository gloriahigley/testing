from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    new_message = "" #initialize a new string
    for char in text: #for loop to iterate through characters
        new_message = new_message + rotate_character(char,rot) #new message equals each characters as it rotates
    return new_message

def main():
    user_message = input(str("Type a message:"))
    user_rotation = input("Rotate by: ")
    print(encrypt(user_message, (int(user_rotation))))
    
if __name__ == "__main__":
    main()
    