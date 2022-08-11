import random
import string

# acceptable characters for the password
characters = string.ascii_lowercase + string.ascii_uppercase + "0123456789" + "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
# the length of the variable 'characters'
char_num = len(characters)
# a placeholder for the password
password = str()

length = input("Enter the number of characters for your password: ")

# adding random characters multiple times based on the user's input
for i in range(int(length)):
    password += characters[random.randint(0, (char_num - 1))]

# saving the generated password in a new file
with open("password.txt", "w") as file:
    file.write(password)

print(f"Your password: {password}\nSuccessfully saved in password.txt")