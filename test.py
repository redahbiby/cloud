import streamlit as st

# 🎨 Configuration de la page
st.set_page_config(page_title="Fitness Goals Club", layout="centered")

# 🔹 Logo + Titre sur la même ligne (CSS/HTML)
st.markdown(
    f"""
    <style>
    .header-container {{
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }}
    .header-container img {{
        width: 200px;
        margin-right: 15px;
        border-radius: 10px;
    }}
    .header-container h1 {{
        color: #333;
        font-size: 72px;
    }}
    </style>
    <div class="header-container">
        <img src="https://raw.githubusercontent.com/redahbiby/cloud/main/332101475_859229345140051_4358309886044135612_n.jpg">
        <h1> Fitness Goals Club</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# 🏋️‍♂️ Sous-titre
st.subheader("Votre salle de sport en ligne")
st.write("Ici, vous pouvez suivre vos objectifs fitness et mieux connaître vos habitudes sportives.")

# 🔹 Informations utilisateur
st.header("👤 Informations personnelles")
nom = st.text_input("Quel est votre nom ?")
if nom:
    st.success(f"Enchanté, {nom} !")

age = st.slider("Quel âge as-tu ?", 0, 100, 25)
st.write(f"Vous avez **{age} ans**.")

if st.button("Confirmer mon âge"):
    st.balloons()

adulte = st.checkbox("Je confirme avoir plus de 18 ans")
if adulte and nom:
    st.success(f"Vous êtes adulte, {nom}. ✅")

# 🔹 Genre
genre = st.radio("Quel est votre genre ?", ["Homme", "Femme", "Autre"])
st.write(f"Genre choisi : **{genre}**")

# 🔹 Objectifs sportifs
st.header("🎯 Vos objectifs sportifs")
objectif = st.selectbox(
    "Quel est votre objectif principal ?",
    ["Perdre du poids", "Prendre du muscle", "Améliorer mon cardio", "Rester en forme"]
)
st.write(f"Votre objectif est : **{objectif}**")

# 🔹 Niveau d’expérience
niveau = st.radio("Quel est votre niveau actuel ?", ["Débutant", "Intermédiaire", "Avancé"])
st.write(f"Niveau choisi : **{niveau}**")

# 🔹 Plan de suivi personnalisé
if st.button("Générer un plan de base"):
    if objectif == "Perdre du poids":
        st.info("👉 Recommandation : 3 séances de cardio + 2 séances de musculation par semaine.")
    elif objectif == "Prendre du muscle":
        st.info("👉 Recommandation : 4 séances de musculation + alimentation riche en protéines.")
    elif objectif == "Améliorer mon cardio":
        st.info("👉 Recommandation : 4 séances de course/vélo/natation + 1 séance renfo.")
    else:
        st.info("👉 Recommandation : 3 séances variées (muscu + cardio + souplesse).")

# Footer
st.markdown("---")
st.caption("⚡ Application développée avec Streamlit | Fitness Goals Club 2025")




