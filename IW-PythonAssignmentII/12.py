def is_palindrome(str):
    if ''.join(reversed(str)) == str:
        return True
    else:
        return False


str = input('enter a word')
print(is_palindrome(str))