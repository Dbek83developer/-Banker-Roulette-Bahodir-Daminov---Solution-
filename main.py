import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
index = len(names) -1

index_random = random.randint(0, index)
print(f"{names[index_random]} is going to buy the meal today!")



