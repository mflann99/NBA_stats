import pandas as pd
import numpy as np
from nba_api.stats import endpoints

#Used to compile all necessary data into one dataframe
def mvp_data(pl,start,end):
    data = pd.DataFrame()
    for i in range(start,end):
        stats =  endpoints.leagueleaders.LeagueLeaders(season=pl["year"][i]).get_data_frames()[0]
        stats = stats[stats["PLAYER"]==pl["name"][i]]
        if(i==0):
            data=stats
        else:
            data = pd.concat([data,stats])

    return data

#Makes a dataframe of stats for each team each year
def team_data(ids):
    data = pd.DataFrame()
    for id in ids:
        team =  endpoints.teamyearbyyearstats.TeamYearByYearStats(team_id=id).get_data_frames()[0]
        data = pd.concat([data,team])
    return data
