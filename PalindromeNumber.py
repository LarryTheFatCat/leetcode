def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    string_value = str(x)
    if string_value == string_value[::-1]:
        return True
    else:
        return False
    
def main():
    print(isPalindrome(121))
    
if __name__ == "__main__":
    main()