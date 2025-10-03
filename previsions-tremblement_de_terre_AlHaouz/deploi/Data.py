import streamlit as st
import pandas as pd
import numpy as np

# Définir les options Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

# Fonction pour charger les données à partir du fichier CSV
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data.copy()  # Cloner les données pour éviter la mutation accidentelle

# Fonction principale pour l'application Streamlit
def main():
    st.title('Analyse des données sismiques')

    # Charger les données depuis le fichier CSV
    file_path = "C:/Users/PC PRO/Desktop/project/deploi/data.csv"  # Mettez à jour avec votre propre chemin
    data = load_data(file_path)

    # Styles CSS personnalisés pour améliorer l'apparence
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 2.5em;
            color: #4B0082;
            text-align: center;
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 10px;
            background-color: #ADD8E6;
        }
        .sub-header {
            font-size: 1.8em;
            color: #4682B4;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        .data-preview {
            margin-top: 20px;
            margin-bottom: 50px;
        }
        .statistics {
            margin-top: 20px;
            margin-bottom: 50px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Section Aperçu des données
    st.markdown('<div class="sub-header">Aperçu des données</div>', unsafe_allow_html=True)
    st.write(data.head(), className="data-preview")

    # Section Statistiques descriptives
    st.markdown('<div class="sub-header">Statistiques descriptives</div>', unsafe_allow_html=True)
    st.write(data.describe(), className="statistics")

# Point d'entrée de l'application
if __name__ == '__main__':
    main()
