import streamlit as st
import subprocess

def query_prolog(file_name, query):
    """Run a Prolog query using the s(CASP) system."""
    try:
        process = subprocess.Popen(
            ['swipl', '-s', file_name, '-g', query, '-t', 'halt'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        if error:
            return f"Error: {error.decode()}"
        return output.decode()
    except Exception as e:
        return f"Exception: {str(e)}"

def save_user_inputs(file_name, user_data):
    """Save user inputs to a Prolog file."""
    with open(file_name, "w") as file:
        for fact in user_data:
            file.write(fact + "\n")

def main():
    st.title("HealthyMe: Personalized Health Advisor")
    st.write("Provide your health information below:")

    # User inputs
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
    bmi = st.number_input("Enter your BMI:", min_value=0.0, max_value=100.0, value=22.0)
    exercise = st.number_input("Enter hours of exercise per week:", min_value=0, max_value=168, value=3)
    diet = st.selectbox("Select your diet type:", ["healthy", "unhealthy"])
    sleep = st.number_input("Enter hours of sleep per night:", min_value=0, max_value=24, value=7)
    water = st.number_input("Enter liters of water intake per day:", min_value=0.0, max_value=10.0, value=2.0)
    stress = st.selectbox("Select your stress level:", ["low", "medium", "high"])
    chronic = st.text_input("Enter any chronic condition (or leave blank):")

    # Submit button
    if st.button("Get Recommendation"):
        # Save user inputs to a Prolog file
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
        prolog_file = "healthyme.pl"
        save_user_inputs(inputs_file, user_data)

        # Query Prolog for a recommendation
        st.write("Analyzing your health data...")
        recommendation = query_prolog(prolog_file, "recommendation(X).")
        if "Error" in recommendation or "Exception" in recommendation:
            st.error("An error occurred while processing your data.")
            st.write(recommendation)
        else:
            # Display the health recommendation
            st.subheader("Health Recommendation:")
            st.write(recommendation)

        # Debugging information
        st.subheader("Debugging Information:")
        debug_info = query_prolog(prolog_file, "debug_info.")
        st.write(debug_info)

if __name__ == "__main__":
    main()
