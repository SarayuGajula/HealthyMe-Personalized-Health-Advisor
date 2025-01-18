% HealthyMe: Personalized Health Advisor

% Facts: User input (example data, replace with dynamic input as needed)
age(30).  % age of the user
bmi(25).  % body mass index of the user
exercise(hours_per_week, 2).  % weekly exercise in hours
diet(unhealthy).  % type of diet
sleep(hours_per_night, 6).  % nightly sleep in hours

% Rules for health assessment
% Assess BMI category
bmi_category(underweight) :- bmi(B), B < 18.5.
bmi_category(normal) :- bmi(B), B >= 18.5, B =< 24.9.
bmi_category(overweight) :- bmi(B), B >= 25, B =< 29.9.
bmi_category(obese) :- bmi(B), B >= 30.

% Exercise sufficiency
sufficient_exercise :- exercise(hours_per_week, H), H >= 3.

% Sleep sufficiency
sufficient_sleep :- sleep(hours_per_night, H), H >= 7.

% Overall health risk assessment
health_risk(low) :- bmi_category(normal), sufficient_exercise, sufficient_sleep.
health_risk(moderate) :- bmi_category(overweight); \+sufficient_exercise; \+sufficient_sleep.
health_risk(high) :- bmi_category(obese).

% Recommendation generation based on health risk
recommendation("Maintain your healthy habits!") :- health_risk(low).
recommendation("Consider improving your exercise and sleep routines.") :- health_risk(moderate).
recommendation("Seek professional advice to manage weight and health.") :- health_risk(high).
