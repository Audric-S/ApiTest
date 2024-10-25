import streamlit as st
import yfinance as yf
import pydeck as pdk
import pandas as pd

# Données des entreprises S&P 500 intégrées
data = {
    "Name": [
        "Apple Inc", "Microsoft Corp", "Amazon.com Inc", "Alphabet Inc Class A", 
        "Alphabet Inc Class C", "Berkshire Hathaway Inc", "Meta Platforms Inc", 
        "Tesla Inc", "NVIDIA Corp", "JPMorgan Chase & Co", "Visa Inc", "UnitedHealth Group Inc", 
        "Johnson & Johnson", "Walmart Inc", "Procter & Gamble Co", "Mastercard Inc", 
        "Home Depot Inc", "Disney (Walt) Co", "Salesforce.com Inc", "Verizon Communications Inc", 
        "Coca-Cola Co", "Pfizer Inc", "Cisco Systems Inc", "PepsiCo Inc", "Exxon Mobil Corp",
        "Chevron Corp", "AbbVie Inc", "Netflix Inc", "Intel Corp", "Amgen Inc",
        "Nexstar Media Group Inc", "Union Pacific Corp", "Medtronic plc", "3M Co", 
        "Boeing Co", "Starbucks Corp", "PayPal Holdings Inc", "Lockheed Martin Corp", 
        "Thermo Fisher Scientific Inc", "IBM Corp", "T-Mobile US Inc", "Qualcomm Inc",
        "General Electric Co", "AT&T Inc", "Caterpillar Inc", "Texas Instruments Inc",
        "Salesforce Inc", "American Tower Corp", "S&P Global Inc", "Booking Holdings Inc",
        "Analog Devices Inc", "General Motors Co", "Broadcom Inc", "Bristol Myers Squibb Co",
        "Honeywell International Inc", "Linde plc", "Charter Communications Inc", "Equinix Inc",
        "Duke Energy Corp", "Illinois Tool Works Inc", "Northrop Grumman Corp", "Activision Blizzard Inc",
        "Capital One Financial Corp", "Southern Co", "Gilead Sciences Inc", "Biogen Inc",
        "Vertex Pharmaceuticals Inc", "Lam Research Corp", "Walt Disney Co", "American Express Co",
        "HCA Healthcare Inc", "Regeneron Pharmaceuticals Inc", "Crown Castle Inc", "CSX Corp",
        "Kweichow Moutai Co Ltd", "Cintas Corp", "The Kraft Heinz Co", "Freeport-McMoRan Inc",
        "Marriott International Inc", "Royal Caribbean Group", "Altria Group Inc", "NextEra Energy Inc",
        "KeyCorp", "Kroger Co", "Parker-Hannifin Corp", "Stryker Corp",
        "Hewlett Packard Enterprise Co", "Dell Technologies Inc", "D.R. Horton Inc", "PulteGroup Inc",
        "Foot Locker Inc", "Kellogg Co", "Mosaic Co", "Lennar Corp",
        "Newmont Corp", "Bristol-Myers Squibb Company", "Moderna Inc", "Zebra Technologies Corp",
        "EOG Resources Inc", "Simon Property Group Inc", "Aflac Inc", "Fortinet Inc",
        "BlackRock Inc", "American Airlines Group Inc", "Chubb Ltd", "Analog Devices Inc",
        "FISV", "Synchrony Financial", "Tapestry Inc", "MGM Resorts International",
        "Humana Inc", "CME Group Inc", "NortonLifeLock Inc", "Baker Hughes Co",
        "Huntington Bancshares Inc", "Vornado Realty Trust", "Boston Scientific Corp", 
        "Workday Inc", "PPL Corp", "Clorox Co", "SBA Communications Corp",
        "Xilinx Inc", "Noble Energy Inc", "Eversource Energy", "Williams Companies Inc",
        "Intercontinental Exchange Inc", "Lennar Corp", "Quest Diagnostics Inc", "FMC Corp",
        "Sempra Energy", "Ryder System Inc", "Weyerhaeuser Co", "Marsh & McLennan Companies Inc",
        "Carlyle Group Inc", "DuPont de Nemours Inc", "Snap Inc", "Regeneron Pharmaceuticals Inc",
        "Western Digital Corp", "Biogen Inc", "Harris Corp", "Darden Restaurants Inc",
        "Centrica plc", "Arista Networks Inc", "Seagate Technology Holdings plc", "Zillow Group Inc",
        "Brighthouse Financial Inc", "Spirit AeroSystems Holdings Inc", "Newell Brands Inc", 
        "WABCO Holdings Inc", "Maxim Integrated Products Inc", "Broadridge Financial Solutions Inc",
        "International Flavors & Fragrances Inc", "L3Harris Technologies Inc", "Molina Healthcare Inc",
        "Hewlett Packard Enterprise Co", "Cimpress plc", "Cheniere Energy Inc", "International Paper Co",
        "Electronic Arts Inc", "Northwest Natural Holding Co", "Verisk Analytics Inc", "Marathon Petroleum Corp",
        "Keurig Dr Pepper Inc", "KBR Inc", "Fastenal Co", "L3Harris Technologies Inc",
        "PPG Industries Inc", "CoStar Group Inc", "D.R. Horton Inc", "Wolverine World Wide Inc",
        "Salesforce.com Inc", "Fastenal Co", "Keysight Technologies Inc", "Bristol-Myers Squibb Co",
        "Pfizer Inc", "Discover Financial Services", "ViacomCBS Inc", "Baxter International Inc",
        "Coterra Energy Inc", "Kraft Heinz Co", "Hanesbrands Inc", "ViacomCBS Inc",
        "Corning Inc", "Chubb Limited", "Omnicom Group Inc", "SS&C Technologies Holdings Inc",
        "Truist Financial Corp", "First Republic Bank", "PG&E Corp", "Hanesbrands Inc",
        "D.R. Horton Inc", "Dexcom Inc", "Cameron International Corp", "Lennar Corp",
        "Motorola Solutions Inc", "Navient Corp", "Spectrum Brands Holdings Inc", "Citizens Financial Group Inc",
        "Prologis Inc", "Ameriprise Financial Inc", "Nordstrom Inc", "Las Vegas Sands Corp",
        "Seagate Technology Holdings plc", "Ulta Beauty Inc", "MGM Resorts International", "Intercontinental Exchange Inc",
        "AECOM", "S&P Global Inc", "Cognizant Technology Solutions Corp", "Evercore Inc",
        "Skyworks Solutions Inc", "McKesson Corp", "Seagate Technology Holdings plc", "Hanesbrands Inc"
    ],
    "Ticker": [
        "AAPL", "MSFT", "AMZN", "GOOGL", 
        "GOOG", "BRK-B", "META", 
        "TSLA", "NVDA", "JPM", "V", "UNH", 
        "JNJ", "WMT", "PG", "MA", 
        "HD", "DIS", "CRM", "VZ", 
        "KO", "PFE", "CSCO", "PEP", "XOM",
        "CVX", "ABBV", "NFLX", "INTC", "AMGN",
        "NXST", "UNP", "MDT", "MMM", 
        "BA", "SBUX", "PYPL", "LMT", 
        "TMO", "IBM", "TMUS", "QCOM",
        "GE", "T", "CAT", "TXN",
        "NOW", "AMT", "SPGI", "BKNG",
        "ADI", "GM", "AVGO", "BMY",
        "HON", "LIN", "CHTR", "EQIX",
        "DUK", "ITW", "NOC", "ATVI",
        "COF", "SO", "GILD", "BIIB",
        "VRTX", "LRCX", "DIS", "AXP",
        "HCA", "REGN", "CCI", "CSX",
        "Kweichow Moutai Co Ltd", "CTAS", "KHC", "FCX",
        "MAR", "RCL", "MO", "NEE",
        "KEY", "KR", "PH", "SYK",
        "HPE", "DELL", "DHI", "PHM",
        "FL", "K", "MOS", "LEN",
        "NEM", "BMY", "MRNA", "ZBRA",
        "EOG", "SPG", "AFL", "FTNT",
        "BLK", "AAL", "CB", "ADI",
        "FISV", "SYF", "TPR", "MGM",
        "HUM", "CME", "NLOK", "BKR",
        "HBAN", "VNO", "BSX", 
        "WDAY", "PPL", "CLX", "SBAC",
        "XLNX", "NBL", "ES", "WMB",
        "ICE", "LEN", "DGX", "FMC",
        "SRE", "R", "WY", "MMC",
        "CG", "DD", "SNAP", "REGN",
        "WDC", "BIIB", "HRS", "DRI",
        "CNA", "OMC", "SSNC", "TFC",
        "FRC", "PCG", "HBI", "VIAC",
        "GLW", "CB", "OMC", "SSNC",
        "TFC", "FRC", "PCG", "HBI",
        "DHI", "DXCM", "CAM", "LEN",
        "MSI", "NAVI", "SPB", "CZR",
        "PLD", "AMP", "JWN", "LVS",
        "STX", "ULTA", "MGM", "ICE",
        "ACM", "SPGI", "CTSH", "EVR",
        "SWKS", "MCK", "STX", "HBI"
    ],
    "Latitude": [
        37.3349, 47.6396, 47.6062, 37.4220, 
        37.4220, 41.2623, 37.4848, 
        37.3947, 37.3695, 40.7566, 37.7749, 44.9778,
        40.7128, 36.1627, 39.0997, 34.0522,
        33.7490, 33.6846, 37.7749, 40.7128,
        33.4484, 40.7128, 37.7749, 33.4484, 29.7604,
        29.9511, 41.8781, 38.9072, 41.8781, 37.7749,
        39.7392, 38.6270, 37.7749, 39.7392,
        37.7749, 39.7392, 36.1627, 40.7128,
        40.7128, 34.0522, 36.1627, 39.0997,
        38.9072, 39.7392, 38.6270, 34.0522,
        37.7749, 41.8781, 36.1627, 37.7749,
        34.0522, 34.0522, 39.7392, 33.4484,
        33.4484, 39.7392, 33.4484, 34.0522,
        39.7392, 34.0522, 34.0522, 33.4484,
        34.0522, 34.0522, 36.1627, 34.0522,
        39.7392, 37.7749, 36.1627, 41.8781,
        39.7392, 34.0522, 34.0522, 34.0522,
        39.7392, 37.7749, 36.1627, 34.0522,
        34.0522, 36.1627, 39.7392, 37.7749,
        34.0522, 39.7392, 41.8781, 34.0522,
        39.7392, 39.7392, 34.0522, 37.7749,
        36.1627, 34.0522, 39.7392, 39.7392,
        41.8781, 39.7392, 37.7749, 37.7749,
        39.7392, 39.7392, 39.7392, 39.7392,
        41.8781, 39.7392, 41.8781, 39.7392,
        36.1627, 39.7392, 39.7392, 34.0522,
        41.8781, 36.1627, 39.7392, 34.0522
    ],
    "Longitude": [
        -122.0090, -122.1281, -122.3321, -122.0841, 
        -122.0841, -95.9378, -122.1484, 
        -122.1500, -122.0365, -73.9884, -122.4194, -93.2650,
        -74.0060, -86.7816, -94.5783, -118.2437,
        -84.3879, -117.1611, -122.4194, -74.0060,
        -112.0740, -74.0060, -122.4194, -112.0740, -95.3698,
        -95.3698, -87.6298, -77.0369, -87.6298, -122.4194,
        -104.9903, -90.1994, -122.4194, -104.9903,
        -122.4194, -104.9903, -86.7816, -74.0060,
        -74.0060, -118.2437, -86.7816, -94.5783,
        -77.0369, -104.9903, -87.6298, -118.2437,
        -122.4194, -73.9352, -86.7816, -122.4194,
        -73.9352, -73.9352, -74.0060, -122.4194,
        -77.0369, -77.0369, -77.0369, -74.0060,
        -112.0740, -77.0369, -112.0740, -118.2437,
        -112.0740, -104.9903, -104.9903, -112.0740,
        -118.2437, -122.4194, -104.9903, -74.0060,
        -73.9352, -73.9352, -104.9903, -77.0369,
        -122.4194, -122.4194, -104.9903, -104.9903,
        -104.9903, -122.4194, -122.4194, -104.9903,
        -104.9903, -104.9903, -104.9903, -112.0740,
        -112.0740, -112.0740, -104.9903, -104.9903,
        -104.9903, -122.4194, -122.4194, -112.0740,
        -112.0740, -112.0740, -118.2437, -118.2437,
        -118.2437, -104.9903, -104.9903, -118.2437,
        -104.9903, -104.9903, -104.9903, -104.9903,
        -104.9903, -104.9903, -104.9903, -104.9903
    ]
}

# Création d'un DataFrame à partir des données
companies_df = pd.DataFrame(data)

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
            width = revenue / 10  # Diviser par 10 pour la visualisation
            
            # Créer une entrée pour le cylindre
            locations_df.append({
                'Name': row['Name'],
                'Ticker': row['Ticker'],
                'Latitude': row['Latitude'],
                'Longitude': row['Longitude'],
                'Height': height,
                'Width': width,
                'MarketCap': market_cap,
                'Revenue': revenue,
                'NetIncome': net_income,
                'PERatio': pe_ratio,
                'Inception': inception,
                'Color': revenue_to_color(revenue)
            })
    except Exception as e:
        print(f"Erreur avec {row['Name']}: {e}")

# Convertir les emplacements en DataFrame
locations_df = pd.DataFrame(locations_df)

# Définir la vue initiale de la carte
initial_view_state = pdk.ViewState(
    latitude=37.0902,
    longitude=-95.7129,
    zoom=3,
    pitch=0,
)

# Créer les objets pour les cylindre
layer = pdk.Layer(
    "ColumnLayer",
    data=locations_df,
    get_position=["Longitude", "Latitude"],
    get_radius="Width",
    get_height="Height",
    get_fill_color="Color",
    elevation_scale=10,
    pickable=True,
)

# Configuration de la carte
deck = pdk.Deck(
    layers=[layer],
    initial_view_state=initial_view_state,
    tooltip={"text": "{Name}"},
)

# Titre de l'application
st.title("Visualisation des entreprises du S&P 500")

# Affichage de la carte
st.pydeck_chart(deck)

# Zone de détails
if 'info' not in st.session_state:
    st.session_state.info = ""

# Affichage des détails des entreprises
if st.session_state.info:
    st.write("Détails de l'entreprise sélectionnée:")
    st.write(st.session_state.info)

# Callback pour récupérer les données de l'entreprise
def on_click(event):
    company = locations_df.iloc[event.index]
    details = f"""
    **Nom:** {company['Name']}
    **Ticker:** {company['Ticker']}
    **Market Cap:** ${company['MarketCap']:.2f} milliards
    **Revenus:** ${company['Revenue']:.2f} milliards
    **Bénéfice Net:** ${company['NetIncome']:.2f} milliards
    **Ratio Cours/Bénéfice:** {company['PERatio']}
    **Année de création:** {company['Inception']}
    """
    st.session_state.info = details

# Ajouter le callback à la couche
deck.on_click(on_click)
