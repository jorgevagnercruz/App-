import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

st.title("Times Brasileiros com mais gols")

def load_data_jogos():
    data_jogos = pd.read_csv("https://www.football-data.co.uk/new/BRA.csv")
    return data_jogos

df_jogos = load_data_jogos()

st.dataframe(df_jogos)
