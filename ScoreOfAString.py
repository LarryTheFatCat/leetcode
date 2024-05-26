def scoreOfString(s:str) -> int:
    ascii_values = []
    for letters in s:
        ascii_values.append(ord(letters))
    
    current_value = []
    for i in range(len(ascii_values) - 1):
        current_value.append(abs(ascii_values[i] - ascii_values[i + 1]))
    return sum(current_value)
            

def main():
    print(scoreOfString("zaz"))
    
if __name__ == "__main__":
    main()