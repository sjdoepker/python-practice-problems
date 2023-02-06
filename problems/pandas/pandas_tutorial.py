import pandas as pd
import numpy as np

# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.

## YOUR CODE HERE ##
morg_df = pd.read_csv("/home/sjdoepker/cmsc14200-win-2023/python-practice-problems/problems/pandas/morg_d07_strings.csv")
morg_df.index = morg_df['h_id']

# TASKS 2-6
# For each of the tasks, print the value requested in the task.

## YOUR CODE HERE ##
print(morg_df['age'])

print(morg_df.loc[morg_df['h_id'] == '1_2_2'])

print(morg_df.iloc[:3])

na_map = {}
for col in morg_df.columns:
    if any(morg_df.loc[col].isna()):
        na_map[col] = 0 
print(na_map)

morg_df.fillna(value=na_map)

### Task 7
### convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]

## YOUR CODE HERE ##

for col in TO_CATEGORICALS:
    morg_df.loc[col] = morg_df.loc[col].astype("category")

# Example use of cut()
boundaries = range(16, 89, 8)
morg_df.loc[:, "age_bin"] = pd.cut(morg_df.loc["age"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

### Task 8

## YOUR CODE HERE ##
hwpw_bounds = range(0,99,9)
morg_df["hwpw_bin"] = pd.cut(morg_df['hours_worked_per_week'], 
                           bins=hwpw_bounds,
                           labels=range(len(hwpw_bounds)-1),
                           include_lowest=True, right=True)

print("Morg columns types after Task 8")
print(morg_df.dtypes)


### Tasks 9-13
full_time_df = morg_df[morg_df['hours_worked_per_week'] >= 35]

unemployed_df = morg_df[morg_df['employment_status'] != "Working"]

full_time_rich_df = morg_df[(morg_df['hours_worked_per_week'] >= 35) | (morg_df['earnings_per_week'] > 1000)]

race_df_val_counts = morg_df.value_counts()
print(race_df_val_counts[:5])

race_df_group = morg_df.groupby('race').size()
### Task 14

students = pd.read_csv("/home/sjdoepker/cmsc14200-win-2023/python-practice-problems/problems/pandas/students.csv")
extended_grades = pd.read_csv("/home/sjdoepker/cmsc14200-win-2023/python-practice-problems/problems/pandas/extended_grades.csv")

roster = pd.merge(students, extended_grades, on="UCID", how="inner")