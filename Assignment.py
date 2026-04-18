# UNIT :- 1

#1 Calculating momentum

m=float(input())
v=float(input())
p=m*v
print(f"{p:.2f}kgm/s")

#2 Use of if-else

n=int(input())

if(n<10 and n>=0):
	print(n**2)
elif(n<100 and n>=10):
	print(f"{n**0.5:.2f}")
elif(n<1000 and n>=100):
	print(f"{n**(1/3):.2f}")
else:
	print("Invalid")

#3 Calculating salary in usd and age using functions

from datetime import datetime

# Input dates
date1 = input()
date2 = input()

# Convert string to date format
d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

# Calculate difference
difference = (d2 - d1).days

# Output number of days
print(difference)

#4 Reversing the string

number=int(input())
reverse_number=int(str(number)[::-1])
print(f"{reverse_number}")

#5 Printing table 

n=int(input())
for i in range (1,11):
	print(n,"x",i,"=",n*i)


# UNIT:- 2

# List operatores with even driven menu :- 

l1=[]
while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	n =int(input("Enter choice: "))
	if n==1:
		add=int(input("Integer: "))
		l1.append(add)
		print(f"List after adding: {l1}")
	elif n==2:
		if len(l1)==0:
			print("List is empty")
		elif len(l1)!=0:
			remove=int(input("Integer: "))
			if remove not in l1 :
				print("Element not found")
			else:
				l1.remove(remove)
				print(f"List after removing: {l1}")
	elif n==3:
		if len(l1)==0:
			print("List is empty")
		else:
			print(l1)
	elif n==4:
		break
	else:
		print("Invalid choice")

# 2 Dictionary operations :-

print("Original Dictionary:",student)


# -------- Insertion --------
key_insert = int(input())
value_insert = input()
student[key_insert] = value_insert

print("After Insertion:",student)

# -------- Update --------
key_update = int(input())
value_update = input()
if key_update in student:
    student.update( {key_update: value_update})

print("After Update:",student)


# -------- Deletion --------
key_delete = int(input())
if key_delete in student:
    student.pop(key_delete)

print("After Deletion:",student)


# -------- Traversal --------
print("Traversing Dictionary:")
for key, value in student.items():
    print(f"{key} : {value}")


# UNIT :- 5

# Stacked plot :- 

import matplotlib.pyplot as plt
import pandas as pd

# Data for Months and Temperature for three cities
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'City_A_Temperature': [5, 7, 10, 13, 17, 20, 22, 21, 18, 12, 8, 6],
    'City_B_Temperature': [2, 3, 5, 6, 10, 14, 16, 17, 12, 9, 5, 3],
    'City_C_Temperature': [3, 4, 6, 8, 9, 12, 15, 14, 10, 7, 4, 2]
}

# Write your code...

df = pd.DataFrame(data)

plt.stackplot(df['Month'],df['City_A_Temperature'],df['City_B_Temperature'],df['City_C_Temperature'])

plt.xlabel('Month')
plt.ylabel('Temperature')
plt.title('Temperature Variation')
#plt.legend(loc='upper left')
plt.show() 