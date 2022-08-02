import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o" "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    ]
symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "~", "`", "|", "}", "{", "]", "[", ":", "<", ">", "/", "?"
]

howmanyYN = int(input("How many passwords? "))
length = int(input("Length of password: "))
lettersYN = input("Include Letters? (y/n): ").lower()
numbersYN = input("Include Numbers? (y/n): ").lower()
symbolsYN = input("Include Symbols? (y/n): ").lower()

password = ""
passwordLength = 0
passwordnum = 0
passwordlist = ""

while passwordnum < howmanyYN:
    while passwordLength < length:
        if lettersYN == "y":
            password += random.choice(letters)
            passwordLength += 1
        if numbersYN == "y":
            password += str(random.choice(numbers))
            passwordLength += 1
        if symbolsYN == "y":
            password += random.choice(symbols)
            passwordLength += 1
    passwordnum += 1
    passwordlist += password + "\n"
    password = ""
    passwordLength = 0

print(passwordlist)

savefileYN = input("Save to file? (y/n): ").lower()
if savefileYN == "y":
    filename = input("Filename? ")
    if ".txt" not in filename: filename += ".txt"
    with open(filename, "w") as f:
        f.write(passwordlist)
    print("Saved to file: " + filename)