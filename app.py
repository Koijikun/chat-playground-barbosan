import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    data = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
    return data

data = load_data()

st.title("MDM-Streamlit")

display_type = st.radio("Wie sollen die Daten dargestellt werden?", ("Tabelle", "Grafik"))

row_range = st.slider("Wieviele Datensätze sollen angezeigt werden?", 0, len(data)-1, (0, 100))

filtered_data = data.iloc[row_range[0]:row_range[1]]

if 'Index' in filtered_data.columns:
    filtered_data = filtered_data.drop(columns=['Index'])

if display_type == "Tabelle":
    st.write("Tabelle:")
    st.write(filtered_data)
else:
    st.write("Grafik:")
    fig, ax = plt.subplots()
    ax.set_xlabel("Grösse (Inches)") 
    ax.set_ylabel("Gewicht (Pounds)") 
    sns.scatterplot(data=filtered_data, x=data.columns[2], y=data.columns[1], ax=ax)
    st.pyplot(fig)
