def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    #fullname = input("What is your full name?")
    name_as_a_list = fullname.split()
    initials = ""
    for item in name_as_a_list:
        initials = initials + item[0]
    initials = initials.upper()
    return initials

def main():
    fullname = input("What is your full name?")
    print(get_initials(fullname))

if __name__ == '__main__':
    main()
