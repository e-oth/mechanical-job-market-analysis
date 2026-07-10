import streamlit as st
import sqlite3
import pandas as pd

st.title("Base de données")

connection = sqlite3.connect("marche_emploi_mecanique.db")
df = pd.read_sql_query("SELECT * FROM offres", connection)
connection.close()

recherche = st.text_input("Recherche")

if recherche:
    df = df[
        df["Titre du poste"].str.contains(recherche, case=False, na=False)
        |
        df["Entreprise"].str.contains(recherche, case=False, na=False)]

df.index += 1
st.dataframe(df, use_container_width=True)

st.download_button("Télécharger le CSV",df.to_csv(index=False).encode("utf-8"),
                   file_name="offres.csv",mime="text/csv")