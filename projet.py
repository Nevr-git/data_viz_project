import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import datetime as dt

data = pd.read_csv("data/mod.csv", sep=";")

st.title("Viewl, a gas station finder, and more")
option = st.selectbox(
     'How would you like to visualise the application ?',
     ('Administrator', 'User'))

if option == "Administrator":
    st.write("You are an administrator")
    st.write("Histogram of the number of services available in a station:")
    histo, ax = plt.subplots()
    ax.hist(data["nbServices"], bins=25, rwidth=0.8)
    plt.xlabel("Number of services")
    plt.ylabel("Number of stations")
    st.pyplot(histo)
    #st.write(data["Gazole_maj"])
    #data["Gazole_maj"] = pd.to_datetime(data["Gazole_maj"], format="%Y-%m-%d %H:%M:%S")
    #st.write("Here are the average prices of the different carburants (€/L) in time:")
    #st.line_chart(data, x = ["Gazole_maj"], y = ["Gazole_prix", "SP95_prix", "SP98_prix", "E10_prix", "E85_prix", "GPLc_prix"])

else:
    st.write("You are a user")
    st.write("Please choose a carburant available in France:")
    carburant = st.selectbox(
        'Available carburants',
        ['Gazole','SP95','SP98','E10','E85','GPLc'])
    twentyfour_on_twentyfour = st.checkbox("Searching for a 24/24 station ?")
    if twentyfour_on_twentyfour:
        st.map(data[(data["Carburants disponibles"].fillna("").str.contains(carburant)) & (data["Automate 24-24 (oui/non)"] == "Oui")])#color = data[carburant+"_prix"].fillna(0)/data[carburant+"_prix"].fillna(0).max()
    else:
        st.map(data[data["Carburants disponibles"].fillna("").str.contains(carburant)])#, color = data[carburant+"_prix"].fillna(0)/data[carburant+"_prix"].fillna(0).max()"""

    st.write("Here are the average prices of ", carburant, "(€/L) depending on the department:")

    bar, ax = plt.subplots()
    ax.bar(range(0, 96), data.groupby("code_departement")[carburant+"_prix"].mean(), align="center")
    plt.xlabel("Departement")
    plt.ylabel("Price (€/L)")
    yy = data.groupby("code_departement")[carburant+"_prix"].mean()
    plt.ylim(min(yy)/1.01, max(yy)*1.01)
    st.pyplot(bar)