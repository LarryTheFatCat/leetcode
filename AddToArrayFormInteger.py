def addToArrayForm(num:list[int], k:int) -> list[int]:
    num_int = int("".join(map(str,num)))
    sum_num = num_int + k
    new_list = []
    for numbers in str(sum_num):
        new_list.append(int(numbers))
    return new_list
    
def main():
    print(addToArrayForm([1,2,0,0],34))
    
if __name__ == "__main__":
    main()