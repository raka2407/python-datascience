from nba_api.stats.static import teams
import matplotlib.pyplot as plt
import pandas as pd

from nba_api.stats.endpoints import leaguegamefinder

nba_teams = teams.get_teams() # Returns a dictionary of all teams
df_teams = pd.DataFrame(nba_teams)  #Creates a Data Frame from Dictionary
df_warriors = df_teams[df_teams['nickname'] == 'Warriors'] # Returns the teams that have nickname as Warriors
df_warriors_id = df_warriors['id'].values[0] # Returns the id of warriors

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=df_warriors_id)
#print(gamefinder.get_json())
games_df = gamefinder.get_data_frames()[0] # returns the games played by the team id in dataframes

# Create 2 DFs - one which holds data that Warriors played with Raptors (TOR) at home : Other - away from home with Raptors (TOR)   
# Home Identification - GSW vs TOR
# Away Identification - GSW @ TOR

games_home = games_df[games_df['MATCHUP'] == 'GSW vs. TOR']
games_away = games_df[games_df['MATCHUP'] == 'GSW @ TOR']

games_home['PLUS_MINUS'].mean()
games_away['PLUS_MINUS'].mean() 

# Plot the PLUS_MINUS column for both DFs. We see that warriors (GSW) played better at home
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

