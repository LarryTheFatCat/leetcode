def arrayRankTransform(arr:list[int]) -> list[int]:
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    sorted_list = sorted(arr)
    ranked_array = []
    rank = 1
    rank_array = []
    
    for i in range(len(sorted_list)):
        if i == 0 or sorted_list[i] != sorted_list[i - 1]:  # Increment rank for new unique numbers
            rank_array.append(rank)
            rank += 1
        else:
            rank_array.append(rank_array[-1])  # Same rank for duplicates
    for unsorted_num in arr:
        for i in range(len(sorted_list)):
            if sorted_list[i] == unsorted_num:
                ranked_array.append(rank_array[i])
                break 

    return ranked_array
def main():
    print(arrayRankTransform([37,12,28,9,100,56,80,5,12]))
    
if __name__ == "__main__": main()