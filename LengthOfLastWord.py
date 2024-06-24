def lengthOfLastWord(s:str) -> int:
    """
    :type s: str
    :rtype: int
    """
    split_string = s.split()
    for words in range(len(split_string)):
        return len(split_string[words - 1])
        

def main():
    print(lengthOfLastWord("   fly me   to   the moon  "))

if __name__ == "__main__":
    main()
    