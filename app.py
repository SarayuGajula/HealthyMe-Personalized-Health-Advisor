import os
import subprocess
import streamlit as st

# Updated query_prolog function
def query_prolog(file_name, query):
    """Run a Prolog query using the SWI-Prolog system."""
    try:
        process = subprocess.Popen(
            ['/opt/homebrew/bin/swipl', '-s', file_name, '-g', query, '-t', 'halt'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        if error:
            return f"Error: {error.decode()}"
        return output.decode()
    except Exception as e:
        return f"Exception: {str(e)}"

# Main Streamlit App
def main():
    st.title("HealthyMe: Personalized Health Advisor")
    st.write("Provide your health information below:")

    # Collecting user inputs
    age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
    bmi = st.number_input("Enter your BMI:", min_value=10.0, max_value=50.0, step=0.1, format="%.2f")
    exercise = st.number_input("Enter hours of exercise per week:", min_value=0, max_value=168, step=1)
    diet = st.selectbox("Select your diet type:", ["healthy", "unhealthy"])
    sleep = st.number_input("Enter hours of sleep per night:", min_value=0, max_value=24, step=1)
    water = st.number_input("Enter liters of water intake per day:", min_value=0.0, max_value=10.0, step=0.1)
    stress = st.selectbox("Select your stress level:", ["low", "medium", "high"])
    chronic = st.text_input("Enter any chronic condition (or leave blank):")

    # Save user inputs to Prolog file
    user_data = [
        f"age({age}).",
        f"bmi({bmi}).",
        f"exercise(hours_per_week, {exercise}).",
        f"diet({diet}).",
        f"sleep(hours_per_night, {sleep}).",
        f"water_intake(liters_per_day, {water}).",
        f"stress_level({stress})."
    ]
    if chronic:
        user_data.append(f"chronic_condition({chronic}).")

    inputs_file = "user_inputs.pl"
    with open(inputs_file, "w") as file:
        for fact in user_data:
            file.write(fact + "\n")

    # Analyze health data using Prolog
    if st.button("Get Recommendation"):
        st.write("Analyzing your health data...")
        recommendation = query_prolog("healthyme.pl", "recommendation(X).")
        if "Error" in recommendation or "Exception" in recommendation:
            st.error(f"An error occurred while processing your data.\n\n{recommendation}")
        else:
            st.success(f"Health Recommendation: {recommendation}")

        st.write("\nDebugging Information:")
        debug_info = query_prolog("healthyme.pl", "debug_info.")
        st.text(debug_info)

if __name__ == "__main__":
    main()
