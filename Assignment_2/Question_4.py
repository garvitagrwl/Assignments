s_name = input("Enter the student's name:")
s_class = int(input("Enter the class of the student(In decimal): "))
print('''
Subject 1 - Mathematics
Subject 2 - Science
Subject 3 - Social Studies
Subject 4 - English
Subject 5 - Hindi
''')

s_sub = [0]* 5
for i in range(5):
    s_sub[i] = int(input(f"Enter the marks for subject {i+1}: "))

s_sum = 0

for i in range(5):
    s_sum = s_sum + s_sub[i]
total_marks = s_sum
per = float(f"{total_marks/5:.2f}")
print(per)
percentage = f"{per}%"
print("------------------------\n\n\n")
print(f"Student Details:\nStudent Name:{s_name}\nStudent Class:{s_class}\nStudent Percentage:{percentage}")
if per > 60.00:
    print("Grade A")
elif per > 50.00:
    print("Grade B")
elif per > 40.00:
    print("Grade C")
else:
    print("Fail")
