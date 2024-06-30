def plusOne(digits:list[int]) -> list[int]:
    digits_string = "".join(map(str,digits))
    new_digits_list = []
    new_digits = int(digits_string) + 1
    for numbers in str(new_digits):
        new_digits_list.append(int(numbers))
    return new_digits_list
    
def main():
    print(plusOne([9]))
    
if __name__ == "__main__":
    main()