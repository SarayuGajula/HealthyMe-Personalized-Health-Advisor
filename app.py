import os
import streamlit as st
import subprocess

def query_prolog(file_name, query):
    """Run a Prolog query using the s(CASP) system."""
    try:
        process = subprocess.Popen(['swipl', '-s', file_name, '-g', query, '-t', 'halt'],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            return f"Error: {error.decode()}"
        return output.decode()
    except Exception as e:
        return f"Exception: {str(e)}"

def main():
    # Debug: Check files in the current directory
    st.write("Files in the current directory:")
    st.write(os.listdir("."))

    # Streamlit UI
    st.title("HealthyMe: Personalized Health Advisor")
    st.write("Provide your health information below:")

    # Collect inputs from the user
    age = st.number_input("Enter your age:", min_value=0, step=1)
    bmi = st.number_input("Enter your BMI:", min_value=0.0, format="%.2f")
    exercise = st.number_input("Enter hours of exercise per week:", min_value=0, step=1)
    diet = st.selectbox("Select your diet type:", ["healthy", "unhealthy"])
    sleep = st.number_input("Enter hours of sleep per night:", min_value=0, step=1)
    water = st.number_input("Enter liters of water intake per day:", min_value=0.0, format="%.2f")
    stress = st.selectbox("Select your stress level:", ["low", "medium", "high"])
    chronic = st.text_input("Enter any chronic condition (or leave blank):")

    if st.button("Get Recommendation"):
        # Save user inputs to a temporary Prolog file
        user_inputs = [
            f"age({age}).",
            f"bmi({bmi}).",
            f"exercise(hours_per_week, {exercise}).",
            f"diet({diet}).",
            f"sleep(hours_per_night, {sleep}).",
            f"water_intake(liters_per_day, {water}).",
            f"stress_level({stress})."
        ]
        if chronic:
            user_inputs.append(f"chronic_condition({chronic}).")

        with open("user_inputs.pl", "w") as file:
            file.write("\n".join(user_inputs))

        # Query Prolog
        recommendation = query_prolog("healthyme.pl", "recommendation(X).")
        if "Error" in recommendation:
            st.error(recommendation)
        else:
            st.success(f"Health Recommendation: {recommendation}")

if __name__ == "__main__":
    main()
