
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

LastName2=random.choice(names)
namesList=len(names)

name=random.randint(0,namesList-1)

LastName=names[name]
print(f"{LastName2} is going to buy the meal today!")