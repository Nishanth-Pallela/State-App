import streamlit as st
import pandas as pd

st.title("State App")

state = st.text_input(label="jhbhj", label_visibility='hidden', placeholder="Enter state here...")

df = pd.read_csv("wheather.csv", sep=',')
for index, sta in df.iterrows():
    if state.title() == sta['state']:
        st.header(sta["state"])
        st.subheader(f"{sta['capitals']} is the capital of {sta['state']}.")
        st.subheader(f"The nickname of {sta['state']} is {sta['nicknames']}")
