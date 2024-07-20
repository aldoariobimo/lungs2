import streamlit as st

def calculate_lung_cancer_score(age, gender, smoke, asbestos, family, alcohol):
    """
    This function calculates the Lung Cancer Risk based on the input parameters.
    """
    # Calculate age score based on given ranges
    if age < 25:
        age_score = 1
    elif 30 <= age <= 50:
        age_score = 2
    else:
        age_score = 3

    # Sum up the scores
    score = age_score + gender + smoke + asbestos + family + alcohol

    # Calculate the final score as a percentage
    final_score = (score / 8) * 100
    return final_score

st.title('Kanker Paru Detektor')
st.write('Nindya Maritza Sulistyowati E13.2022.00197')

age = st.slider('Age', 0, 100, 30)
gender = st.selectbox('Gender', [('Male', 0), ('Female', 1)])
smoke = st.selectbox('Smoke', [('No', 0), ('Yes', 1)])
asbestos = st.selectbox('Exposure to asbestos', [('No', 0), ('Yes', 1)])
family = st.selectbox('Family history of lung cancer', [('No', 0), ('Yes', 1)])
alcohol = st.selectbox('Alcohol consumption', [('No', 0), ('Yes', 1)])

if st.button('Calculate Score'):
    score = calculate_lung_cancer_score(age, gender[1], smoke[1], asbestos[1], family[1], alcohol[1])
    st.write('The Lung Cancer Risk is: {:.2f}%'.format(score))

    if score < 40:
        st.write('Low Risk Lung Cancer')
    elif 40 <= score <= 60:
        st.write('Medium Risk Lung Cancer')
    else:
        st.write('High Risk Lung Cancer')
