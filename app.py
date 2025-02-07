

import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)


# Importation du module
from streamlit_option_menu import option_menu



import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")


import streamlit as st



# Using object notation
def accueil():
      st.sidebar.title("Bienvenu ", name)

# Using "with" notation
with st.sidebar:
    authenticator.login()




if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

# Création du menu qui va afficher les choix qui se trouvent dans la variable options
with st.sidebar:
   selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )    
add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
  
# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos":
    st.write("Bienvenue sur mon album photo")
# # ... et ainsi de suite pour les autres pages

# import pandas as pd
# import streamlit as st
# st.title('Bienvenue sur le site web de Sébastien')

# link='https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv'
# df=pd.read_csv(link, sep=",")
# pickup = df['pickup_borough'].unique()


# option=st.selectbox("Indiquez votre arrondissement de récupération",pickup)
# st.write('Tu as choisi :', option)

# image={'Brooklyn' : 'https://images.ctfassets.net/1aemqu6a6t65/68nkexvLlGiTxvxFvzoELk/68ee51265baad76b8d7f5ae8cd99bf2c/brooklyn-bridge-sunset-julienne-schaer.jpg',
#         'Manhattan' : 'https://media.istockphoto.com/id/946087016/fr/photo/vue-a%C3%A9rienne-du-lower-manhattan-new-york.jpg?s=612x612&w=0&k=20&c=UC9a3WcsVU-qRI70I1Y7G7_kznMidm6_9VrKAJA1pBg=',
#         'Bronx' : 'https://thegoodlife.fr/wp-content/thumbnails/uploads/sites/2/2016/03/TGL-P-022-188-V-H-06-tt-width-2000-height-1282-fill-0-crop-0-bgcolor-eeeeee.jpg',
#         'Queens' : 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4_S6_aNBwe0flIJUM7xFM216c7GiVXLwVvIiRLmPF7qicgnRC5UiKk7DCvVewzN_fqOHGwWLb_cWERBFLPcVsloBZPd_cM9C2mnwkLYLll7knOnRS6TVVJotcffBNyefU_-jRKkVUJyU7/s1600/Visiter-Queens-New-York.jpg',
#         }

# if option in image :
#         st.image(image[option])
# else : st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHRpdWhvajlncHgyaWF2Zm0xY2M3N3hzdnlsbXplZHZsMDgxbnlqaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/c20UV66B7zCWA/giphy.gif')


