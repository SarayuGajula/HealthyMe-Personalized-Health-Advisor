import subprocess

def query_prolog(query):
    """Run a Prolog query using the s(CASP) system."""
    process = subprocess.Popen(['swipl', '-s', 'healthyme.pl', '-g', query, '-t', 'halt'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return f"Error: {error.decode()}"
    return output.decode()

def get_user_input():
    """Gather user inputs dynamically."""
    print("Welcome to HealthyMe: Personalized Health Advisor\n")
    
    age = input("Enter your age: ")
    bmi = input("Enter your BMI: ")
    exercise = input("Enter hours of exercise per week: ")
    diet = input("Enter your diet type (healthy/unhealthy): ")
    sleep = input("Enter hours of sleep per night: ")
    
    # Write inputs to the Prolog knowledge base
    with open("healthyme_inputs.pl", "w") as input_file:
        input_file.write(f"age({age}).\n")
        input_file.write(f"bmi({bmi}).\n")
        input_file.write(f"exercise(hours_per_week, {exercise}).\n")
        input_file.write(f"diet({diet}).\n")
        input_file.write(f"sleep(hours_per_night, {sleep}).\n")
    
    print("\nCalculating your personalized health advice...\n")
    recommendation = query_prolog('recommendation(X)')
    print(recommendation)

if __name__ == "__main__":
    get_user_input()
