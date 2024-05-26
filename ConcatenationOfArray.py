def getConcatenation(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[i])
    for i in range(len(nums)):
        ans.append(nums[i])
    return ans
def main():
    print(getConcatenation([1,2,1]))
    
if __name__ == "__main__":
    main()