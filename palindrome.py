def is_palindrome(s):
    return s==s[::-1]
    pass
s="malayalam"
ans=is_palindrome(s)
if ans:
    print("yes")
else:
    print("no")


