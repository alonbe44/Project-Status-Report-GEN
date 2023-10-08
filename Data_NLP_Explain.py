#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from transformers import pipeline


import pandas as pd
import numpy as np
import shap
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from data_Visualization import mp

# sentiment_analysis = pipeline("sentiment-analysis")
# result = sentiment_analysis("I love using Hugging Face Transformers!")
# print(result)
# # Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM


# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

# Encode and classify a text
text = "Hugging Face Transformers is awesome!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits



# df = pd.DataFrame.from_dict(mp)
# # Create a synthetic dataset (replace with your data)
# data = pd.DataFrame({
#     'DEP': df['DEP'].values,
#     'Project_Description': df['project name'].values,
#     'Resource_Allocation': 2,  # 2 Resource for each project
#     'Project_Complexity':  [9 if dep == 'OS' else 6 for dep in df['DEP'].values],
#     'Project_Duration': df['Duration'].values
# })
# # Convert department (DEP) to numerical values
# data['DEP'] = pd.factorize(data['DEP'])[0]
#
# # Split the data into training and test sets
# X = data.drop(columns=['Project_Duration', 'Project_Description'])
# y = data['Project_Duration']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Train a RandomForestRegressor model
# model = RandomForestRegressor(random_state=42)
# model.fit(X_train, y_train)
#
#
#
# # Calculate feature importance
# feature_importance = model.feature_importances_
# print("Feature Importance:")
# for feature, importance in zip(X.columns, feature_importance):
#     print(f"{feature}: {importance:.2f}")
#
# # Explain an individual prediction using SHAP values
# explainer = shap.Explainer(model, X_train)
# # Explain predictions for the entire test set using SHAP values
# shap_values = explainer(X_test)
#
# # Visualize feature importance using summary plot for all test instances
# # shap.summary_plot(shap_values, X_test)
#
#
#
#
# # Assuming you have a list of top features affecting project duration and their SHAP values
# top_features = {'DEP','Resource_Allocation','Project_Complexity'}
# shap_values=shap_values.values[1]
# # Create explanations for each top feature
# explanations = []
# for feature, shap_value in zip(top_features, shap_values):
#     shap_magnitude = abs(shap_value)
#     if shap_value > 0:
#         explanation = f"An increase in '{feature}' tends to lead to longer project durations, with a magnitude of {shap_magnitude:.2f}."
#     elif shap_value < 0:
#         explanation = f"A decrease in '{feature}' tends to lead to longer project durations, with a magnitude of {shap_magnitude:.2f}."
#     else:
#         explanation = f"'{feature}' has a neutral effect on project duration."
#     explanations.append(explanation)
#
# # Combine explanations into a single text
# text_explanation = "\n".join(explanations)
#
# # Provide contextual information
# context_information = """
# It's important to consider these factors when planning and managing projects.
# Allocating sufficient resources can help expedite project completion,
# while understanding and addressing project complexity is crucial for accurate scheduling and resource planning.
# """
#
# # Combine explanations and context information
# full_explanation = text_explanation + context_information
#
# # Print or use the 'full_explanation' as needed
# print(full_explanation)
#
#
#
#
