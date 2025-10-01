import streamlit as st

# 🎨 Configuration de la page
st.set_page_config(page_title="Fitness Goals Club", page_icon="💪", layout="centered")

# 🔹 Ajouter un arrière-plan (image hébergée en ligne)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1571019613914-85f342c1d4b1"); 
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🏋️‍♂️ Titre et description
st.title("💪 Bienvenue au Fitness Goals Club")
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

# 🔹 Plan de suivi (exemple simple)
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
