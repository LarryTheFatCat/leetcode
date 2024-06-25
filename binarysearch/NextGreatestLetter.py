def nextGreatestLetter(letters:list[str], target:str) -> str:
    """
    Returns the next character in the sequence assuming said letters list is sorted
    This also makes the assumption that there are more than 2 distinct characters
    Convert to ascii first
    """
    ascii_list = []
    for chars in letters:
        ascii_list.append(ord(chars))
    sorted_ascii_list= sorted(ascii_list)
    lo = 0
    hi = len(sorted_ascii_list) - 1
    if ord(target) >= sorted_ascii_list[-1]:
        return sorted_ascii_list[0]
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if ascii_list[mid] <= ord(target):
            lo = mid + 1
        else:
            hi = mid - 1
    
    return chr(ascii_list[lo])
    

def main():
    print(nextGreatestLetter(["c","f","j"],"c"))
    
if __name__ == "__main__":
    main()