from helpers import alphabet_position, rotate_character

def encrypt(text, text_key):
    abcs = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N':13, 'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17, 'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22, 'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25}
    encryption = [] # initialize an accumulator list    
    starting_index = 0 #starting index for rotation
    for letter in text:# create a for loop to iterate through text_key
        rotation = alphabet_position(text_key[starting_index])
        if letter.isspace():
            encryption.append(letter)
        elif not letter in abcs: #need help with skipping spaces
            encryption.append(letter)
        else:             
            encryption.append(rotate_character(letter, rotation))  
            starting_index += 1
     
        if starting_index > (len(text_key) - 1): 
            starting_index = 0
      
    return ''.join(encryption) 
 
def main():
    user_message = input(str("Type a message:"))
    user_rotation = input("Encryption key: ")
    print(encrypt(user_message, (user_rotation)))

if __name__ == "__main__":
    main()