def reverseSort(list:list[int]) -> list[int]:
    left = 0
    right = 0
    for numbers in list:
        if numbers.isdigit():
            right += 1
    
    while (left < right):
        # Swap
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
        left += 1
        right -= 1
    return list

def addTwoNumbers(l1, l2):
    # reverse sort algorithm
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