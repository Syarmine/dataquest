#Import the necessary libraries.
import pandas as pd

#Import the load_breast_cancer function from the sklearn.datasets module.
from sklearn.datasets import load_breast_cancer

#Call the load_breast_cancer() function.
cancer_data = load_breast_cancer(as_frame = True)

#Save the output to the variable cancer_df.
cancer_df = cancer_data.data    

#Add a column called target to cancer_df and assign the target attribute from cancer_data to that column.
cancer_df['target'] = cancer_data.target 

#Look at the first few observations in the dataset.
print(cancer_df.head())

#Print out the shape of the dataset and confirm that the number of features and observations are same as the ones listed above.
print(f"Shape of the dataset: {cancer_df.shape}")

#Calculate and print the number of missing values in each column.
print(cancer_df.isna().sum())

#Calculate and print the number of patients with a benign tumor and the number of patients with a malignant tumor.
print(cancer_df['target'].value_counts())

#Display the summary statistics for the dataset.
print(cancer_df.head())

#Display the summary statistics for the dataset.
cancer_df.describe()
