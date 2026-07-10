import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Analyse du marché de l'emploi", layout="wide")

st.title("Analyse du marché de l'emploi en génie mécanique")
st.write("Application développée dans le cadre d'un stage au HCP.")

connection = sqlite3.connect("marche_emploi_mecanique.db")
df = pd.read_sql_query("SELECT * FROM offres", connection)
connection.close()

st.subheader("Statistiques générales")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Offres", len(df))
c2.metric("Entreprises", df["Entreprise"].nunique())
c3.metric("Villes", df["Ville"].nunique())
c4.metric("Secteurs", df["Secteur d'activité"].nunique())

st.subheader("Tableau général des offres")
df.index += 1

st.dataframe(df, use_container_width=True)