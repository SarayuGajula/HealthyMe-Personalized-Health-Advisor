% HealthyMe: Personalized Health Advisor 

% Facts: Example inputs for reasoning
age(30). % User's age
bmi(28). % Body mass index
exercise(hours_per_week, 2). % Hours of weekly exercise
diet(unhealthy). % Dietary habits (healthy/unhealthy)
sleep(hours_per_night, 6). % Hours of nightly sleep
water_intake(liters_per_day, 1.5). % Daily water intake in liters
stress_level(high). % Stress levels (low/medium/high)
chronic_condition(hypertension). % Chronic conditions (if any)

% BMI categories
bmi_category(underweight) :- bmi(B), B < 18.5.
bmi_category(normal) :- bmi(B), B >= 18.5, B =< 24.9.
bmi_category(overweight) :- bmi(B), B >= 25, B =< 29.9.
bmi_category(obese) :- bmi(B), B >= 30.

% Exercise sufficiency
sufficient_exercise :- exercise(hours_per_week, H), H >= 3.

% Sleep sufficiency
sufficient_sleep :- sleep(hours_per_night, H), H >= 7.

% Water intake sufficiency
sufficient_water :- water_intake(liters_per_day, W), W >= 2.

% Stress impact
stress_impact(low) :- stress_level(low).
stress_impact(moderate) :- stress_level(medium).
stress_impact(high) :- stress_level(high).

% Chronic illness management
chronic_impact(low) :- \+chronic_condition(_).
chronic_impact(high) :- chronic_condition(hypertension); chronic_condition(diabetes).

% Overall health risk assessment
health_risk(low) :- 
    bmi_category(normal),
    sufficient_exercise,
    sufficient_sleep,
    sufficient_water,
    stress_impact(low),
    chronic_impact(low).

health_risk(moderate) :- 
    bmi_category(overweight);
    \+sufficient_exercise;
    \+sufficient_sleep;
    \+sufficient_water;
    stress_impact(moderate).

health_risk(high) :- 
    bmi_category(obese);
    stress_impact(high);
    chronic_impact(high).

% Recommendations based on health risk
recommendation("Maintain your healthy lifestyle and habits!") :- health_risk(low).
recommendation("Improve your sleep, exercise, or water intake to lower your risk.") :- health_risk(moderate).
recommendation("Seek immediate medical advice to manage your health risks.") :- health_risk(high).

% Debugging support
debug_info :-
    write("Age: "), age(Age), write(Age), nl,
    write("BMI: "), bmi(BMI), write(BMI), nl,
    write("Exercise Hours: "), exercise(hours_per_week, EH), write(EH), nl,
    write("Sleep Hours: "), sleep(hours_per_night, SH), write(SH), nl,
    write("Water Intake: "), water_intake(liters_per_day, WI), write(WI), nl,
    write("Stress Level: "), stress_level(SL), write(SL), nl,
    (chronic_condition(CC) -> write("Chronic Condition: "), write(CC), nl ; write("No Chronic Conditions"), nl).
