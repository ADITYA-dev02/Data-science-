import pandas as pd

df = pd.read_csv("International_T20_Data.csv")

df = df.rename(columns={"info.venue": "venue"})

top_venues = df["venue"].value_counts().head(3)

print("Top 3 venues with most matches:")
print(top_venues)