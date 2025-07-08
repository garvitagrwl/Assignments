name = input("Enter student name: ")
class_name = input("Enter class: ")


marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print(f"\nStudent Name: {name}")
print(f"Class: {class_name}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
