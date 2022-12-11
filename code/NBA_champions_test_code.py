## LIBRARY IMPORTS ##
import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import numpy as np

import plotly as ply
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from PIL import Image
import datetime

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt
# import seaborn as sns
# import dash as dash
# from dash import dash_table
# from dash import dcc
# from dash import html
# from dash.dependencies import Input, Output
# from dash.exceptions import PreventUpdate
# import dash_bootstrap_components as dbc

# import scipy.stats as stats
# import statistics


## DIRECTORY CONFIGURATION ##
abs_path = r'https://raw.githubusercontent.com/nehat312/winning-composition/main'
players_path = abs_path + '/data/NBA_champs_python.csv'
# team_path = abs_path + '/data/NBA_champs_python.csv'

## DATA IMPORT ##
champion_players = pd.read_csv(players_path, index_col='YR_TM_PLR', header=0)
# champion_teams = pd.read_csv(players_path, header=0, index_col='YR_TM_PLR')

## PRE-PROCESSING ##
# players_path.sort_values(by='disc_year', inplace=True)

# ## TIME INTERVALS ##
# today = datetime.date.today()
# before = today - datetime.timedelta(days=1095) #700
# start_date = '2000-01-01'
# end_date = today


## IMAGE IMPORT ##

## DESIGN IMAGES ##
nba_logo_1 = Image.open('images/NBA_Logo.png')
nba_logo_2 = Image.open('images/NBA_Logo2.png')
court_img_1 = Image.open('images/Court1.png')

## EASTERN CONFERENCE LOGOS ##
East_logo = Image.open('images/east/NBA_East.png')
ATL_logo = Image.open('images/east/ATL-Hawks.png')
BKN_logo = Image.open('images/east/BKN-Nets.png')
BOS_logo = Image.open('images/east/BOS-Celtics.png')
CHI_logo = Image.open('images/east/CHI-Bulls.png')
CHA_logo = Image.open('images/east/CHA-Hornets.png')
CLE_logo = Image.open('images/east/CLE-Cavaliers.png')
DET_logo = Image.open('images/east/DET-Pistons.png')
IND_logo = Image.open('images/east/IND-Pacers.png')
MIA_logo = Image.open('images/east/MIA-Heat.png')
MIL_logo = Image.open('images/east/MIL-Bucks.png')
NYK_logo = Image.open('images/east/NYK-Knicks.png')
ORL_logo = Image.open('images/east/ORL-Magic.png')
PHI_logo = Image.open('images/east/PHI-Sixers.png')
TOR_logo = Image.open('images/east/TOR-Raptors.png')
WAS_logo = Image.open('images/east/WAS-Wizards.png')

## WESTERN CONFERENCE LOGOS ##
West_logo = Image.open('images/west/NBA_West.png')
DAL_logo = Image.open('images/west/DAL-Mavericks.png')
DEN_logo = Image.open('images/west/DEN-Nuggets.png')
GSW_logo = Image.open('images/west/GSW-Warriors.png')
HOU_logo = Image.open('images/west/HOU-Rockets.png')
LAC_logo = Image.open('images/west/LAC-Clippers.png')
LAL_logo = Image.open('images/west/LAL-Lakers.png')
MEM_logo = Image.open('images/west/MEM-Grizzlies.png')
MIN_logo = Image.open('images/west/MIN-Timberwolves.png')
NOP_logo = Image.open('images/west/NOP-Pelicans.png')
PHX_logo = Image.open('images/west/PHX-Suns.png')
POR_logo = Image.open('images/west/POR-Trailblazers.png')
SAC_logo = Image.open('images/west/SAC-Kings.png')
SAS_logo = Image.open('images/west/SAS-Spurs.png')
OKC_logo = Image.open('images/west/OKC-Thunder.png')
UTA_logo = Image.open('images/west/UTA-Jazz.png')


#%%

## FORMAT / STYLE ##

## COLOR SCALES ##

Tropic = px.colors.diverging.Tropic
Blackbody = px.colors.sequential.Blackbody
BlueRed = px.colors.sequential.Bluered

Sunsetdark = px.colors.sequential.Sunsetdark
Sunset = px.colors.sequential.Sunset
Temps = px.colors.diverging.Temps
Tealrose = px.colors.diverging.Tealrose

Ice = px.colors.sequential.ice
Ice_r = px.colors.sequential.ice_r
Dense = px.colors.sequential.dense
Deep = px.colors.sequential.deep
PuOr = px.colors.diverging.PuOr
Speed = px.colors.sequential.speed
# IceFire = px.colors.diverging.
# YlOrRd = px.colors.sequential.YlOrRd
# Mint = px.colors.sequential.Mint
# Electric = px.colors.sequential.Electric

# pd.options.display.float_format = '${:,.2f}'.format
# pd.set_option('display.max_colwidth', 200)

## VISUALIATION LABELS ##

all_cols = ['YR_TM_PLR', 'YEARS', 'YEAR',
            'TEAM', 'CHAMP', 'PLAYER', 'NUMBER',
            'POS', 'WTD POS',
            'HEIGHT (IN)',
            'WEIGHT (LBS)',
            'BMI', 'W-SPAN (IN)', 'APE',
            'AGE',  'EXPERIENCE',
            'NATION', 'COUNTRY',
            'CONTINENT', 'GLOBAL REGION',
            'CONFERENCE', 'COLLEGE',
            'SALARY', '% SALARY',
            'MP', 'PER', 'WTD-PER', 'AGE',
            'D-WS', 'O-WS', 'WS', 'WS_VAL', 'TM-WS',
            'RAPTOR', 'RAPTOR_VAL', 'TM-RAPTOR',
            'LEBRON', 'LEBRON_VAL', 'TM-LEBRON', #D #O
            'USG%',
            ]


viz_cols = ['YEAR', 'TEAM', 'CHAMP', 'PLAYER', 'WTD POS',
            'HEIGHT (IN)', 'WEIGHT (LBS)', 'BMI', 'W-SPAN (IN)', 'APE',
            'AGE',  'EXPERIENCE',
            'NATION', 'COUNTRY',
            'CONTINENT', 'GLOBAL REGION',
            'CONFERENCE', 'COLLEGE',
            'SALARY', '% SALARY',
            'MP', #'PER', 'WTD-PER',
            'D-WS', 'O-WS', 'WS',  # 'TM-WS', 'TM-RAPTOR',
            'RAPTOR', 'LEBRON', 'USG%',
            'RAPTOR_VAL', 'LEBRON_VAL', 'WS_VAL',

            ]

scale_cols = ['WTD POS',
              'RAPTOR', 'WS', #'LEBRON',
              'USG%', 'WS',
              'BMI', 'W-SPAN (IN)', 'APE',
              'AGE', #'EXPERIENCE',

            ]


## * DUMMIFICATION OF QUAL COLS

chart_labels = {'W-SPAN (IN)':'WINGSPAN (IN)',
                'APE':'APE INDEX',
                'CHAMP':'YR-TM',
                'LEBRON_VAL':'LEBRON/$',
                'RAPTOR_VAL':'RAPTOR/$',
                'WS_VAL':'WS/$',
                '1991':'1991-CHI', '1992':'1992-CHI', '1993':'1993-CHI',
                '1994':'1994-HOU', '1995':'1995-HOU',
                '1996':'1996-CHI', '1997':'1997-CHI', '1998':'1998-CHI',
                '1999':'1999-SAS', '2000':'2000-LAL', '2001':'2001-LAL', '2002':'2002-LAL',
                '2003':'2003-SAS', '2004':'2004-DET', '2005':'2005-SAS',
                '2006':'2006-MIA', '2007':'2007-SAS', '2008':'2008-BOS',
                '2009':'2009-LAL', '2010':'2010-LAL',
                '2011':'2011-DAL', '2012':'2012-MIA', '2013':'2013-MIA', '2014':'2014-SAS',
                '2015':'2015-GSW', '2016':'2016-CLE', '2017':'2017-GSW', '2018':'2018-GSW',
                '2019':'2019-TOR', '2020':'2020-LAL', '2021':'2021-MIL', '2022':'2022-GSW',
                # '':'',
                }

team_logos_dict = {'ATL':ATL_logo,
                   'BKN':BKN_logo,
                   'BOS':BOS_logo,
                   'CHI':CHI_logo,
                   'CHA':CHA_logo,
                   'CLE':CLE_logo,
                   'DET':DET_logo,
                   'IND':IND_logo,
                   'MIL':MIL_logo,
                   'MIA':MIA_logo,
                   'NYK':NYK_logo,
                   'ORL':ORL_logo,
                   'PHI':PHI_logo,
                   'TOR':TOR_logo,
                   'WAS':WAS_logo,

                   }

## COURT BACKGROUND ##
court_img_dict = dict(source=court_img_1,#'images/Court1.png', #
                                                           xref="paper",
                                                           yref="paper",
                                                           x=0.5,
                                                           y=0.5,
                                                           sizex=2.5,
                                                           sizey=1,
                                                           opacity=.5,
                                                           xanchor="center",
                                                           yanchor="middle", #top #bottom
                                                           visible=True,
                                                           layer="below",
                                                           # sizing="contain",
                                                           )


## FEATURED VARIABLES ##

team_list = list(champion_players['TEAM'].unique())
champ_list = list(champion_players['CHAMP'].unique())
college_list = list(champion_players['COLLEGE'].unique())
conference_list = list(champion_players['CONFERENCE'].unique())
country_list = list(champion_players['COUNTRY'].unique())
region_list = list(champion_players['GLOBAL REGION'].unique())



eastconf_logos_list = [ATL_logo, BKN_logo, BOS_logo, CHI_logo, CHA_logo,
                       CLE_logo, DET_logo, IND_logo, MIA_logo, MIL_logo,
                       NYK_logo, ORL_logo, PHI_logo, TOR_logo, WAS_logo]
westconf_logos_list = [DAL_logo, DEN_logo, HOU_logo, LAC_logo, LAL_logo,
                       GSW_logo, MEM_logo, MIN_logo, MEM_logo, PHX_logo,
                       SAS_logo, SAC_logo, OKC_logo, UTA_logo, POR_logo]


# print(team_list)
# print(college_list)
# print(conference_list)
# print(country_list)
# print(region_list)


# #%%
# # group_cols = ['']
# college_raptor = champion_players.groupby(['TEAM', 'COLLEGE']).mean()
# print(college_raptor)




#**#value per dollar is the key AKA secret sauce *** #



# from IPython.display import HTML
# import base64
#
# # convert your links to html tags
# def path_to_image_html(path):
#     return '<img src="'+ path + '" width="60" >'
#
# HTML(champion_players[['LOGO']].to_html(escape=False, formatters=dict(image=path_to_image_html)))

# print(champion_players.info())


## PRE-PROCESSING ##
# exo_drop_na = champion_players.dropna()
# exo_with_temp = champion_players[['st_temp_eff_k']].dropna()


## FILTER DATA ##
champion_players = champion_players[viz_cols]
champion_players = champion_players[champion_players['MP'] > 300]
lebron_val_players = champion_players[champion_players['YEAR'] >= 2010]




#%%
# features = champion_players.columns.to_list()[:]
# print(features)

numerical_champion_players = champion_players[scale_cols]
print(numerical_champion_players.info())
#%%

X = champion_players[scale_cols].values
X = StandardScaler().fit_transform(X)

#%%
pca = PCA(n_components='mle', svd_solver='full') # 'mle'

pca.fit(X)
X_PCA = pca.transform(X)
print('ORIGINAL DIMENSIONS:', X.shape)
print('TRANSFORMED DIMENSIONS:', X_PCA.shape)
print(f'EXPLAINED VARIANCE RATIO: {pca.explained_variance_ratio_}')

# 6 features explain ~95% of variance

#%%
x = np.arange(1, len(np.cumsum(pca.explained_variance_ratio_))+1, 1)

plt.figure(figsize=(12,8))
plt.plot(x, np.cumsum(pca.explained_variance_ratio_))
plt.xticks(x)

plt.show()

#%%
# AUTO DATASET

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
champ_pca_cols = champion_players.select_dtypes(include=numerics)
champ_pca_cols.info()

X = champion_players[champion_players._get_numeric_data().columns.to_list()[:-1]]
Y = champion_players['price']

#X.drop(columns='price', inplace=True, axis=1)

#%%
print(X)

#%%

X = StandardScaler().fit_transform(X)

#%%

# pca = PCA(n_components='mle', svd_solver='full') # 'mle'
pca = PCA(n_components=6, svd_solver='full') # 'mle'

pca.fit(X)
X_PCA = pca.transform(X)
print('ORIGINAL DIMENSIONS:', X.shape)
print('TRANSFORMED DIMENSIONS:', X_PCA.shape)
print(f'EXPLAINED VARIANCE RATIO: {pca.explained_variance_ratio_}')


#%%
x = np.arange(1, len(np.cumsum(pca.explained_variance_ratio_))+1, 1)

plt.figure(figsize=(12,8))
plt.plot(x, np.cumsum(pca.explained_variance_ratio_))
plt.xticks(x)
#plt.grid()
plt.show()

# 6 features explain ~95% of variance

#%%
# SINGULAR VALUE DECOMPOSITION ANALYSIS [SVD]
# CONDITION NUMBER

# ORIGINAL DATA

from numpy import linalg as LA

H = np.matmul(X.T, X)
_, d, _ = np.linalg.svd(H)
print(f'ORIGINAL DATA: SINGULAR VALUES {d}')
print(f'ORIGINAL DATA: CONDITIONAL NUMBER {LA.cond(X)}')


#%%
# TRANSFORMED DATA
H_PCA = np.matmul(X_PCA.T, X_PCA)
_, d_PCA, _ = np.linalg.svd(H_PCA)
print(f'TRANSFORMED DATA: SINGULAR VALUES {d_PCA}')
print(f'TRANSFORMED DATA: CONDITIONAL NUMBER {LA.cond(X_PCA)}')
print('*'*58)

#%%
# CONSTRUCTION OF REDUCED DIMENSION DATASET

#pca_df = pca.explained_variance_ratio_

a, b = X_PCA.shape
column = []

for i in range(b):
    column.append(f'PRINCIPAL COLUMN {i+1}')

df_PCA = pd.DataFrame(data=X_PCA, columns=column)
# df_PCA = pd.concat([df_PCA, Y], axis=1)

df_PCA.info()

#%%
print(df_PCA.describe())

#%%



#%%


#%%



#%%
## ELO
# import Elo_Rating as elo
#
# # %% ELO Rating System
#
# # instance of the Elo rating system. Uses a k-factor of 40 and 15 game for the provisional period
# i = elo.Implementation(k=40, k_prov=40, prov_games=15)
#
#
# def update_elo(game):
#     '''
#     For a given game, get the winning/losing jump ball player's id and name and update the Elo system
#
#     '''
#     winner_id = game.WINNING_JUMP_ID
#     loser_id = game.HOME_JUMPER_ID if game.HOME_JUMPER_ID != game.WINNING_JUMP_ID else game.AWAY_JUMPER_ID
#
#     winner_name = player_info[player_info.PLAYER_ID == winner_id].PLAYER_NAME.values[-1]
#     loser_name = player_info[player_info.PLAYER_ID == loser_id].PLAYER_NAME.values[-1]
#
#     winner_info = [winner_id, winner_name]
#     loser_info = [loser_id, loser_name]
#
#     if not i.getPlayer(winner_info):
#         i.addPlayer(winner_info)
#
#     if not i.getPlayer(loser_info):
#         i.addPlayer(loser_info)
#
#     i.recordMatch(winner_info, loser_info, winner=winner_info)
#
#
# jumps.progress_apply(lambda x: update_elo(x), axis=1)
#
# # put the results of the Elo system into a data frame
# player_df = pd.DataFrame()
#
# player_df['Player_ID'] = [player.name[0] for player in i.players]
# player_df['Player_Name'] = [player.name[1] for player in i.players]
# player_df['Rating'] = [player.rating for player in i.players]
# player_df['Game_Count'] = [player.game_count for player in i.players]
# player_df['Games_Won'] = player_df.Player_ID.progress_apply(lambda x: jumps[(jumps.WINNING_JUMP_ID == x)].shape[0])
# player_df['Win%'] = player_df.Games_Won / player_df.Game_Count
#
# player_df.to_csv('jumpballs.csv')
#
# class Implementation:
#     """
#     A class that represents an implementation of the Elo Rating System
#     """
#
#     def __init__(self, base_rating=1500, k=20, k_prov=40, prov_games=20):
#         """
#         Runs at initialization of class object.
#         @param base_rating - The rating a new player would have
#         """
#         self.base_rating = base_rating
#         self.k = k
#         self.k_prov = k_prov
#         self.prov_games = prov_games
#         self.players = []
#
#     def __getPlayerList(self):
#         """
#         Returns this implementation's player list.
#         @return - the list of all player objects in the implementation.
#         """
#         return self.players
#
#     def getPlayer(self, name):
#         """
#         Returns the player in the implementation with the given name.
#         @param name - name of the player to return.
#         @return - the player with the given name.
#         """
#         for player in self.players:
#             if player.name == name:
#                 return player
#         return None
#
#     def contains(self, name):
#         """
#         Returns true if this object contains a player with the given name.
#         Otherwise returns false.
#         @param name - name to check for.
#         """
#         for player in self.players:
#             if player.name == name:
#                 return True
#         return False
#
#     def addPlayer(self, name, rating=None):
#         """
#         Adds a new player to the implementation.
#         @param name - The name to identify a specific player.
#         @param rating - The player's rating.
#         """
#         if rating == None:
#             rating = self.base_rating
#
#         self.players.append(_Player(name=name, rating=rating))
#
#     def removePlayer(self, name):
#         """
#         Adds a new player to the implementation.
#         @param name - The name to identify a specific player.
#         """
#         self.__getPlayerList().remove(self.getPlayer(name))
#
#     def recordMatch(self, name1, name2, winner=None, draw=False):
#         """
#         Should be called after a game is played.
#         @param name1 - name of the first player.
#         @param name2 - name of the second player.
#         """
#         player1 = self.getPlayer(name1)
#         player2 = self.getPlayer(name2)
#
#         expected1 = player1.compareRating(player2)
#         expected2 = player2.compareRating(player1)
#
#         rating1 = player1.rating
#         rating2 = player2.rating
#
#         if draw:
#             score1 = 0.5
#             score2 = 0.5
#         elif winner == name1:
#             score1 = 1.0
#             score2 = 0.0
#         elif winner == name2:
#             score1 = 0.0
#             score2 = 1.0
#         else:
#             raise InputError('One of the names must be the winner or draw must be True')
#
#         if player1.game_count <= self.prov_games:
#             k_factor_1 = self.k_prov
#         else:
#             k_factor_1 = self.k
#
#         if player2.game_count <= self.prov_games:
#             k_factor_2 = self.k_prov
#         else:
#             k_factor_2 = self.k
#
#         newRating1 = rating1 + k_factor_1 * (score1 - expected1)
#         newRating2 = rating2 + k_factor_2 * (score2 - expected2)
#
#         if newRating1 < 0:
#             newRating1 = 0
#             newRating2 = rating2 - rating1
#
#         elif newRating2 < 0:
#             newRating2 = 0
#             newRating1 = rating1 - rating2
#
#         player1.rating = newRating1
#         player2.rating = newRating2
#
#         player1.game_count += 1
#         player2.game_count += 1
#
#     def getPlayerRating(self, name):
#         """
#         Returns the rating of the player with the given name.
#         @param name - name of the player.
#         @return - the rating of the player with the given name.
#         """
#         player = self.getPlayer(name)
#         return player.rating
#
#     def getRatingList(self):
#         """
#         Returns a list of tuples in the form of ({name},{rating})
#         @return - the list of tuples
#         """
#         lst = []
#         for player in self.__getPlayerList():
#             lst.append((player.name, player.rating))
#         return lst
#
#
# class _Player:
#     """
#     A class to represent a player in the Elo Rating System
#     """
#
#     def __init__(self, name, rating):
#         """
#         Runs at initialization of class object.
#         @param name - TODO
#         @param rating - TODO
#         """
#         self.name = name
#         self.rating = rating
#         self.game_count = 0
#
#     def compareRating(self, opponent):
#         """
#         Compares the two ratings of the this player and the opponent.
#         @param opponent - the player to compare against.
#         @returns - The expected score between the two players.
#         """
#         return (1 + 10 ** ((opponent.rating - self.rating) / 400.0)) ** -1

#%%