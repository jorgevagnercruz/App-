import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

st.title("Times Brasileiros com mais gols em casa")

def load_data_jogos():
    data_jogos = pd.read_csv("https://www.football-data.co.uk/new/BRA.csv")
    
    return data_jogos

df_jogos = load_data_jogos()

st.dataframe(df_jogos)

df = df_jogos
df = df[['Season','Date','Home','Away','HG','AG','Res','PH','PD','PA']]
df.columns = ['Season','Date','Home','Away','Goals_H','Goals_A','Result','Odds_H','Odds_D','Odds_A']

flt = df.Season == 2022
df = df[flt]

def Prob_Home():
    P_H = 1/df.Odds_H
    return P_H

def Prob_Draw():
    P_D = 1/df.Odds_D
    return P_D

def Prob_Away():
    P_A = 1/df.Odds_A
    return P_A
  
df['p(H)'] = Prob_Home()
df['p(D)'] = Prob_Draw()
df['p(A)'] = Prob_Away()

df
