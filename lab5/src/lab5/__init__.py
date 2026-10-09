import numpy as np
import pandas as pd
import math

df_students = pd.read_csv("students.csv", na_values=np.nan)
df_scores = pd.read_csv("scores.csv", na_values=np.nan)

def floor_to_two_digits(number):
    return math.floor(number*100)/100.0

def first_part(df) -> None:
    gpa = df["GPA"].values
    formatted_mean = floor_to_two_digits(np.nanmean(gpa))
    df = df.fillna({"GPA": formatted_mean})
    # print(df.head())
    # print(f"row: {df.shape[0]}, column: {df.shape[1]}")
    # print(df[["name", "GPA"]])
    # print(df[["name", "GPA"]][df["GPA"] >= 3.5])
    # print(df[["name", "GPA"]].sort_values(by="GPA", ascending=False))
    print(df.groupby("major")["GPA"].mean())

def second_part(df_st, df_sc) -> None:
    gpa = df_st["GPA"].values
    df_st = df_st.fillna({"GPA": floor_to_two_digits(np.nanmean(gpa))})

    gpa_python = df_sc["python"].values
    gpa_math = df_sc["math"].values
    gpa_database = df_sc["database"].values
    df_sc = df_sc.fillna({"python": floor_to_two_digits(np.nanmean(gpa_python))})
    df_sc = df_sc.fillna({"math": floor_to_two_digits(np.nanmean(gpa_math))})
    df_sc = df_sc.fillna({"database": floor_to_two_digits(np.nanmean(gpa_database))})

    joined_df = pd.merge(df_st, df_sc, on='student_id', how='left')

    joined_df["avg_score"] = joined_df[["python", "math", "database"]].mean(axis=1)
    print(joined_df.sort_values(by="avg_score", ascending=False).head())
    print(joined_df.groupby("major")["avg_score"].mean())
    # print(df_st)

def main() -> None:
    # first_part(df_students)
    second_part(df_students, df_scores)