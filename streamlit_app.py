# streamlit_app.py
import streamlit as st
import requests
from bs4 import BeautifulSoup

# Streamlit App
def main():
    st.title("Automotive Data Explorer")

    # Define session_state to keep track of the user's progress
    if 'step' not in st.session_state:
        st.session_state.step = 'user_info'

    # User input fields
    name = st.text_input('Name')
    car_model = st.text_input('Car Model')
    make = st.text_input('Make')
    year = st.text_input('Year')
    mileage = st.text_input('Mileage')
    date_of_diagnosis = st.text_input('Date of Diagnosis')

    # Handle different steps
    if st.session_state.step == 'user_info':
        # Button to trigger diagnosis
        if st.button('Next - Choose Symptoms'):
            # Prepare user_info dictionary
            user_info = {
                'name': name,
                'car_model': car_model,
                'make': make,
                'year': year,
                'mileage': mileage,
                'date_of_diagnosis': date_of_diagnosis
            }

            # Display user_info for verification
            st.write('User Info:', user_info)

            # Simulate posting user_info to Flask /symptoms route
            response_symptoms = requests.post('http://localhost:3000/symptoms', data=user_info)

            # Parse HTML content from the Flask response
            soup = BeautifulSoup(response_symptoms.text, 'html.parser')

            # Update session_state to move to the next step
            st.session_state.step = 'symptoms'

    elif st.session_state.step == 'symptoms':
        # Display the symptoms form
        st.title("Choose Symptoms")
        # ... (your existing code for symptoms form)
        
        # Button to trigger diagnosis
        if st.button('Diagnose'):
            # Simulate fetching diagnosis results from Flask /explanation route
            response_diagnosis = requests.get('http://localhost:3000/explanation')

            # Parse HTML content from the Flask response
            soup_diagnosis = BeautifulSoup(response_diagnosis.text, 'html.parser')

            # Update session_state to move to the next step
            st.session_state.step = 'diagnosis'

    elif st.session_state.step == 'diagnosis':
        # Display diagnosis results
        st.title("Diagnosis Results")
        # ... (your existing code for displaying diagnosis results)

# Run the Streamlit app
if __name__ == "__main__":
    main()
