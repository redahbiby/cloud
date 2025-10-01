import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import os

# 🎨 Configuration de la page (centered pour mobile)
st.set_page_config(page_title="Fitness Goals Club", page_icon="💪", layout="centered")

# -------------------------------
# 🔹 CSS Responsive Mobile
# -------------------------------
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .header-container {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        flex-wrap: wrap;
    }
    .header-container img {
        width: 80px;  /* plus petit pour mobile */
        margin-right: 10px;
        border-radius: 8px;
    }
    .header-container h1 {
        color: #222;
        font-size: 28px;  /* réduit pour petits écrans */
    }
    @media (max-width: 600px) {
        .header-container {
            flex-direction: column;
            text-align: center;
        }
        .header-container img {
            margin-bottom: 10px;
        }
        .header-container h1 {
            font-size: 24px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 🔹 En-tête avec logo + titre
# -------------------------------
st.markdown(
    f"""
    <div class="header-container">
        <img src="https://raw.githubusercontent.com/redahbiby/cloud/main/332101475_859229345140051_4358309886044135612_n.jpg">
        <h1>Fitness Goals Club</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# 🔹 Menu navigation (Selectbox au lieu de sidebar pour mobile)
# -------------------------------
menu = st.selectbox(
    "📌 Navigation",
    ["🏠 Accueil", "👤 Profil", "🎯 Objectifs", "📊 Suivi de progression", "ℹ️ À propos"]
)

# -------------------------------
# 🏠 Page Accueil
# -------------------------------
if menu == "🏠 Accueil":
    st.subheader("Bienvenue dans votre salle de sport en ligne 🏋️‍♂️")
    st.write("👉 Suivez vos objectifs, enregistrez vos progrès et restez motivé chaque jour.")

# -------------------------------
# 👤 Profil utilisateur
# -------------------------------
elif menu == "👤 Profil":
    st.header("👤 Informations personnelles")
    nom = st.text_input("Quel est votre nom ?")
    age = st.slider("Quel âge as-tu ?", 0, 100, 25)
    genre = st.radio("Quel est votre genre ?", ["Homme", "Femme", "Autre"])

    if nom:
        st.success(f"Enchanté, {nom} ! Vous avez {age} ans et vous êtes {genre}.")

# -------------------------------
# 🎯 Objectifs
# -------------------------------
elif menu == "🎯 Objectifs":
    st.header("🎯 Vos objectifs sportifs")
    objectif = st.selectbox(
        "Quel est votre objectif principal ?",
        ["Perdre du poids", "Prendre du muscle", "Améliorer mon cardio", "Rester en forme"]
    )
    niveau = st.radio("Quel est votre niveau actuel ?", ["Débutant", "Intermédiaire", "Avancé"])

    if st.button("Générer un plan de base"):
        if objectif == "Perdre du poids":
            st.info("👉 Recommandation : 3 séances de cardio + 2 séances de musculation par semaine.")
        elif objectif == "Prendre du muscle":
            st.info("👉 Recommandation : 4 séances de musculation + alimentation riche en protéines.")
        elif objec
