abcs = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N':13, 'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17, 'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22, 'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25}

def alphabet_position(letter):
    abcs = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N':13, 'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17, 'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22, 'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25}
    return abcs.get(letter) 
    

def rotate_character(char, rot):
    if char.islower(): #if char is lower, shift_pos starts at 97
        shift_pos = 97 
    elif char.isupper():#if char is upper, shift_pos starts at 65
        shift_pos = 65 
    else:
        return char 
    letter = alphabet_position(char) #can't figure out how to fit this in
    add_char_to_rot_shift_mod_shift = chr((ord(char) + rot - shift_pos) % 26 + shift_pos)
    return add_char_to_rot_shift_mod_shift