def lengthOfLastWord(s:str) -> int:
    """
    Iterates through string, returns length of last word
    
    >>> lengthOfLastWord("Hello World")
    5
    
    >>> lengthOfLastWord("John Paul")
    4
    """
    current_string = s.split()
    return len(current_string[-1])
    


def main():
    print(lengthOfLastWord("luffy is still joyboy"))
    
if __name__ == "__main__":
    main()