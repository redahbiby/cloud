import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import os

# 🎨 Configuration de la page
st.set_page_config(page_title="Fitness Goals Club", page_icon="💪", layout="wide")

# -------------------------------
# 🔹 CSS pour thème personnalisé
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
    }
    .header-container img {
        width: 120px;
        margin-right: 15px;
        border-radius: 10px;
    }
    .header-container h1 {
        color: #222;
        font-size: 42px;
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
# 🔹 Barre latérale navigation
# -------------------------------
menu = st.sidebar.radio(
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
        elif objectif == "Améliorer mon cardio":
            st.info("👉 Recommandation : 4 séances de course/vélo/natation + 1 séance renfo.")
        else:
            st.info("👉 Recommandation : 3 séances variées (muscu + cardio + souplesse).")

# -------------------------------
# 📊 Suivi de progression
# -------------------------------
elif menu == "📊 Suivi de progression":
    st.header("📊 Suivi de vos progrès")

    # Fichier CSV pour sauvegarder
    file_path = "progression.csv"

    # Charger données si fichier existe
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=["Date", "Poids (kg)"])

    # Entrée poids actuel
    poids = st.number_input("Entrez votre poids actuel (kg)", min_value=30.0, max_value=200.0, step=0.1)
    if st.button("Enregistrer mon poids"):
        new_data = pd.DataFrame([[date.today(), poids]], columns=["Date", "Poids (kg)"])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(file_path, index=False)
        st.success("✅ Poids enregistré avec succès !")

    # Afficher historique
    if not df.empty:
        st.subheader("📅 Historique du poids")
        st.dataframe(df)

        # Graphique de progression
        st.subheader("📈 Évolution du poids")
        fig, ax = plt.subplots()
        ax.plot(df["Date"], df["Poids (kg)"], marker="o", linestyle="-", color="blue")
        ax.set_xlabel("Date")
        ax.set_ylabel("Poids (kg)")
        ax.set_title("Progression du poids")
        st.pyplot(fig)

# -------------------------------
# ℹ️ À propos
# -------------------------------
elif menu == "ℹ️ À propos":
    st.header("ℹ️ À propos")
    st.write("Cette application a été développée avec **Streamlit** pour aider les passionnés de fitness à suivre leurs progrès et rester motivés.")
    st.markdown("⚡ Développée par : **Fitness Goals Club 2025**")
    st.markdown("---")
