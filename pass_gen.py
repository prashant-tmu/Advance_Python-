import random
while (10==10):
 char = "abcdefghijklmnopqrstuvwxyz)(*&^%$#@!0123456789"
 lenght = int(input("enter the lenght :"))
 password = ""
 for i in range(lenght):
    password += random.choice(char)
 print("your password is : " +password)
