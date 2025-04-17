import streamlit as st
st.title("Ma première application Streamlit")
st.write("Bienvenue dans cette atkii  !")
nom = st.text_input("Quel est votre nom ?")
if nom:
    st.success(f"Enchanté, {nom} ! ")

age = st.slider("Quel est votre âge ?", 0, 100, 25)

st.write(f"Vous avez {age} ans")
genre = st.radio("Quel est votre genre ?", ["Homme", "Femme",])
st.write(f"Genre choisi : {genre}")
debut= st.date_input(f"entrez la date de debut")
st.write (f"date debut est:{debut}")

if st.button("Cliquez ici"):
    st.balloons()