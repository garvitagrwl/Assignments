def is_palindrome(number):
    original = str(number)
    reverse = original[::-1]
    if original == reverse:
        return True
    else:
        return False


num = int(input("Enter a number to check if it’s a palindrome: "))

if is_palindrome(num):
    print(f"{num} is a Palindrome Number")
else:
    print(f"{num} is NOT a Palindrome Number")
