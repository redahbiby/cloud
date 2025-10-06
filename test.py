try:
    sheet.append_row(["TEST", "Connexion réussie", "✅"])
    st.success("Connexion à Google Sheets OK ✅")
except Exception as e:
    st.error(f"Erreur de connexion Google Sheets ❌ : {e}")
