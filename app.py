import streamlit as st 
import pickle

scaler = pickle.load(open('scaler.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('IRIS Classifier')

input_sepal_length = st.number_input("Enter sepal length (cm)")
input_sepal_width = st.number_input("Enter sepal width (cm)")
input_petal_length = st.number_input("Enter petal length (cm)")
input_petal_width = st.number_input("Enter petal width (cm)")
input_Data = [[
        input_sepal_length,
        input_sepal_width,
        input_petal_length,
        input_petal_width
    ]]
if st.button("Predict"):
        scaler_input = scaler.transform(input_Data)

        result = model.predict(scaler_input)
        if result == 0:
            st.header('Setosa')
        elif result==1:
            st.header('Versicolor')
        else:
            st.header('Virginica')
            
