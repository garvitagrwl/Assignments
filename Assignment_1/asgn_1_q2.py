str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

str3 = str1 + str2

print("\nConcatenated String is:", str3)


print("\n--- String Methods ---")
print("Uppercase:", str3.upper())
print("Lowercase:", str3.lower())
print("Capitalize:", str3.capitalize())
print("Swapcase:", str3.swapcase())
print("Length of string:", len(str3))
print("Is the string starting with 'A'", str3.startswith('A'))
print("Count of 'l':", str3.count('l'))

