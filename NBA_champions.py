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

# import matplotlib.pyplot as plt
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

## EASTERN CONFERENCE LOGOS ##
East_logo = Image.open('images/east/NBA_East.png')
ATL_logo = Image.open('images/east/ATL-Hawks.png')
BOS_logo = Image.open('images/east/BOS-Celtics.png')
CHI_logo = Image.open('images/east/CHI-Bulls.png')
CHA_logo = Image.open('images/east/CHA-Hornets.png')
CLE_logo = Image.open('images/east/CLE-Cavaliers.png')
DET_logo = Image.open('images/east/DET-Pistons.png')
IND_logo = Image.open('images/east/IND-Pacers.png')
MIA_logo = Image.open('images/east/MIA-Heat.png')
MIL_logo = Image.open('images/east/MIL-Bucks.png')
BKN_logo = Image.open('images/east/BKN-Nets.png')
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


## FORMAT / STYLE ##

## COLOR SCALES ##
YlOrRd = px.colors.sequential.YlOrRd
Mint = px.colors.sequential.Mint
Electric = px.colors.sequential.Electric
Sunsetdark = px.colors.sequential.Sunsetdark
Sunset = px.colors.sequential.Sunset
Tropic = px.colors.diverging.Tropic
Temps = px.colors.diverging.Temps
Tealrose = px.colors.diverging.Tealrose
Blackbody = px.colors.sequential.Blackbody
Ice = px.colors.sequential.ice
Ice_r = px.colors.sequential.ice_r
Dense = px.colors.sequential.dense

# pd.options.display.float_format = '${:,.2f}'.format
# pd.set_option('display.max_colwidth', 200)

## VISUALIATION LABELS ##

all_cols = ['YR_TM_PLR', 'YEARS', 'YEAR',
            'TEAM', 'PLAYER', 'NUMBER',
            'POS', 'WTD POS',
            'HEIGHT (IN)',
            'WEIGHT (LBS)',
            'BMI', 'W-SPAN (IN)',
            'AGE',  'EXPERIENCE',
            'NATION', 'COUNTRY',
            'CONTINENT', 'GLOBAL REGION',
            'CONFERENCE', 'COLLEGE',
            'SALARY', '% SALARY',
            'MP', 'PER', 'WTD-PER', 'AGE',
            'D-WS', 'O-WS', 'WS', 'TM-WS',
            'RAPTOR', 'TM-RAPTOR', 'USG%',
            ]


# output_cols = ['',
#                ''
#                ]

chart_labels = {'W-SPAN (IN)':'WINGSPAN',
                # '':'',
                # '':'',
                # '':'',
                # '':'',
                # '':'',
                # '':'',
                # '':'',
                }

## FEATURED VARIABLES ##

team_list = list(champion_players['TEAM'])
college_list = list(champion_players['COLLEGE'])
conference_list = list(champion_players['CONFERENCE'])
country_list = list(champion_players['COUNTRY'])
region_list = list(champion_players['GLOBAL REGION'])



## PRE-PROCESSING ##
# exo_drop_na = champion_players.dropna()
# exo_with_temp = champion_players[['st_temp_eff_k']].dropna()
# exo_with_dist = champion_players[['sy_distance_pc']].dropna()


## FILTER DATA ##
# disc_facility_filter = champion_players[champion_players['facility_count'] > 1]
# facility_filtered = disc_facility_filter['disc_facility'].unique()


## VISUALIZATIONS ##

scatter_3d_wingspan1 = px.scatter_3d(champion_players,
                                     x=champion_players['HEIGHT (IN)'],
                                     y=champion_players['WEIGHT (LBS)'],
                                     z=champion_players['WINGSPAN (IN)'],
                                     color=champion_players['WTD POS.'],
                                     color_discrete_sequence=Ice_r,
                                     color_continuous_scale=Ice_r,
                                     color_continuous_midpoint=3,
                                     title='NBA CHAMPIONS -- HEIGHT / WEIGHT / WINGSPAN',
                                     hover_name=champion_players['PLAYER'],
                                     hover_data=champion_players[['PLAYER', 'TEAM', 'YEAR']],
                                     # size=champion_players['pl_rade'],
                                     # size_max=50,
                                     # symbol=champion_players['disc_year'],
                                     labels=chart_labels,
                                     # range_x=[0,360],
                                     # range_y=[-50,50],
                                     # range_z=[0,2500],
                                     # range_color=Sunsetdark,
                                     opacity=.8,
                                     height=800,
                                     width=1600,
                                     )

scatter_matrix_raptor1 = px.scatter_matrix(champion_players,
                                     dimensions=['RAPTOR', 'D-WS', 'O-WS', 'WS', 'USG%'],
                                     color=champion_players['TEAM'],
                                     color_continuous_scale=Ice_r,
                                     color_discrete_sequence=Ice_r,
                                     hover_name=champion_players['PLAYER'],
                                     hover_data=champion_players[['PLAYER', 'TEAM', 'YEAR']],
                                     title='CHAMPIONSHIP CONTRIBUTIONS',
                                     labels=chart_labels,
                                     # height=850,
                                     # width=800,
                                     )


#
# disc_info_1 = px.histogram(disc_facility_filter,
#                            y=disc_facility_filter['disc_facility'],
#                            color=disc_facility_filter['disc_method'],
#                            color_discrete_sequence=Ice_r,
#                            hover_name=disc_facility_filter['pl_name'],
#                            hover_data=disc_facility_filter[['host_name', 'disc_facility', 'disc_telescope', 'sy_star_count', 'sy_planet_count']],
#                            # animation_frame=disc_facility_filter['disc_year'],
#                            # animation_group=disc_facility_filter['disc_facility'],
#                            title='EXOPLANET DISCOVERY FACILITY (BY DISCOVERY METHOD)',
#                            labels=chart_labels,
#                            range_x=[0,2500],
#                            height=1000,
#                            # width=800,
#                            )
#
# density_map_1 = px.density_contour(exoplanets,
#                                    x=exoplanets['ra'],
#                                    y=exoplanets['dec'],
#                                    z=exoplanets['sy_distance_pc'],
#                                    color=exoplanets['disc_method'],
#                                    color_discrete_sequence=Temps,
#                                    hover_name=exoplanets['pl_name'],
#                                    hover_data=exoplanets[['host_name', 'disc_facility', 'disc_telescope', 'sy_star_count', 'sy_planet_count']],
#                                    title='EXOPLANET RIGHT ASCENSION / DECLINATION',
#                                    labels=chart_labels,
#                                    )
#


#####################
### STREAMLIT APP ###
#####################

## CONFIGURATION ##
st.set_page_config(page_title='COMPOSITION OF NBA CHAMPIONS', layout='wide', initial_sidebar_state='auto') #, page_icon=":smirk:"

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)

## CSS LAYOUT CUSTOMIZATION ##

th_props = [('font-size', '12px'),
            ('text-align', 'center'),
            ('font-weight', 'bold'),
            ('color', '#EBEDE9'), #6d6d6d #29609C
            ('background-color', '#29609C') #f7f7f9
            ]

td_props = [('font-size', '12px'),
            # ('text-align', 'center'),
            # ('font-weight', 'bold'),
            # ('color', '#EBEDE9'), #6d6d6d #29609C
            # ('background-color', '#29609C') #f7f7f9
            ]

df_styles = [dict(selector="th", props=th_props),
             dict(selector="td", props=td_props)]


# col_format_dict = {'BYE': "{:,}",
#                    '': "{:,}",
#                    '': "{:,}",
#                    '': "{:,}",
#                    '': "{:,}",
#                    '': "{:,}",
#                    '': "{:,}",
#                    'O-WS': "{:,}",
#                    'D-WS': "{:,}",
#                    'WS': "{:,}",
#                    'TM_WS': "{:,}",
                   # #: "{:.1%}", #:"{:.1}x", "${:.2}", #"${:,}"
#                   }


## SIDEBAR ##
# st.sidebar.xyz


## HEADER ##
st.container()

st.title('WINNING COMPOSITION OF NBA CHAMPIONS')
st.write('*CHAMPIONSHIP-CALIBER ROSTER CONSTRUCTION FOR MODERN-DAY BASKETBALL*')

## EAST LOGOS ##
EA_col_1, EA_col_2, EA_col_3, EA_col_4, EA_col_5, \
EC_col_1, EC_col_2, EC_col_3, EC_col_4, EC_col_5, \
ES_col_1, ES_col_2, ES_col_3, ES_col_4, ES_col_5 = st.columns(15)
EA_col_1.image(BOS_logo, caption='BOS', width=45)
EA_col_2.image(BKN_logo, caption='BKN', width=45)
EA_col_3.image(NYK_logo, caption='NYK', width=45)
EA_col_4.image(PHI_logo, caption='PHI', width=45)
EA_col_5.image(TOR_logo, caption='TOR', width=45)
EC_col_1.image(CHI_logo, caption='CHI', width=45)
EC_col_2.image(CLE_logo, caption='CLE', width=45)
EC_col_3.image(DET_logo, caption='DET', width=45)
EC_col_4.image(IND_logo, caption='IND', width=45)
EC_col_5.image(MIL_logo, caption='MIL', width=45)
ES_col_1.image(ATL_logo, caption='ATL', width=45)
ES_col_2.image(MIA_logo, caption='MIA', width=45)
ES_col_3.image(ORL_logo, caption='ORL', width=45)
ES_col_4.image(WAS_logo, caption='WAS', width=45)
ES_col_5.image(CHA_logo, caption='CHA', width=45)

## WEST LOGOS ##
WN_col_1, WN_col_2, WN_col_3, WN_col_4, WN_col_5, \
WP_col_1, WP_col_2, WP_col_3, WP_col_4, WP_col_5, \
WS_col_1, WS_col_2, WS_col_3, WS_col_4, WS_col_5 = st.columns(15)
WN_col_1.image(DEN_logo, caption='DEN', width=45)
WN_col_2.image(MIN_logo, caption='MIN', width=45)
WN_col_3.image(POR_logo, caption='POR', width=45)
WN_col_4.image(OKC_logo, caption='OKC', width=45)
WN_col_5.image(UTA_logo, caption='UTA', width=45)
WP_col_1.image(GSW_logo, caption='GSW', width=45)
WP_col_2.image(LAC_logo, caption='LAC', width=45)
WP_col_3.image(LAL_logo, caption='LAL', width=45)
WP_col_4.image(PHX_logo, caption='PHX', width=45)
WP_col_5.image(SAC_logo, caption='SAC', width=45)
WS_col_1.image(NOP_logo, caption='NOP', width=45)
WS_col_2.image(DAL_logo, caption='DAL', width=45)
WS_col_3.image(HOU_logo, caption='HOU', width=45)
WS_col_4.image(SAS_logo, caption='SAS', width=45)
WS_col_5.image(MEM_logo, caption='MEM', width=45)

## 3D SCATTER ##
st.plotly_chart(scatter_3d_wingspan1, use_container_width=False, sharing="streamlit")

## SCATTER MATRIX ##
st.plotly_chart(scatter_matrix_raptor1, use_container_width=False, sharing="streamlit")


## LEAGUE LOGOS ##
east_col_1, nba_col_2, west_col_3 = st.columns(3)
east_col_1.image(East_logo, width=300) # caption='WESTERN CONFERENCE'
nba_col_2.image(nba_logo_1, width=300) # caption='NATIONAL BASKETBALL ASSOCIATION'
west_col_3.image(West_logo, width=300) # caption='EASTERN CONFERENCE'


## TABLEAU ##
## NEO4J / MONGO ?? ##




## SELECTION FORM ##
# exo_drop_cols = ['', '']


## FORM FUNCTIONS ##
# @st.cache(persist=True, allow_output_mutation=True, suppress_st_warning=True)



## DISCOVERY INFORMATION ##
# st.plotly_chart(disc_info_1.update_yaxes(categoryorder='total ascending'), use_container_width=True, sharing="streamlit")




## EXTERNAL LINKS ##

github_link = '[GITHUB REPOSITORY](https://github.com/nehat312/NBA-championship-caliber/)'
nba_site_link = '[NBA.com](https://www.nba.com/)'
bbref_site_link = '[BASKETBALL REFERENCE](https://www.basketball-reference.com/)'

link_col_1, link_col_2, link_col_3 = st.columns(3)
ext_link_1 = link_col_1.markdown(github_link, unsafe_allow_html=True)
ext_link_2 = link_col_2.markdown(nba_site_link, unsafe_allow_html=True)
ext_link_3 = link_col_3.markdown(bbref_site_link, unsafe_allow_html=True)


## SCRIPT TERMINATION ##
st.stop()




### INTERPRETATION ###





### SCRATCH NOTES ###






## FONTS ##

# t = st.radio("Toggle to see font change", [True, False])
#
# if t:
#     st.markdown(
#         """
#         <style>
# @font-face {
#   font-family: 'Tangerine';
#   font-style: normal;
#   font-weight: 400;
#   src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
#   unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
# }
#
#     html, body, [class*="css"]  {
#     font-family: 'Tangerine';
#     font-size: 48px;
#     }
#     </style>
#
#     """,
#         unsafe_allow_html=True,
#     )
#
# "# Hello"
#
# """This font will look different, based on your choice of radio button"""

# CONFIG TEMPLATE
    # st.set_page_config(page_title="CSS hacks", page_icon=":smirk:")
    #
    # c1 = st.container()
    # st.markdown("---")
    # c2 = st.container()
    # with c1:
    #     st.markdown("Hello")
    #     st.slider("World", 0, 10, key="1")
    # with c2:
    #     st.markdown("Hello")
    #     st.slider("World", 0, 10, key="2")

# STYLE WITH CSS THROUGH MARKDOWN
    # st.markdown("""
    # <style>
    # div[data-testid="stBlock"] {
    #     padding: 1em 0;
    #     border: thick double #32a1ce;
    # }
    # </style>
    # """, unsafe_allow_html=True)


# STYLE WITH JS THROUGH HTML IFRAME
    # components.html("""
    # <script>
    # const elements = window.parent.document.querySelectorAll('div[data-testid="stBlock"]')
    # console.log(elements)
    # elements[0].style.backgroundColor = 'paleturquoise'
    # elements[1].style.backgroundColor = 'lightgreen'
    # </script>
    # """, height=0, width=0)


# st.markdown("""
#             <style>
#             div[data-testid="stBlock"] {padding: 1em 0; border: thick double #32a1ce; color: blue}
#             </style>
#             """,
#             unsafe_allow_html=True)

# style={'textAlign': 'Center', 'backgroundColor': 'rgb(223,187,133)',
#                                            'color': 'black', 'fontWeight': 'bold', 'fontSize': '24px',
#                                            'border': '4px solid black', 'font-family': 'Arial'}),

#pattern_shape = "nation", pattern_shape_sequence = [".", "x", "+"]

            # fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", facet_row="time", facet_col="day",
            #        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})

            # fig = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species")

            # fig = px.parallel_categories(df, color="size", color_continuous_scale=px.colors.sequential.Inferno)

            # fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
            #                   "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
            #                   "petal_width": "Petal Width", "petal_length": "Petal Length", },
            #                     color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
