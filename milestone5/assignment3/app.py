import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load Titanic dataset and model
data = pd.read_csv('titanic.csv')
model = joblib.load('titanic_model.pkl')

st.title("Titanic Survival Prediction & Data Exploration")

menu = st.sidebar.selectbox("Select Mode", ["Prediction", "Data Exploration"])

if menu == "Prediction":
    st.subheader("Passenger Information Input")
    
    col1, col2 = st.columns(2)
    
    with col1:
        pclass = st.selectbox('Pclass (Passenger Class)', [1, 2, 3], help="1 = 1st class, 2 = 2nd class, 3 = 3rd class")
        sex = st.selectbox('Sex', ['male', 'female'], help="Select passenger gender")
        age = st.slider('Age', 0, 100, 30, help="Passenger age in years")
        sibsp = st.slider('Siblings/Spouses aboard', 0, 8, 0)
    
    with col2:
        parch = st.slider('Parents/Children aboard', 0, 6, 0)
        fare = st.slider('Fare', 0.0, 600.0, 32.2)
        embarked = st.selectbox('Port of Embarkation', ['S', 'C', 'Q'], help="S = Southampton, C = Cherbourg, Q = Queenstown")

    sex_map = {'male': 0, 'female': 1}
    embarked_map = {'S': 0, 'C': 1, 'Q': 2}
    
    input_df = pd.DataFrame({
        'Pclass': [pclass],
        'Sex': [sex_map[sex]],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Fare': [fare],
        'Embarked': [embarked_map[embarked]]
    })
    
    if st.button('Predict Survival'):
        prediction = model.predict(input_df)[0]
        if prediction == 1:
            st.success("🎉 The passenger is likely to survive.")
        else:
            st.error("☹️ The passenger is unlikely to survive.")
            
elif menu == "Data Exploration":
    st.subheader("Explore Titanic Dataset")
    st.dataframe(data.head())
    
    feature = st.selectbox("Histogram Feature", ['Age', 'Fare', 'SibSp', 'Parch'], help="Select feature for histogram")
    bins = st.slider("Number of bins", 5, 50, 20, help="Adjust histogram bins")

    fig, ax = plt.subplots()
    ax.hist(data[feature].dropna(), bins=bins, color='skyblue', edgecolor='black')
    ax.set_xlabel(feature)
    ax.set_ylabel("Count")
    ax.set_title(f"Histogram of {feature}")
    st.pyplot(fig)
    
    st.write("Scatter Plot")
    x_feature = st.selectbox("X-axis", ['Age', 'Fare', 'SibSp', 'Parch'], key='xaxis')
    y_feature = st.selectbox("Y-axis", ['Age', 'Fare', 'SibSp', 'Parch'], key='yaxis')
    
    fig2, ax2 = plt.subplots()
    ax2.scatter(data[x_feature], data[y_feature], alpha=0.5)
    ax2.set_xlabel(x_feature)
    ax2.set_ylabel(y_feature)
    ax2.set_title(f"{y_feature} vs {x_feature}")
    st.pyplot(fig2)
