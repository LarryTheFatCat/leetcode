def searchInsert(nums:list[int], target:int) -> int:
    lo = 0
    hi = len(nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            return mid
    return lo
    
        
            
    
    
def main():
    print(searchInsert([1,3,5,6],7))
    
if __name__ == "__main__":
    main()