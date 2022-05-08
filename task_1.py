import random
import sys

password = input("Enter your password: ")

if len(password) <= 8:
    print("Password too short.")
    sys.exit()
# it enables the programme to generate 3 different random letters and enter 3 times if it is matched in each time
for i in range(3):
    random_index = random.randint(1, len(password))
    letter = input("Enter letter at position " + str(random_index) + ": ")
    # " " concatenated to the password itself to be able to start index 1 of the password when the random_index 1
    if letter == (" " + password)[random_index]:
        print("Correct")
    else:
        sys.exit("Security check failed.")
    if i == 2:
        print("Security check passed.")
