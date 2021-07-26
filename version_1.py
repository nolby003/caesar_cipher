#
# Author: Benjamin Nolan
# Date: 28/10/2018, Modified as corrected 17/11/2018
# Description: Caesar Cipher in Python
# Encrypt a string, decrypt a string and brute force decrypt
# ASCII range: ordinals 32 to 127
#

def display_details():
    print('Author: Benjamin Nolan')
    
display_details()

option = ''

# display menu
def get_menu_choice():
    
    print('\n*** Menu ***\n')
    print('1. Encrypt string')
    print('2. Decrypt string')
    print('3. Brute force decryption')
    print('4. Quit\n')

    # user input menu option
    option = int(input('What would you like to do [1,2,3,4]? '))

    # validate - only options 1,2,3 and 4 can be entered    
    while option not in range(1,5):
        print('Invalid choice, please enter either 1, 2, 3 or 4.\n')
        option = int(input('What would you like to do [1,2,3,4]? '))
    if option == 1:
        #call enrypt function
        encode()
    elif option == 2:
        #call derypt function
        decode()
    elif option == 3:
        #call brute force decryption function
        brute()
    elif option == 4:
        #abort function    
        abort()

# offset
def get_offset():
    offset_opt = int(input('Please enter offset value (1 to 94): '))
    while offset_opt not in range(1,95):
        offset_opt = int(input('Please enter offset value (1 to 94): '))
    return offset_opt

# encrypt message    
def encode():
            
    # get user input for message to encrypt (string)
    val = str(input('\nPlease enter string to encrypt: '))

    # fetch user input for shift offset from get_offset() function
    offset = get_offset()

    print('\nEncrypted string:')

    # set variables    
    total_enc = ''
    uc_string = ''

    # loop through each character found in string to encrypt
    for char in val:

        # get unicode integer from each character of string
        uc_string = ord(char)

        # set shift variable to calculate unicode integer plus offset chosen by user
        uc_string = (uc_string + offset)

        # is ord from string less than 32, yes, add 94
        # Modified as corrected 17/11/2018, changed value from 94 to 95
        while uc_string < 32:
            uc_string += 95
                
        # is ord from string greater than 126, yes, minus 94
        # Modified as corrected 17/11/2018, changed value from 94 to 95
        while uc_string > 126:
            uc_string -= 95   

        # append all new unicode characters encrypted from original message
        total_enc += chr(uc_string)

    # display to screen the encrypted message result
    print(total_enc)

    # recall menu
    get_menu_choice()


# decrypt message
def decode():
    
    # get user input for message to decrypt (string)
    val = str(input('\nPlease enter string to decrypt: '))
        
    # fetch user input for shift offset from get_offset() function
    offset = get_offset()

    print('\nDecrypted string:')

    # set variables
    total_dec = ''
    uc_string = ''

    # loop through each character found in string to decrypt
    for char in val:

        # get unicode integer from each character of string
        uc_string = ord(char)

        # set shift variable to calculate unicode integer minus offset chosen by user
        uc_string = (uc_string - offset)

        # is ord from string less than 32, yes, add 94 
        while uc_string < 32:
            # Modified as corrected 17/11/2018, changed value from 94 to 95
            uc_string += 95

        # is ord from string greater than 126, yes, minus 94
        while uc_string > 126:
            # Modified as corrected 17/11/2018, changed value from 94 to 95
            uc_string -= 95   

        # append all new unicode characters decrypted from original message
        total_dec += chr(uc_string)

    # display to screen the encrypted message result
    print(total_dec)

    # recall menu
    get_menu_choice()


# Bruce force decryption 
def brute():
    # get user input for message to decrypt (string)
    val = input('\nPlease enter string to decrypt: ')

    # set offset value to zero ready for loop
    offset = 0

    # loop until loop ends at 94th loop
    for offset in range(1,95):

        # set variables
        total_dec = ''
        uc_string = ''

        # loop through each character found in string to encrypt
        for char in val:

            # get unicode integer from each character of string
            uc_string = ord(char)

            # set shift variable to calculate unicode integer minus offset in each loop
            uc_string = (uc_string - offset)

            while uc_string < 32:
                # Modified as corrected 17/11/2018, changed value from 94 to 95
                uc_string += 95

            while uc_string > 126:
                # Modified as corrected 17/11/2018, changed value from 94 to 95
                uc_string -= 95   

            # append all new unicode characters encrypted from original message
            total_dec += chr(uc_string)

        # display to screen decrypted messages from offset 1 through to 94
        print('Offset:',offset,'= Decrypted string:',total_dec)

    # recall menu
    get_menu_choice()
            
# quit program 
def abort():

    print('Goodbye.')

if option not in range(1,5):
    get_menu_choice()
    
#EOF

   
