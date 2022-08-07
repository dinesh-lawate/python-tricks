# Check if string is palindrome or not
name = input('Enter a string: ')
isPalindrome = name.find(name[::-1]) == 0
print(isPalindrome)
