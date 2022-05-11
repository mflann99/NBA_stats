import pandas as pd
import numpy as np

def per_game(x,gp):
    return x/gp

def eff_fga(fgm,fg3m,fga):
    num = fgm + (0.5*fg3m)
    den = fga
    return num/den

def ts_pct(pts,fga,fta):
    den = 2 * (fga + (0.475*fta))
    return pts/den

def ft_rate(fta,fga):
    return fta/fga

def holl_ar(ast,fga,fta,tov):
    den = fga + (0.475*fta) + ast + tov
    return ast/den

def tov_pct(ast,fga,fta,tov):
    den = fga + (0.475*fta) + ast + tov
    return tov/den
