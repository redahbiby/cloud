import streamlit as st
import pandas as pd
import plotly.express as px

def show_sheets_page():
    st.title("Lecture de Google Sheets dans Streamlit")

    # Remplace cet ID par celui de ta feuille Google Sheets
    sheet_id = "1JUDA-tJpzyUpDSXb-daKN7ACVAP7LUboRVVplQD34eA"
    sheet_name = "listdepart"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        df = pd.read_csv(url)
        st.success("Données chargées avec succès depuis Google Sheets !")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        # Graphique en barres
# Graphique en barres
fig = px.bar(df, x='Fonction', y='Motif de départ', title='depart users')
st.plotly_chart(fig)


# Appel de la fonction
show_sheets_page()
