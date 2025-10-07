import random #imports a code module that helps you randomize numbers. This is so you don't have to write complicated code for randomising things yourself.

#creating a variable called random_int to store the outcome of the "coin flip". 1 is heads and 0 is tails. This will let me create an if statement where I can give each number their respective name.
random_int = random.randint(0, 1)

if random_int == 1:
    print("Heads")
else:
    print("Tails")