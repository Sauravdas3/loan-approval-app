import streamlit as st
import pandas as pd
import pickle


# Load the pre-trained machine learning model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)
def main():
    st.title("Loan Eligibility Prediction")


    # Collect user input
    age = st.number_input("age", min_value=12)
    income = st.number_input("income", min_value=0)
    credit_score = st.slider("credit_Score", min_value=300, max_value=900, value=700)


    # Create a DataFrame with user input
    user_data = pd.DataFrame({
        "age": [age],
        "income": [income],
        "credit_score": [credit_score]

    })

    # Preprocess user data (if needed)
    # ...
    # Display prediction result

    if st.button("Predict Loan Eligibility"):
        # Make loan eligibility prediction
        prediction = model.predict(user_data)[0]

        # Display prediction result
        if prediction == 1:
            st.success("Congratulations! Your loan is approved.")
        else:
            st.error("Sorry, your loan application is rejected.")
if __name__ == "__main__":
    main()