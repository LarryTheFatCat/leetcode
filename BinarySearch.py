def search(nums:list[int], target:int):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid_point = (lo + hi) // 2
        if nums[mid_point] < target:
            lo = mid_point + 1
        elif nums[mid_point] > target:
            hi = mid_point - 1
        else:
            return mid_point
    return -1

def main():
    print(search([-1,0,3,5,9,12],9))
    
if __name__ == "__main__":
    main()