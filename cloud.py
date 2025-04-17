import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
        return  # Arrête la fonction ici en cas d’erreur

    # Vérifie que les colonnes existent
    if 'Fonction' in df.columns and 'Motif de départ' in df.columns:
        # Comptage du nombre de motifs de départ par fonction
        grouped = df.groupby('Fonction')['Motif de départ'].count().sort_values(ascending=False)

        # Création du graphique
        fig, ax = plt.subplots(figsize=(10, 6))
        grouped.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title("Nombre de départs par fonction")
        ax.set_xlabel("Fonction")
        ax.set_ylabel("Nombre de départs")
        plt.xticks(rotation=45, ha='right')

        # Affichage dans Streamlit
        st.pyplot(fig)
    else:
        st.warning("Les colonnes 'Fonction' ou 'Motif de départ' sont manquantes dans le fichier.")

# Appel de la fonction
show_sheets_page()
