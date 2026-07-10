import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(layout="wide")
st.title("Dashboard")
connection = sqlite3.connect("marche_emploi_mecanique.db")
df = pd.read_sql_query("SELECT * FROM offres", connection)
connection.close()

ville = st.sidebar.selectbox("Ville",["Toutes"] + sorted(df["Ville"].unique().tolist()))
secteur = st.sidebar.selectbox("Secteur",["Tous"] + sorted(df["Secteur d'activité"].unique().tolist()))
entreprise = st.sidebar.selectbox("Entreprise",["Tous"] + sorted(df["Entreprise"].unique().tolist()))
compétences = st.sidebar.selectbox("Compétences techniques",["Toutes"] + sorted(df["Compétences techniques"].unique().tolist()))
langue = st.sidebar.selectbox("Langues",["Tous"] + sorted(df["Langues"].unique().tolist()))

if ville != "Toutes":
    df = df[df["Ville"] == ville]

if secteur != "Tous":
    df = df[df["Secteur d'activité"] == secteur]

if entreprise != "Tous":
    df = df[df["Entreprise"] == entreprise]

if compétences != "Toutes":
    df = df[df["Compétences techniques"] == compétences]

if langue != "Tous":
    df = df[df["Langues"] == langue]

tab1, tab2, tab3 = st.tabs([ "Vue Macro-Économique",
                             "Analyse Sectorielle",
                             "Analyse des Compétences"])

with tab1:

    st.subheader("Répartition des offres par ville")
    villes = df[df["Ville"] != "Non spécifié"]["Ville"].value_counts().head(10)
    st.bar_chart(villes)

    st.subheader("Répartition des contrats")
    st.subheader("Niveau d'étude")

with tab2:

    st.subheader("Top secteurs")
    secteurs = df[df["Secteur d'activité"] != "Non spécifié"]["Secteur d'activité"].value_counts().head(10)
    st.bar_chart(secteurs)

    st.subheader("Top entreprises")

with tab3:

    st.subheader("Compétences techniques")

    competences = (df[df["Compétences techniques"] != "Non spécifié"]["Compétences techniques"].dropna().str.split(",").explode().str.strip())
    st.bar_chart(competences.value_counts().head(15))

    
    