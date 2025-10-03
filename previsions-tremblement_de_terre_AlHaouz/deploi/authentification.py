import streamlit as st

# Fonction pour l'authentification
def authenticate(username, password):
    # Simulation de la logique d'authentification
    if username == "hiba" and password == "123456":
        return True
    else:
        return False

# Fonction principale pour la page de login et la redirection
def main():
    # Styles CSS pour la page de login
    st.markdown(
        """
        <style>
        .stApp {
            background: url("https://source.unsplash.com/1600x900/?nature,water") no-repeat center center fixed;
            background-size: cover;
        }
        .login-box {
            background: rgba(255, 255, 255, 0.8);
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
            margin-top: 100px;
        }
        .login-title {
            font-size: 2rem;
            color: white;
            font-weight: bold;
            text-align: center;
            margin-bottom: 2rem;
        }
        .login-input {
            font-size: 1.2rem;
            padding: 0.5rem;
            margin: 0.5rem 0;
            width: 100%;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .login-button {
            background-color: #4B0082;
            color: white;
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 5px;
            font-size: 1.2rem;
            cursor: pointer;
            width: 100%;
            margin-top: 1rem;
        }
        .login-button:hover {
            background-color: #3A0066;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">Login Page</div>', unsafe_allow_html=True)

    username = st.text_input('Username', key='username', placeholder='Enter your username', help='Enter your username here')
    password = st.text_input('Password', type='password', key='password', placeholder='Enter your password', help='Enter your password here')

    if st.button('Login', key='login'):
        if authenticate(username, password):
            st.success('Logged In as {}'.format(username))
            # Redirection vers app.py avec les paramètres de session
            st.session_state.logged_in = True
        else:
            st.error('Invalid Username or Password')

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
