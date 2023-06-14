import streamlit as st
import pickle 
import numpy as np
import time

def load_model():
    with open('model_pickle', 'rb') as f:
        data = pickle.load(f)
    return data

model = load_model()

def show_prediction():
    st.title("Heart Failure Prediction :heart:")
    st.header("Fill the Form to check your Heart Health !!")
    st.divider()
    #inputs of the user
    age = st.number_input('Enter your Age:',10,110,10)

    gender = int(st.radio('Enter your Gender:',('Male','Female'))=='Female')
    #print(gender)

    x = st.selectbox('Select the type of Chest Pain you have:',['None','TA: Typical Angina Pain','ATA: Atypical Angina Pain','NAP: Non-Anginal Pain', 'ASY: Asymptomatic'])
    if x=="TA: Typical Angina Pain":
        chestpain = 0
    elif x=="ATA: Atypical Angina Pain":
        chestpain = 1
    elif x=="NAP: Non-Anginal Pain":
        chestpain = 2
    else:
        chestpain =3

    RestingBP = st.number_input("Enter your Resting BP [mm Hg]:",60,160,60)

    cholesterol = st.number_input("Enter your serum Cholesterol [mm /dl]:",60,320,60)

    fasting_bs = int( (st.slider("Enter your Fasting Blood Sugar:",60,220,0)>120)==1)

    x = st.select_slider('Select the type of REsting ECG :',('LVH','Normal','ST'))
    if x=="LVH":
        restingECG = 0
    elif x=="Normal":
        restingECG = 1
    elif x=="ST":
        restingECG = 2

    maxHR = st.number_input("Enter your Maximum Heart Rate:",80,210,80)

    exercise_angina = int(st.radio('Do you have Exercise Angina:',('Yes','No'))=='Yes')

    old_peak = st.selectbox('Select value of Old Peak:',[0.0,0.5,1.0,1.5,2.0,2.5,3.0])

    x = st.select_slider("Select ST_slope:",['Down','Flat','Up'])
    if x=="Flat":
        ST_slope = 0
    elif x=="Down":
        ST_slope = -1
    elif x=="Up":
        ST_slope = 1

    if st.button("Predict"):
        X =np.array([[age,gender,chestpain,RestingBP,cholesterol,fasting_bs,restingECG,maxHR,exercise_angina,old_peak,ST_slope]])
        prediction = model.predict(X)
        st.subheader(f'{prediction[0]}')
 
show_prediction()


