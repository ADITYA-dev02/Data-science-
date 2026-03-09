import pandas as pd
import ast

df = pd.read_csv("International_T20_Data.csv")

df["teams"] = df["info.teams"].apply(ast.literal_eval)


df["pair"] = df["teams"].apply(lambda x: tuple(sorted(x)))


pair_count = df["pair"].value_counts()

print("Pair of teams who played most matches:")
print(pair_count.head(1))