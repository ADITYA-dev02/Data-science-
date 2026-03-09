import pandas as pd
import ast

df = pd.read_csv("International_T20_Data.csv")

innings = ast.literal_eval(df.loc[0, "innings"])

def get_scorecard(innings):

    first_innings = innings[0]["1st innings"]["deliveries"]
    second_innings = innings[1]["2nd innings"]["deliveries"]

    first_list = []
    for ball in first_innings:
        for k, v in ball.items():
            first_list.append(v)

    second_list = []
    for ball in second_innings:
        for k, v in ball.items():
            second_list.append(v)

    df1 = pd.json_normalize(first_list)
    df2 = pd.json_normalize(second_list)

    top_bat1 = df1.groupby("batsman")["runs.batsman"].sum().sort_values(ascending=False).head(4)
    top_bat2 = df2.groupby("batsman")["runs.batsman"].sum().sort_values(ascending=False).head(4)

    top_bowl2 = df1.groupby("bowler")["runs.total"].sum().sort_values().head(4)
    top_bowl1 = df2.groupby("bowler")["runs.total"].sum().sort_values().head(4)

    scorecard1 = pd.concat([top_bat1, top_bowl2], axis=1)
    scorecard2 = pd.concat([top_bat2, top_bowl1], axis=1)

    return scorecard1, scorecard2


score1, score2 = get_scorecard(innings)

print("Scorecard First Innings")
print(score1)

print("\nScorecard Second Innings")
print(score2)