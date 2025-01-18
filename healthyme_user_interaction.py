import subprocess

def query_prolog(file_name, query):
    """Run a Prolog query using the s(CASP) system."""
    process = subprocess.Popen(['swipl', '-s', file_name, '-g', query, '-t', 'halt'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return f"Error: {error.decode()}"
    return output.decode()

def save_user_inputs(file_name, user_data):
    """Save user inputs to a Prolog file."""
    with open(file_name, "w") as file:
        for fact in user_data:
            file.write(fact + "\n")

def collect_user_inputs():
    """Collect user inputs dynamically."""
    print("Welcome to HealthyMe: Personalized Health Advisor\n")
    age = input("Enter your age: ")
    bmi = input("Enter your BMI: ")
    exercise = input("Enter hours of exercise per week: ")
    diet = input("Enter your diet type (healthy/unhealthy): ")
    sleep = input("Enter hours of sleep per night: ")
    water = input("Enter liters of water intake per day: ")
    stress = input("Enter your stress level (low/medium/high): ")
    chronic = input("Do you have a chronic condition? (e.g., hypertension/diabetes) Leave blank if none: ")

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
    
    return user_data

def main():
    """Main function to run the enhanced HealthyMe advisor."""
    inputs_file = "user_inputs.pl"
    prolog_file = "healthyme_expanded.pl"
    
    # Collect user inputs and save them
    user_data = collect_user_inputs()
    save_user_inputs(inputs_file, user_data)
    
    print("\nAnalyzing your health data...\n")
    recommendation = query_prolog(inputs_file, "recommendation(X).")
    if "Error" in recommendation:
        print("An error occurred:", recommendation)
    else:
        print("Health Recommendation:", recommendation)

    print("\nDebugging Information:")
    debug_info = query_prolog(inputs_file, "debug_info.")
    print(debug_info)

if __name__ == "__main__":
    main()
