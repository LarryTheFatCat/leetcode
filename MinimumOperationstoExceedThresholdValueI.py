def minOperations(nums:list[int], k:int) -> int:
    counter = 0
    for i in range(len(nums) - 1):
        if nums[i] < k:
            counter += 1
    return counter

def main():
    print(minOperations([1,1,2,4,9], 1))
    
if __name__ == "__main__":
    main()