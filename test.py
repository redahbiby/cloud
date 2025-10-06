import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 🎨 Configuration de la page
st.set_page_config(page_title="Fitness Goals Club", page_icon="💪", layout="centered")

# -------------------------------
# 🔹 Connexion à Google Sheets
# -------------------------------
SHEET_NAME = "fitness_progress"  # 👉 nom de ta feuille
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1

# -------------------------------
# 🔹 Header avec logo + titre
# -------------------------------
st.markdown(
    """
    <div style="display:flex; align-items:center; justify-content:center; margin-bottom:20px;">
        <img src="https://raw.githubusercontent.com/redahbiby/cloud/main/332101475_859229345140051_4358309886044135612_n.jpg" width="80">
        <h1 style="margin-left:10px;">Fitness Goals Club</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# 🔹 Menu navigation (boutons en ligne)
# -------------------------------
col1, col2, col3, col4, col5 = st.columns(5)
menu_selection = None
if col1.button("🏠 Accueil"): menu_selection = "Accueil"
if col2.button("👤 Profil"): menu_selection = "Profil"
if col3.button("🎯 Objectifs"): menu_selection = "Objectifs"
if col4.button("📊 Suivi"): menu_selection = "Suivi"
if col5.button("ℹ️ À propos"): menu_selection = "A propos"
if menu_selection is None: menu_selection = "Accueil"

# -------------------------------
# 🏠 Accueil
# -------------------------------
if menu_selection == "Accueil":
    st.subheader("Bienvenue 🏋️‍♂️")
    st.write("👉 Chaque membre peut enregistrer ses données et suivre ses progrès en temps réel.")

# -------------------------------
# 👤 Profil
# -------------------------------
elif menu_selection == "Profil":
    st.header("👤 Informations personnelles")
    nom = st.text_input("Quel est votre nom ?")
    age = st.slider("Quel âge as-tu ?", 0, 100, 25)
    genre = st.radio("Quel est votre genre ?", ["Homme", "Femme", "Autre"])

    if nom:
        st.success(f"Bienvenue, {nom} ! ({age} ans, {genre})")

# -------------------------------
# 🎯 Objectifs
# -------------------------------
elif menu_selection == "Objectifs":
    st.header("🎯 Vos objectifs sportifs")
    objectif = st.selectbox(
        "Quel est votre objectif principal ?",
        ["Perdre du poids", "Prendre du muscle", "Améliorer mon cardio", "Rester en forme"]
    )
    niveau = st.radio("Quel est votre niveau actuel ?", ["Débutant", "Intermédiaire", "Avancé"])

    if st.button("Générer un plan"):
        if objectif == "Perdre du poids":
            st.info("👉 3 séances de cardio + 2 muscu / semaine")
        elif objectif == "Prendre du muscle":
            st.info("👉 4 séances muscu + alimentation riche en protéines")
        elif objectif == "Améliorer mon cardio":
            st.info("👉 4 séances course/vélo/natation + 1 séance renfo")
        else:
            st.info("👉 3 séances variées (muscu + cardio + souplesse)")

# -------------------------------
# 📊 Suivi (Google Sheets)
# -------------------------------
elif menu_selection == "Suivi":
    st.header("📊 Suivi de vos progrès")

    nom = st.text_input("Entrez votre nom (même que profil)")
    poids = st.number_input("Votre poids actuel (kg)", min_value=30.0, max_value=200.0, step=0.1)

    if st.button("Enregistrer mon poids"):
        if nom.strip() != "":
            new_row = [str(date.today()), nom, poids]
            sheet.append_row(new_row)  # ✅ Enregistre dans Google Sheets
            st.success("✅ Données enregistrées dans Google Sheets !")
        else:
            st.error("⚠️ Veuillez entrer votre nom pour sauvegarder vos données.")

    # Charger toutes les données depuis Google Sheets
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    if not df.empty and "Nom" in df.columns:
        if nom.strip() != "":
            df_user = df[df["Nom"] == nom]
            if not df_user.empty:
                st.subheader("📅 Historique de votre poids")
                st.dataframe(df_user)

                st.subheader("📈 Évolution de votre poids")
                fig, ax = plt.subplots(figsize=(4,3))
                ax.plot(df_user["Date"], df_user["Poids"], marker="o", color="blue")
                ax.set_xlabel("Date")
                ax.set_ylabel("Poids (kg)")
                st.pyplot(fig)
            else:
                st.info("Aucune donnée trouvée pour ce nom.")

# -------------------------------
# ℹ️ À propos
# -------------------------------
elif menu_selection == "A propos":
    st.header("ℹ️ À propos")
    st.write("Application développée avec **FITNESS GOALS CLUB**. Chaque membre a son suivi personnel dans Google Sheets 📊.") 
    st.markdown("⚡ Développée par : **REDA HBIBY**") 

