import pandas as pd
import ast

df = pd.read_csv("International_T20_Data.csv")

df["teams"] = df["info.teams"].apply(ast.literal_eval)

df["team1"] = df["teams"].apply(lambda x: x[0])
df["team2"] = df["teams"].apply(lambda x: x[1])

matches_played = pd.concat([df["team1"], df["team2"]]).value_counts()


matches_won = df["info.outcome.winner"].value_counts()

team_stats = pd.DataFrame({
    "played": matches_played,
    "won": matches_won
}).fillna(0)


team_stats["win_percentage"] = (team_stats["won"] / team_stats["played"]) * 100

top5 = team_stats.sort_values(by="win_percentage", ascending=False).head(5)

print("Top 5 teams by win percentage:")
print(top5)