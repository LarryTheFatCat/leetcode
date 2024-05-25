def numberOfEmployeesWhoMetTarget(hours, target):
    """
    :type hours: List[int]
    :type target: int
    :rtype: int
    """
    counter = 0
    for i in range(len(hours)):
        if hours[i] >= target:
            counter += 1
    return counter
def main():
    print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
    
if __name__ == "__main__":
    main()