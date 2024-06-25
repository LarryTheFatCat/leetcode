def countNegatives(grid:list[list[int]]) -> int:
    negative_nums = []
    for numbers in grid:
        for nums in numbers:
            if nums < 0:
                negative_nums.append(nums)
    return len(negative_nums)

def main():
    print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    
if __name__ == "__main__":
    main()

