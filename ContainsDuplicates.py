def containsDuplicate(nums:list[int]) -> bool:
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] == sorted_nums[i + 1]:
            return True
    return False

def main():
    print(containsDuplicate([2,14,18,22,22]))
    
if __name__ == "__main__":
    main()