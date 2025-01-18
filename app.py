import os
import streamlit as st
import subprocess

def query_prolog(file_name, query):
    prolog_path = "/opt/homebrew/bin/swipl"  # Ensure this is correct
    process = subprocess.Popen(
        [prolog_path, '-s', file_name, '-g', query, '-t', 'halt'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f"Prolog error: {stderr.decode('utf-8')}")
    return stdout.decode('utf-8')

def main():
    st.title("HealthyMe: Personalized Health Advisor")
    st.write("Provide your health information below:")

    # Check if Prolog file exists
    if not os.path.exists("healthyme.pl"):
        st.error("Prolog file 'healthyme.pl' is missing.")
        return

    # Collect inputs
    sleep_hours = st.number_input("Enter hours of sleep per night:", min_value=0, max_value=24, step=1)
    exercise_hours = st.number_input("Enter hours of exercise per week:", min_value=0, max_value=168, step=1)

    if st.button("Get Recommendation"):
        try:
            recommendation = query_prolog("healthyme.pl", f"recommendation(X, {sleep_hours}, {exercise_hours}).")
            st.write("Health Recommendation:", recommendation)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
