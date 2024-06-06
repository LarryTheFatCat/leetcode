def reverseSort(list:list[int]) -> list[int]:
    """
    Takes in list storing integer values, returns reverse order of list (unsorted, just reversed)
    
    >>> [1,2,3,4]
    4,3,2,1
    
    >>> [2,4,5,1]
    1,5,4,2
    
    """
    left = 0
    right = len(list) - 1
    
    while (left < right):
        # Swap
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
        left += 1
        right -= 1
    return list

def addTwoNumbers(l1:list[int], l2:list[int]) -> list[int]:
    """
    takes in 2 lists that store integers, returns the reverse sum order of list
    
    >>> addTwoNumbers([2,4,3],[5,6,4])
    789
    
    >>> addTwoNumbers([1,2,3],[5,6,7])
    6801
    """
    sorted_reverse_l1 = reverseSort(l1)
    sorted_reverse_l2 = reverseSort(l2)
    l1_string = ''.join(map(str,sorted_reverse_l1))
    l2_string = ''.join(map(str, sorted_reverse_l2))
    sum_of_strings = int(l1_string) + int(l2_string)
    ans = []
    for numbers in str(sum_of_strings):
        ans.append(numbers)
    return ans
        
def main():
    print(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))

if __name__ == "__main__":
    main()