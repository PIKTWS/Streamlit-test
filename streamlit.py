import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle



pickle_in = open('logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)

st.sidebar.image("./pics/superai.png", caption=None, width=300, use_column_width=None, clamp=False, channels='RGB', output_format='auto')
st.sidebar.header('👉 SUPERAI2-1329 👈')
st.sidebar.header('Choose Prediction Model')

model_choice = st.sidebar.selectbox('Select Prediction Model', ['Diabetes Prediction','Other predictions'], key='1')

if model_choice == 'Diabetes Prediction':
    col1,col2,col3 = st.beta_columns(3)
    with col2:
        st.image("./pics/super_ai_logo.png", caption=None, width=200, use_column_width=None, clamp=False, channels='RGB',output_format='auto')
    st.title('🍄 Predition chance of diabetes 😱')
    name = st.text_input("Patient Name:")
    # pregnancy = st.number_input("No. of times pregnant: ")
    pregnancy = st.number_input("No. of times pregnant: ", min_value=0, max_value=10, value=0, step=1)
    # glucose = st.number_input("Plasma Glucose Concentration: ")
    glucose = st.slider( "Plasma Glucose Concentration: ", min_value=0.0 , max_value=250.0 ,value=121.0, step=0.1)
    # bp =  st.number_input("Diastolic blood pressure (mm Hg): ")
    bp = st.slider("Diastolic blood pressure (mm Hg): ", min_value=0.0 , max_value=130.0 ,value=69.0, step=0.1)
    # skin = st.number_input("Triceps skin fold thickness (mm): ")
    skin = st.slider("Triceps skin fold thickness (mm): ", min_value=0.0 , max_value=100.0 ,value=20.5, step=0.1)
    # insulin = st.number_input("2-Hour serum insulin (mu U/ml): ")
    insulin = st.slider("2-Hour serum insulin (mu U/ml): ", min_value=0.0 , max_value=200.0 ,value=80.1, step=0.1)
    # bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
    bmi = st.slider( "Body mass index (weight in kg/(height in m)^2): ", min_value=10.0 , max_value=50.0 ,value=32.0, step=0.1)
    dpf = st.slider( "Diabetes Pedigree Function:", min_value=0.05 , max_value=2.500 ,value=0.471876, step=0.001)
    age = st.slider( "Your Age: ", min_value=10 , max_value=99 ,value=30, step=1)

    submit = st.button('Predict')
    if submit:
            # prediction = classifier.predict([["pregnancy", "glucose", "bp", "skin", "insulin", "bmi", "dpf", "age"]])
            prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
            if prediction == 0:
                st.balloons()
                st.write("")
                st.success('Congratulation! ' + str(name) + '  You are not diabetic')
            else:
                st.error("Ohh  " + str(name) +"... We are really sorry to say but it seems like you are Diabetic. But don't worry, there's a cure.")
                st.info("Remember.  The sooner you know, the eaiser cure will be.")

