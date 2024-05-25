def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    defang = ""
    for numbers in address:
        if numbers == ".":
            defang += "[.]"
        else:
            defang += numbers
    return defang
def main():
    print(defangIPaddr("255.100.50.0"))
    
if __name__ == "__main__":
    main()