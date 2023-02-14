
def is_palindrome(x):

    return x == x[::-1]

    

if __name__ == "__main__":
    
    assert is_palindrome("radar") == True
    assert is_palindrome("not") == False