import soccerdata as sd

# Create a scraper class instance for the 2018/19 Premier League
five38 = sd.FiveThirtyEight('ENG-Premier League', '1819')

# Fetch data
games = five38.read_games()
forecasts = five38.read_forecasts()
clinches = five38.read_clinches()

print(games)
