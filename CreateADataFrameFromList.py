import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns=["student_id","age"])
    
def main():
    print(createDataframe([[1,15],[2,11],[3,11],[4,20]]))
    
if __name__ == "__main__":
    main()