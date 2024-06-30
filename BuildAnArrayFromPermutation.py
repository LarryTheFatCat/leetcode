def buildArray(nums:list[int]) -> list[int]:
    """
    nums[nums[1]], nums[nums[2]], nums[nums[3]]... nums[nums[n]]
    """
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans

def main():
    print(buildArray([0,2,1,5,3,4]))

if __name__ == "__main__":
    main()