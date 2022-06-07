import pandas as pd
import sys,os
 
def main():
    df = pd.read_csv("data/sleep_data.csv")
    print(df)
    
main()