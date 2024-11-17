#ENCRYPTION CODE
alphabet = "abcdefghijklmnopqrstuvwxyz"
new_message = ""

user_message = input("Enter your secret message: ").lower()
key = int(input("Enter a key (1 through 26): "))
#print(user_input)

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character

    else:
        new_message += character
print("Your secret message is " + new_message)

#DECRYPTION CODE
alphabet = "abcdefghijklmnopqrstuvwxyz"
new_message = ""

user_message = input("Enter your secret message: ").lower()
key = int(input("Enter a key (1 through 26): "))
#print(user_input)

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position - key) % 26
        new_character = alphabet[new_position]
        new_message += new_character

    else:
        new_message += character
print("Your secret message is " + new_message)

# I know I can define a function to improve the
# code and reduce the repetition, but each time I
# tried, the code nevr ran through all the input 
# prompts. Only the initial input prompt would work. 
# Any advice on how to get started with moving this 
# into a function would be much apprecaited!
