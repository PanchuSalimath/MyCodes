password = input("Enter Password: ")

letters = 0
digits = 0
special = 0

for ch in password:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1
    
if letters > 0 and digits > 0 and special > 0:
    print("Password is strong")
elif letters > 0 and digits > 0:
    print("Password is medium")
else:
    print("Password is Weak")

print("Letters: ",letters)
print("Digits: ",digits)
print("Specials: ",special)