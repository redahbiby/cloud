import streamlit as st
st.title ('madame mon coeur')
st.write ("je t'aime")
nom = st.text_input("Quel est votre nom ?")
if nom:
    st.success(f"Enchanté, {nom} ! ")
age= st.slider("combien tu maime?",0,100,50)
st.write (f"vous avez ,{age} ans" )
if st.button(f"cliquez ici si c'est vrai"):
    st.balloons()
adulte= st.checkbox('cliquez ici si tu as plus que 18 ans')
if adulte:
    st.success(f"vous etes adulte,{nom}")
genre = st.radio("Quel est votre genre ?", ["Homme", "Femme", "Autre"])
st.write(f"Genre choisi : {genre}")