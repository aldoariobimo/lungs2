import streamlit as st
import pandas as pd

def calculate_lung_cancer_score(age, gender, smoke, asbestos, family):
    """
    This function calculates the Gupta Postoperative Respiratory Failure Risk based on the input parameters.
    """
    # The following is pseudo-code for calculating the score.
    # Replace with the actual calculation algorithm.

    score = 0
    score += age
    score += gender
    score += smoke
    score += asbestos
    score += family 

    return score

st.title('Kanker Paru detektor')
st.write('Nindya Maritza Sulistyowati E13.2022.00197')

age = st.slider('Age', 0, 100, 30)
gender = st.selectbox('Gender', [(0, 'Male'), (1, 'Female')])
smoke = st.selectbox('Smoke', [(0, 'No'), (1, 'Yes')])
asbestos = st.selectbox('Exposure to asbestos', [(0, 'No'), (1, 'Yes')])
family = st.selectbox('Family history of lung cancer', [(0, 'No'), (1, 'Yes')])

if st.button('Calculate Score'):
    score = calculate_lung_cancer_score(age, gender[0], smoke[0], asbestos[0], family [0])
    st.write('The Lung Cancer Risk is: ', score)