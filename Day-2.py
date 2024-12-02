#Question:
# Function to find the nth highest salary
# Return None if nth highest salary does not exist
# Return result as a Pandas DataFrame with dynamic column name

import pandas as pd


def nth_highest_salary(df, n):
    # Drop duplicates, sort salaries in descending order, and reset index
    sorted_salaries = df['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    
    # Check if n is within the range of available salaries
    if n <= len(sorted_salaries):
        result = sorted_salaries.iloc[n-1]
    else:
        result = None  
    
    column_name = f'getNthHighestSalary({n})'
    return pd.DataFrame({column_name: [result]})
