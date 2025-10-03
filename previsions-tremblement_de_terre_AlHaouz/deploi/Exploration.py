import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA

# Définir les options Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

# Fonction pour charger les données à partir du fichier CSV
@st.cache_data()  # Cache les données pour améliorer les performances
def load_data(file_path):
    return pd.read_csv(file_path)

# Fonction pour créer le graphique des résidus ARIMA
def create_residuals_fig(train_data):
    # Ajuster le modèle ARIMA (exemple avec ARIMA(1,0,0))
    model = ARIMA(train_data, order=(1, 0, 0))
    fit_model = model.fit()

    # Calculer les résidus
    residuals = train_data - fit_model.fittedvalues

    # Créer une figure Plotly pour la série temporelle des résidus
    residuals_fig = go.Figure()

    # Ajouter une trace de ligne pour la série temporelle des résidus
    residuals_fig.add_trace(go.Scatter(x=np.arange(len(train_data)), y=residuals,
                                       mode='markers+lines', marker=dict(color='blue'),
                                       name='Série temporelle des résidus'))

    # Personnalisation du layout de la figure
    residuals_fig.update_layout(title='Série temporelle des résidus',
                                xaxis_title='Index',
                                yaxis_title='Résidus',
                                height=600,
                                width=800)
    return residuals_fig

# Fonction principale pour l'application Streamlit
def main():
    # Titre principal de l'application
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
            color: black;
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
        .plot-header {
            font-size: 1.5em;
            color: #4682B4;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .data-preview {
            margin-top: 20px;
            margin-bottom: 50px;
        }
        .correlation-matrix {
            margin-top: 20px;
            margin-bottom: 60px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Section Histogramme de la magnitude
    st.markdown('<div class="sub-header">Histogramme de la magnitude</div>', unsafe_allow_html=True)
    fig_hist_magnitude = px.histogram(data, x='Magnitude', nbins=20, title='Histogramme de la magnitude')
    st.plotly_chart(fig_hist_magnitude)

    # Section ECDF de la magnitude
    st.markdown('<div class="sub-header">ECDF de la magnitude</div>', unsafe_allow_html=True)
    fig_ecdf_magnitude = px.ecdf(data, x='Magnitude', title='ECDF de la magnitude')
    st.plotly_chart(fig_ecdf_magnitude)

    # Section KDE Plot de la magnitude
    st.markdown('<div class="sub-header">KDE Plot de la magnitude</div>', unsafe_allow_html=True)
    fig_kde_magnitude = px.density_heatmap(data, x='Magnitude', title='KDE Plot de la magnitude', color_continuous_scale='thermal')
    st.plotly_chart(fig_kde_magnitude)

    # Section Scatterplot de la magnitude par rapport à la profondeur
    st.markdown('<div class="sub-header">Scatterplot de la magnitude par rapport à la profondeur</div>', unsafe_allow_html=True)
    fig_scatter_magnitude_depth = px.scatter(data, x='Magnitude', y='Profondeur', title='Scatterplot de la magnitude par rapport à la profondeur')
    st.plotly_chart(fig_scatter_magnitude_depth)

    # Section Heatmap de la profondeur et de la magnitude
    st.markdown('<div class="sub-header">Heatmap de la profondeur et de la magnitude</div>', unsafe_allow_html=True)
    heatmap_data = pd.pivot_table(data, values='Magnitude', index='Profondeur', columns='Date', aggfunc=np.mean)
    fig_heatmap_depth_magnitude = px.imshow(heatmap_data, labels={'x': 'Date', 'y': 'Profondeur', 'color': 'Magnitude'}, title='Heatmap de la profondeur et de la magnitude', color_continuous_scale='thermal')
    st.plotly_chart(fig_heatmap_depth_magnitude)

    # Section Pairplot pour visualiser les relations entre les variables numériques
    st.markdown('<div class="sub-header">Pairplot pour les variables numériques</div>', unsafe_allow_html=True)
    fig_pairplot = px.scatter_matrix(data, dimensions=['Magnitude', 'Profondeur', 'Latitude', 'Longitude'], title='Pairplot des variables numériques')
    st.plotly_chart(fig_pairplot)

    # Section Boxplot de la magnitude par rapport à l'année
    st.markdown('<div class="sub-header">Boxplot de la magnitude par rapport à l\'année</div>', unsafe_allow_html=True)
    data['Year'] = pd.to_datetime(data['Date']).dt.year
    fig_boxplot_year_magnitude = px.box(data, x='Year', y='Magnitude', title='Boxplot de la magnitude par rapport à l\'année')
    st.plotly_chart(fig_boxplot_year_magnitude)

    # Section Barplot du nombre de séismes par mois
    st.markdown('<div class="sub-header">Barplot du nombre de séismes par mois</div>', unsafe_allow_html=True)
    data['Month'] = pd.to_datetime(data['Date']).dt.month
    fig_barplot_monthly_earthquakes = px.bar(data, x='Month', title='Barplot du nombre de séismes par mois')
    st.plotly_chart(fig_barplot_monthly_earthquakes)

    # Section Histogramme de la profondeur des tremblements de terre
    st.markdown('<div class="sub-header">Histogramme de la profondeur des tremblements de terre</div>', unsafe_allow_html=True)
    fig_hist_depth = px.histogram(data, x='Profondeur', nbins=20, title='Histogramme de la profondeur des tremblements de terre')
    st.plotly_chart(fig_hist_depth)

    # Section Exemple de données (à remplacer par vos propres données)
    st.markdown('<div class="sub-header">Exemple de données</div>', unsafe_allow_html=True)
    example_data = pd.DataFrame({
        'Magnitude': [3.5, 4.2, 3.8, 4.5, 4.1],
        'Profondeur': [10, 15, 12, 18, 14],
        'Latitude': [30, 32, 31, 29, 33],
        'Longitude': [-120, -118, -119, -121, -117]
    })
    st.write(example_data)

    # Section Matrice de corrélation
    st.markdown('<div class="sub-header">Matrice de corrélation</div>', unsafe_allow_html=True)
    correlation_matrix = example_data[['Magnitude', 'Profondeur', 'Latitude', 'Longitude']].corr()
    fig_corr_matrix = px.imshow(correlation_matrix, text_auto=True, color_continuous_scale='thermal', title='Matrice de corrélation')
    st.plotly_chart(fig_corr_matrix)

    # Section Série temporelle des résidus ARIMA
    st.markdown('<div class="sub-header">Série temporelle des résidus ARIMA</div>', unsafe_allow_html=True)
    # Exemple de données pour le modèle ARIMA (à remplacer par vos propres données)
    np.random.seed(42)
    train_data = np.random.randn(100)
    fig_residuals = create_residuals_fig(train_data)
    st.plotly_chart(fig_residuals)
  
# Point d'entrée de l'application
if __name__ == '__main__':
    main()
