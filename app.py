import os
import subprocess
import streamlit as st

# Explicitly set the path to swipl
SWIPL_PATH = "/opt/homebrew/bin/swipl"  # Replace with the output from `which swipl`

def query_prolog(file_name, query):
    try:
        # Run the Prolog query using subprocess
        process = subprocess.Popen(
            [SWIPL_PATH, '-s', file_name, '-g', query, '-t', 'halt'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        if error:
            return f"Error: {error.decode()}"
        if not output.strip():
            return "No recommendation generated. Check your Prolog logic."
        return output.decode().strip()
    except Exception as e:
        return f"Exception: {str(e)}"

def main():
    st.title("HealthyMe: Personalized Health Advisor")
    st.write("Provide your health information below:")

    # Collect user inputs
    age = st.number_input("Enter your age:", min_value=0, step=1)
    bmi = st.number_input("Enter your BMI:", min_value=0.0, step=0.1)
    exercise_hours = st.number_input("Enter hours of exercise per week:", min_value=0, step=1)
    diet_type = st.selectbox("Select your diet type:", ["healthy", "unhealthy"])
    sleep_hours = st.number_input("Enter hours of sleep per night:", min_value=0, step=1)
    water_intake = st.number_input("Enter liters of water intake per day:", min_value=0.0, step=0.1)
    stress_level = st.selectbox("Select your stress level:", ["low", "medium", "high"])
    chronic_condition = st.text_input("Enter any chronic condition (or leave blank):")

    # Submit button
    if st.button("Get Recommendation"):
        # Write user inputs to a Prolog file
        user_inputs = [
            f"age({age}).",
            f"bmi({bmi}).",
            f"exercise({exercise_hours}).",
            f"diet({diet_type}).",
            f"sleep({sleep_hours}).",
            f"water_intake({water_intake}).",
            f"stress({stress_level}).",
        ]
        if chronic_condition:
            user_inputs.append(f"chronic_condition({chronic_condition}).")
        
        with open("user_inputs.pl", "w") as file:
            file.write("\n".join(user_inputs))

        # Query Prolog for recommendation
        recommendation = query_prolog("healthyme.pl", "recommendation(X).")
        st.subheader("Health Recommendation:")
        st.write(recommendation)

if __name__ == "__main__":
    main()
