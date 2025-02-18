import streamlit as st
import streamlit.components.v1 as components
import time
import datetime
import random
from PIL import Image



# Set page configuration once
st.set_page_config(page_title="Spline Design Viewer", layout="wide")

# App title
st.title("Hi, I am Streamlit Robot. Today is my birthday!")

col1, col2, col3, col4 = st.columns([1, 2, 1, 1])

# Spline 3D model iframe
with col2:
    spline_url = "https://my.spline.design/robotfollowcursorforlandingpage-a8ce559ec2b984ce43d73a7786dd8461/"
    components.html(f'<iframe src="{spline_url}" style="width:100%; height:386px; border:none; padding:20px;"></iframe>', height=355)

# Button to trigger celebrations
with col3:
    if st.button('Celebrate!'):
        st.snow()  # Snow effect
        time.sleep(2)  # Pause for effect
        st.balloons()  # Balloons effect

# Sidebar configuration and dynamic theme application
with st.sidebar:
    # Color picker for sidebar theme
    party_color = st.color_picker('Party Color', '#000000')  # Default black color

    # Dynamic CSS to update sidebar color
    st.markdown(
        f"""
        <style>
        .stSidebar > div:first-child {{
            background-color: {party_color} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Party settings and features
    st.write("## Party Settings")
    party_mode = st.checkbox("Activate Party Mode")
    if party_mode:
        st.markdown("### Let's get the party started!")
        music_on = st.checkbox("Play Music")
        if music_on:
            st.audio("https://www.bensound.com/bensound-music/bensound-happyrock.mp3")
    
    # Additional Fun Features
    st.write("## More Fun Stuff")
    if st.button('Get a Funny Quote'):
        funny_quotes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Did you hear about the mathematician who’s afraid of negative numbers? He'll stop at nothing to avoid them.",
            "Parallel lines have so much in common. It’s a shame they’ll never meet."
        ]
        st.write(random.choice(funny_quotes))
    
    fun_fact = st.button("Tell me a fun fact")
    if fun_fact:
        facts = [
            "A group of flamingos is called a 'flamboyance'.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are as much as 3000 years old and still preserved.",
            "Bananas are berries, but strawberries aren't."
        ]
        st.write(random.choice(facts))

    # Sliders for fun
    st.slider("Choose your fun level", min_value=1, max_value=100, value=50)

# Celebratory footer message
st.markdown("### 🎉🎈 Celebrate Good Times! 🎈🎉 -  2025 /test with Spline")
