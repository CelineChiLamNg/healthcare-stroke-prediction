# Stroke Prediction Dataset

## Objective

The dataset was downloaded from Kaggle, [Stroke_Prediction_Data](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
, on 10 September 2024. It will be used to predict whether a patient is likely
 <br> to get a stroke. <br>
The data contains 11 clinical features, like gender, age, smoking status, <br>
etc, that help describe each patient.<br><br>


## Technology Used
1. python
2. pandas
3. matplotlib
4. seaborn
5. sklearn
5. pipeline
6. random forest
7. xgboost
8. lightgbm
9. logistic regression
10. dummy classifier
11. SHAP


## Results
<i>Age, BMI and avg_glucose_level are most influential</i><br>
 1. Age <br>
   - It is visible how it has a much larger impact in general on younger 
   cases. This importance slowly reduced with age growing and increases 
   again for older cases. <br>
   - On younger cases, the impact is negative, pushing values towards no 
   stroke, 0. <br>
   - On older cases, the impact is positive, pushing values towards stroke, 
   1.<br><br>
2. BMI<br>
    - This feature seems to only have influence when bmi values are extreme,
     very low or very high. For values in the middle, it is not a huge 
     predictor.<br>
    - For all extreme bmi values, the impact is positive.<br><br>
3. Avg_glucose_level<br>
    - It is not clear if there is a consistent pattern on how this feature 
    affects predicted values. But the impact is in general higher for low 
    glucose level values.<br><br>
4. Other features<br>
    - The rest are categorical features. For most of them, a 0 in the 
    feature pushes the predicted value to 0 as well, vice-versa.<br>
    - Gender-male, ever married, and hypertension have a more distinct 
    influence on the prediction. <br>
    - Gender-male is the opposite of gender-female.<br>
    - 1 in never married are not influenced by this feature, whereas 0 is 
    pushed both to stroke and no stroke.<br>
    - 0 in hypertension is not influenced by this feature, whereas 1 in 
    hypertension is pushed towards both stroke and no stroke.<br>



## Instructions

In order to run the app on port 8000 please run in the terminal
```
uvicorn app:app --reload
```

and then the app is available on 
POST localhost:8000 with body: <br>
eg.
[
    1.0,
    2.0,
    3.0,
    4.0,
    5.0,
    6.0,
    7.0,
    8.0,
    9.0,
    10.0,
    11.0,
    12.0,
    13.0,
    14.0,
    15.0,
    16.0,
    17.0,
    18.0
]<br>
The model will return 0 or 1, for False or True.