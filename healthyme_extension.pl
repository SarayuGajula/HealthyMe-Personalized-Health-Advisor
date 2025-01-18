% Additional Rules for Chronic Illness Management and Dietary Recommendations

% Chronic illness management
% Example facts for chronic illnesses
chronic_condition(diabetes).
chronic_condition(hypertension).

% Rules for health advice based on chronic illnesses
health_advice("Follow a low-carb, balanced diet and monitor blood sugar levels regularly.") :- chronic_condition(diabetes).
health_advice("Reduce salt intake, exercise moderately, and monitor blood pressure.") :- chronic_condition(hypertension).

% Advanced dietary recommendations
% Example rules for personalized diet plans
diet_recommendation("Increase intake of fruits and vegetables, and reduce red meat consumption.") :- diet(unhealthy).
diet_recommendation("Maintain your current diet, ensuring it's rich in nutrients.") :- diet(healthy).

% Integration with the main system
personalized_advice(Advice) :-
    health_advice(HealthAdvice),
    diet_recommendation(DietAdvice),
    string_concat(HealthAdvice, " Additionally, ", Temp),
    string_concat(Temp, DietAdvice, Advice).
