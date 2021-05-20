# Roll the dice

import random

while True:
    print(""" 1. Roll the dice \n 2. Exit """)
    User = int(input("Choose an opiton:"))

    if User == 1:
        no = random.randint(1,6)
        print(no)

    else:
        break

