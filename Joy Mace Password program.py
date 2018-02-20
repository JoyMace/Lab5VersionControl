# CSC 119-101 March 3, 2016 Joy Mace

password_out = ' '
case_changer = ord('a') - ord('A')
#change numbers to letters
number_letter = ()

# changes the letters from lowercase to uppercase and numbers to other numbers
encryption_key = (('a','m'), ('b', 'h'), ('c', 't'), ('d','f'), ('e', 'g'),
                  ('f', 'k'), ('g', 'b'), ('h', 'p'), ('i', 'j'), ('j', 'w'), ('k', 'e'), ('l', 'r'),
                  ('m', 'q'), ('n', 's'), ('o', 'l'), ('p', 'n'), ('q', 'i'), ('r', 'u'), ('s', 'o'),
                  ('t', 'x'), ('u', 'z'), ('v', 'y'), ('w', 'v'), ('x', 'd'), ('y', 'c'), ('z', 'a'),
                  ('0', '2'), ('1', '3'), ('2', '4'), ('3', '5'), ('4', '6'), ('5', '7'),
                  ('6', '8'), ('7', '9'), ('8', '0'), ('9', '1'))

#replaces every instance of the first letter with the second letter in a given password
# program greeting
print('This program will encrypt and decrypt user passwords\n')

#get selection(encrypt/decrypt)
which = input('Enter (e) to encrypt a passowrd, and (d) to decrypt: ')

while which != 'e' and which != 'd':
    which = input.("\nINVALID - Enter 'e' to encrypt, 'd' to decrypt: ")
# ensures input works with the rest of the code

encrypting = (which == 'e') #assigns True or False

#get password
password_in = input('Enter password: ')

#perform encryption / decryption
if encrypting:
    from_index = 0
    to_index = 1
#changes first letter to second letter
else:
    from_index = 1
    to_index = 0
#changes second letter back to first letter
case_changer = ord('a') - ord('A')
                                             
#code to deal with letters (works)
for ch in password_in:
    letter_found = False

    for t in encryption_key:
        if ('a' <=ch and ch <= 'z') and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True
#changes uppercase to lowercase for comparison and changes to_letter to uppercase
        elif ('A' <= ch and ch <= 'z') and chr(ord(ch) + 32) == t[from_index]:
            password_out = password_out + chr(ord(t[to_index]) - case_changer)
            letter_found = True
#code to deal with numbers
        elif ('0' <=ch and ch <='9') and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True
            
    if not letter_found:
        password_out = password_out + ch

#output
if encrypting:
    print('Your encrypted password is:', password_out)
else:
    print('Your decrypted password is:', password_out)
