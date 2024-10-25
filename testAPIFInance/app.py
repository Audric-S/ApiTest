import streamlit as st
import yfinance as yf
import pydeck as pdk
import pandas as pd
import numpy as np

# Chargement des données des entreprises à partir du CSV
companies_df = pd.read_csv("data.csv")  # Assurez-vous que le chemin est correct

# DataFrame pour stocker les données des emplacements
locations_df = []

# Fonction pour générer une couleur en fonction du chiffre d'affaires
def revenue_to_color(revenue):
    # Normaliser les revenus pour obtenir une couleur entre 0 et 1
    norm_revenue = min(max(revenue, 0), 100) / 100  # Limiter à 100 milliards pour la normalisation
    # Générer une couleur entre bleu clair et bleu foncé
    r = int(0 * (1 - norm_revenue) + 0)  # Rouge reste 0
    g = int(0 * (1 - norm_revenue) + 0)  # Vert reste 0
    b = int(255 * norm_revenue)  # Bleu varie
    return [r, g, b, 160]

# Boucle à travers chaque entreprise pour récupérer les données nécessaires
for index, row in companies_df.iterrows():
    ticker = yf.Ticker(row['Ticker'])
    try:
        # Récupérer les données financières
        market_cap = ticker.info.get('marketCap', 0) / 1e9  # Capitalisation boursière en milliards
        revenue = ticker.info.get('totalRevenue', 0) / 1e9  # Revenus en milliards
        net_income = ticker.info.get('netIncome', 0) / 1e9  # Bénéfice net en milliards
        pe_ratio = ticker.info.get('trailingPE', "N/A")  # Ratio Cours/Bénéfice
        inception = ticker.info.get('yearFounded', "N/A")  # Année de création
        
        # Vérifier si la capitalisation boursière est supérieure à 20 milliards
        if market_cap > 20:
            # Hauteur : capitalisation boursière
            height = market_cap * 100  # Multiplier par 100 pour une meilleure visualisation
            
            # Largeur : revenus
            width = revenue  # Utiliser les revenus directement pour la largeur

            # Couleur basée sur les revenus
            color = revenue_to_color(revenue)

            # Ajouter les données de l'entreprise au DataFrame
            locations_df.append({
                "name": row['Name'],
                "market_cap": f"{market_cap:.1f}B",  # Formater la capitalisation boursière
                "revenue": f"{revenue:.1f}B",  # Revenus formatés
                "net_income": f"{net_income:.1f}B",  # Bénéfice net formaté
                "pe_ratio": pe_ratio,  # Ratio Cours/Bénéfice
                "inception": inception,  # Année de création
                "latitude": row['Latitude'],
                "longitude": row['Longitude'],
                "elevation": height,  # Hauteur basée sur la capitalisation boursière
                "width": width,  # Largeur basée sur les revenus
                "color": color
            })
    except Exception as e:
        st.warning(f"Could not retrieve data for {row['Ticker']}: {e}")

# Convertir le DataFrame en DataFrame pandas pour Pydeck
locations_df = pd.DataFrame(locations_df)

# Créer une couche 3D pour la carte
layer = pdk.Layer(
    "ColumnLayer",
    data=locations_df,
    get_position="[longitude, latitude]",
    get_elevation="elevation",
    elevation_scale=1,  # Ajustez ceci si nécessaire
    radius=20000,  # Réduire la largeur des colonnes
    get_fill_color="color",
    pickable=True,
    auto_highlight=True,
)

# Configuration de la vue de la carte
view_state = pdk.ViewState(
    latitude=39.5,
    longitude=-98.35,
    zoom=3,
    pitch=45,
)

# Afficher la carte avec un info-bulle enrichi
deck = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=view_state,
    layers=[layer],
    tooltip={
        "html": "<b>{name}</b><br/>Market Cap: {market_cap}<br/>Revenue: {revenue}<br/>Net Income: {net_income}<br/>P/E Ratio: {pe_ratio}<br/>Year Founded: {inception}",
        "style": {"color": "white"},
    },
)

# Afficher la carte dans Streamlit
st.pydeck_chart(deck)
