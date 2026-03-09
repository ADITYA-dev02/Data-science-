import pandas as pd

df = pd.read_csv("International_T20_Data.csv")

df = df.rename(columns={
    "meta.created": "created_date",
    "meta.data_version": "data_version",
    "meta.revision": "revision",
    "info.city": "city",
    "info.venue": "venue",
    "info.match_type": "match_type",
    "info.overs": "overs",
    "info.teams": "teams",
    "info.toss.winner": "toss_winner",
    "info.toss.decision": "toss_decision",
    "info.player_of_match": "player_of_match",
    "info.outcome.winner": "match_winner"
})

print("Renamed Columns:")
print(df.columns)