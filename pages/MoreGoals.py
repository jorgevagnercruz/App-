import streamlit as st
import pandas as pd
import numpy as np
import base64

# DataFrame do Campeonato Brasileiro
df = pd.read_excel("https://www.football-data.co.uk/new/BRA.xlsx")
st.title("Web App Football Data")

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

st.sidebar.header("Times")
selected_league = st.sidebar.selectbox('São Paulo',['Palmeiras','Flamengo','Santos','Vitória'])

# WebScraping Football Data
def load_data(league):
  
  if selected_league == 'São Paulo':
    team = 'Sao Paulo'
  if selected_league == 'Palmeiras':
    team = 'Palmeiras'
  if selected_league == 'Flamengo':
    team = 'Flamengo'
  if selected_league == 'Santos':
    team = 'Santos'
  if selected_league == 'Vitória':
    team = 'Vitoria'
  
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df1 = df.groupby(['Home']).get_group(team)
df2 = df.groupby(['Away']).get_group(team)

