import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import plotly.graph_objects as go

# Fonction pour afficher le premier graphique avec Plotly
def plot_initial_graph():
    # Exemple de série temporelle
    np.random.seed(0)
    date_range = pd.date_range(start='2023-09-01', periods=100, freq='D')
    serie = pd.Series(np.random.randn(len(date_range)), index=date_range)

    # Exemple de prédictions (mêmes dates pour cet exemple)
    predictions = pd.Series(np.random.randn(len(date_range)), index=date_range)

    # Créer une figure Plotly
    fig = go.Figure()

    # Ajouter les données réelles à la figure
    fig.add_trace(go.Scatter(x=serie.index, y=serie.values, mode='lines', name='Données réelles'))

    # Ajouter les prédictions à la figure
    fig.add_trace(go.Scatter(x=predictions.index, y=predictions.values, mode='lines', name='Prédictions', line=dict(color='red')))

    # Personnaliser la mise en page et les titres
    fig.update_layout(
        title='Prédictions ARIMA',
        xaxis_title='Date',
        yaxis_title='Magnitude',
        height=600,
        width=1000,
        font=dict(size=12),
        legend=dict(x=0, y=1.0, bgcolor='rgba(255, 255, 255, 0.5)', bordercolor='rgba(255, 255, 255, 0.5)')
    )

    # Afficher la figure
    st.plotly_chart(fig)

# Fonction pour afficher le second graphique avec Plotly
def plot_dynamic_forecast():
    # Création du DataFrame avec les dates mises à jour
    dates = pd.date_range(start='2023-09-01', end='2023-12-31', freq='D')
    data = {
        'Datetime': dates,
        'Magnitude': np.random.uniform(3.0, 7.0, len(dates))  # Génération de données aléatoires pour Magnitude
    }

    df = pd.DataFrame(data)
    df.set_index('Datetime', inplace=True)
    df.index = pd.DatetimeIndex(df.index, freq='D')  # Spécification explicite de la fréquence

    # On va se concentrer sur la variable Magnitude
    ts = df['Magnitude']

    # Ajustement du modèle SARIMA
    model = sm.tsa.statespace.SARIMAX(ts, order=(1, 1, 1), seasonal_order=(1, 1, 1, 7))
    model_fit = model.fit(disp=False)

    # Génération des prévisions dynamiques jusqu'à la fin de l'année 2023 et au-delà
    forecast_period = 30  # 30 jours de prévisions supplémentaires
    dynamic_forecast = model_fit.get_forecast(steps=forecast_period)
    mean_forecast = dynamic_forecast.predicted_mean
    conf_int = dynamic_forecast.conf_int()

    # Créer une nouvelle série temporelle avec les prévisions ajoutées
    forecast_index = pd.date_range(start=ts.index[-1] + pd.Timedelta(days=1), periods=forecast_period, freq='D')
    mean_forecast.index = forecast_index
    conf_int.index = forecast_index

    # Conversion des données pour Plotly
    ts_plotly = go.Scatter(x=ts.index, y=ts, mode='lines', name='Données réelles', opacity=0.6)
    forecast_plotly = go.Scatter(x=mean_forecast.index, y=mean_forecast, mode='lines', name='Prévisions dynamiques', line=dict(color='red'))
    conf_int_plotly = go.Scatter(
        x=forecast_index.tolist() + forecast_index.tolist()[::-1],
        y=conf_int.iloc[:, 0].tolist() + conf_int.iloc[:, 1].tolist()[::-1],
        fill='toself',
        fillcolor='rgba(255, 0, 0, 0.2)',
        line=dict(color='rgba(255, 0, 0, 0)'),
        hoverinfo="skip",
        showlegend=False
    )

    # Création de la figure Plotly
    fig = go.Figure([ts_plotly, forecast_plotly, conf_int_plotly])

    # Personnalisation du layout
    fig.update_layout(title='Prévisions dynamiques de Magnitude - Graphique en lignes',
                      xaxis_title='Date',
                      yaxis_title='Magnitude',
                      width=900,
                      height=500)

    # Affichage du graphique Plotly
    st.plotly_chart(fig)

# Code principal pour l'application Streamlit
def main():
    st.title('Visualisation des prévisions')

    st.header('Graphique 1: Prédictions ARIMA')
    plot_initial_graph()

    st.header('Graphique 2: Prévisions dynamiques de Magnitude')
    plot_dynamic_forecast()

if __name__ == '__main__':
    main()
