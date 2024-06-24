import streamlit as st
import pandas as pd
import pokemon_api
import requests
import seaborn as sns
import matplotlib.pyplot as plt

if 'pokedict' not in st.session_state:
    st.session_state['pokedict'] = pokemon_api.get_pokedict()

if 'weights' not in st.session_state:
    st.session_state['weights'] = pokemon_api.get_weights()

st.title('1$^{st}$ Generation Pokémon Comparison Tool 🔮')

user_choices = st.multiselect("Choose your Pokémon!", options=st.session_state['pokedict'].keys(), max_selections=2)


col1, col2 = st.columns(2)
try:
    with col1:
        name_1, height_1, weight_1, n_moves_1, n_abilities_1, types_1, image_url_1, cry_1 = pokemon_api.get_details(st.session_state['pokedict'][user_choices[0]])
        sound_1 = requests.get(cry_1)
        st.image(image_url_1)
        st.header(f"You have chosen :blue[***{name_1.title()}***]")
        st.markdown(f"{name_1.title()} is a :blue[***{types_1.title()}***] type")
        st.audio(sound_1.content, format="audio/ogg")
        st.caption(f'Cry of {name_1}')
        st.divider()
except:
    pass
try:
    with col2:
        name_2, height_2, weight_2, n_moves_2, n_abilities_2, types_2, image_url_2, cry_2 = pokemon_api.get_details(st.session_state['pokedict'][user_choices[1]])
        sound_2 = requests.get(cry_2)
        st.image(image_url_2)
        st.header(f"You have chosen :red[***{name_2.title()}***]")
        st.markdown(f"{name_2.title()} is a :red[***{types_2.title()}***] type")
        st.audio(sound_2.content, format="audio/ogg")
        st.caption(f'Cry of {name_2}')
        st.divider()
except:
    pass



try:
    with col1:
        st.metric(label=f'Height \(m\)📏', value=height_1/10, delta=(height_1-height_2)/10)
        st.metric(label=f'Weight \(kg\) ⚖', value=weight_1/10, delta=(weight_1-weight_2)/10)
        st.metric(label='Number of Moves 🥋', value=n_moves_1, delta=n_moves_1-n_moves_2)
        st.metric(label='Number of Abilities 🧙‍♂️', value=n_abilities_1, delta=n_abilities_1-n_abilities_2)
except:
    pass
try:
    with col2:
        st.metric(label=f'Height \(m\)📏', value=height_2/10, delta=(height_2-height_1)/10)
        st.metric(label=f'Weight \(kg\) ⚖', value=weight_2/10, delta=(weight_2-weight_1)/10)
        st.metric(label='Number of Moves 🥋', value=n_moves_2, delta=n_moves_2-n_moves_1)
        st.metric(label='Number of Abilities 🧙‍♂️', value=n_abilities_2, delta=n_abilities_2-n_abilities_1)
except:
    pass


try:
    st.divider()
    st.header('Weight Analysis')
    sns.set_style("dark")
    fig, ax = plt.subplots()
    sns.kdeplot(x=st.session_state['weights'], ax=ax, color='green', fill=True)
    ax.axvline(x=weight_1/10, color='blue', linewidth=1, 
            label=f'{name_1.title()} ({weight_1/10} kg)')
    ax.axvline(x=weight_2/10, color='red', linewidth=1, 
            label=f'{name_2.title()} ({weight_2/10} kg)')
    ax.set_title('$1^{st}$ Generation Pokémon Weight Distribuion')
    ax.set_xlabel('Weight (kg)')
    ax.set_ylabel('Density')
    ax.set_xlim(0)
    ax.legend()
    st.pyplot(fig)
except:
    pass