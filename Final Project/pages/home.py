import streamlit as st
from PIL import Image

def app():
    st.markdown("""

    # Text Analysis Web Application
    
    A Text Based Emotion Detection Automated Solution.  
    

    


    """)

    # image = Image.open('images/speech-text.png')
    image = Image.open('images/nlp1.png')
    st.image(image)

    st.markdown("""
   Emotion detection (ED) is a branch of sentiment analysis that deals with emotion extraction and analysis. 
   Sentiment Analysis aims to detect positive, neutral, or negative feelings from text, whereas Emotion Analysis aims to detect and recognize
    types of feelings through the expression of texts, such as anger, neutral, fear, happiness, sadness, and surprise. 
    """)

    

    st.markdown("""
    ## Contact us Via 
    * [Varun's Linkedin](https://www.linkedin.com/in/akash9varun/)
    * [Trishwanth's Linkedin](https://www.linkedin.com/in/akash9varun/)

    """)