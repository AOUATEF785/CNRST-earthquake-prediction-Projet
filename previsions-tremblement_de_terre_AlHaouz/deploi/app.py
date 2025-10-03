import streamlit as st

def home_page():
    # Utilisez des colonnes pour afficher les logos côte à côte
    col1, col2, col3= st.columns(3)

    with col1:
        st.image('https://tse2.mm.bing.net/th?id=OIP.jPlg8OVUr44Nu3OM_vh9CgHaHa&pid=Api&P=0&h=180', width=200)
    st.write("")
    st.write("")
    st.write("")
   
    with col2:

        st.write("")
        st.write("") 


    with col3:
        st.image(r'C:\Users\PC PRO\Downloads\Image2.png', width=230)
    st.markdown('<div style="text-align: center;"><b>Analyse et prédiction des données sismiques ALHAOUZ</b></div>', unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")

    # Styles CSS personnalisés
        # Styles CSS personnalisés
    st.markdown("""
    <style>
    .main-title {
        font-size: 3em;
        color: white;
        text-align: center;
        margin-bottom: 20px;
        background: linear-gradient(to right, #4B0082, #000080);
        padding: 10px;
        border-radius: 10px;
    }
    .header {
        font-size: 2em;
        color: #FF4500; /* Rouge */
        text-align: center;
        margin-top: 20px;
    }
    .subheader {
        font-size: 1.5em;
        color: #4682B4;
        margin-top: 20px;
        text-align: center;
    }
    .content {
        font-size: 1.2em;
        margin-top: 10px;
        line-height: 1.6;
        text-align: justify;
        color: Black; /* Couleur du texte en blanc */
    }
    .highlight {
        color: #FF6347;
        font-weight: bold;
    }
    .section {
        margin: 30px 0;
    }
    .footer {
        font-size: 1em;
        color: #808080;
        text-align: center;
        margin-top: 50px;
    }
    .card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .button {
        background-color: #4B0082;
        color: white;
        padding: 10px 20px;
        text-align: center;
        border-radius: 5px;
        text-decoration: none;
        display: inline-block;
        font-size: 1.2em;
    }
    </style>
    """, unsafe_allow_html=True)
    # Titre principal
    st.markdown('<div class="main-title">Centre National des Recherches Scientifiques et Techniques</div>', unsafe_allow_html=True)

    # Sous-titre
    st.markdown('<div class="header">Bienvenue à l\'Institut National de Géophysique</div>', unsafe_allow_html=True)

    # Image d'accueil
    st.image('https://article19.ma/accueil/wp-content/uploads/2020/06/cnrst_bz1.jpg', use_column_width=True, caption="Institut National de Géophysique - Promouvoir la recherche géophysique")
    st.image('https://tse3.mm.bing.net/th?id=OIP.VLdSsbM1YUpXKg0YrnrdUwHaD4&pid=Api&P=0&h=180', use_column_width=True, caption="Réseau national et l’ensemble des stations géré par l'Institut National de Géophysique.")
    st.image('https://maghreb-observateur.com/wp-content/uploads/2023/09/image-27.png', use_column_width=True, caption="Réseau Sismologique National")
    st.image('https://tse4.mm.bing.net/th?id=OIP.p6u_l2wcmRRbf0mtnIP-9wHaEO&pid=Api&P=0&h=180', use_column_width=True, caption="Les répliques s'atténuent selon l'institut national de géophysique")
    # Section d'introduction
    st.markdown('<div class="section content">L\'Institut National de Géophysique est une institution dédiée à la promotion et au développement de la recherche en géophysique au Maroc. Récemment, notre institut a détecté un tremblement de terre dans la région d\'Al Haouz. Selon nos premières observations, le séisme a été enregistré à une magnitude de 4,5 sur l\'échelle de Richter. Les équipes de surveillance ont indiqué que le tremblement de terre s\'est produit à une profondeur relativement faible, ce qui a pu contribuer à son ressenti plus intense dans les zones proches de l\'épicentre. Nous sommes en contact avec les autorités locales pour évaluer les éventuels dommages et prendre les mesures nécessaires pour assurer la sécurité des habitants. Pour plus d\'informations sur nos activités de recherche en géophysique ou sur cet événement spécifique, veuillez nous contacter :</div>', unsafe_allow_html=True)

    # Section des contacts
    st.markdown('<div class="subheader">Contactez-nous</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="content">
        <ul>
            <li><strong>Adresse</strong> : Avenue des FAR et Allal El Fassi Hay Riad, B.P.8027 Rabat, Maroc</li>
            <li><strong>Téléphone</strong> : +212 537 56 98 00</li>
            <li><strong>Email</strong> : info@cnrst.ma</li>
            <li><strong>RH</strong> : grh@cnrst.ma</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Bouton d'appel à l'action
    st.markdown('<div style="text-align:center;"><a class="button" href="https://www.cnrst.ma" target="_blank">Visitez notre site web</a></div>', unsafe_allow_html=True)

    # Pied de page
    st.markdown('<div class="footer">© 2024 Institut National de Géophysique - Tous droits réservés.</div>', unsafe_allow_html=True)

import streamlit as st
from Data import main as Data_main  # Importer la fonction main de donnees_page.py
from prévision import main as prévision_main  # Importer la fonction main de prevision.py
from Exploration import main as Exploration_main  # Importer la fonction main de visualisation.py

# Fonction principale pour le routeur des pages
def main():
    st.title('Application Streamlit')
   
    # Sidebar de navigation
    menu = ['Home', 'Data', 'Prévision', 'Exploration']
    choice = st.sidebar.selectbox('Menu', menu)

    # Gestion de la sélection du menu
    if choice == 'Home':
        home_page()  # Appeler la fonction home_page définie ci-dessus
    elif choice == 'Data':
        Data_main()  # Appeler la fonction principale de donnees_page.py
    elif choice == 'Prévision':
        prévision_main()  # Appeler la fonction principale de prevision.py
    elif choice == 'Exploration':
        Exploration_main()  # Appeler la fonction principale de visualisation.py

if __name__ == '__main__':
    main()
