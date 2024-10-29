## Data Collection and Exploration

On the previous screen, we learned what machine learning is and about the machine learning workflow. Let's put what we learned into action!

We'll build a model that predicts whether a patient has breast cancer. We'll start with the data.

![2.1-m736](..\images\2.1-m736.svg)

While it's possible, it's not always feasible to collect our own data. Fortunately, there are a lot of publicly available datasets that we can freely access and work with, depending on what kind of problem we want to solve.

We'll work with the [Breast Cancer Wisconsin (Diagnostic) Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)). The scikit-learn library stores several datasets, including [this breast cancer dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset), and makes it convenient for us to load and work with them.

On the first screen, we looked at what kind of data could be collected by a company like Dataquest:

How many lessons students have completed on the website.
How many courses they've completed so far.
How many exercises they've successfully passed.
How many hours they've spent on each lesson.
Each of the above is called a feature. They all describe or are a property of our data. When we work with tabular data, each column name corresponds to a feature -- except one:

Whether or not a learner has already completed the course.
The column corresponding to the above is called the target variable because that's what we want our model to predict. That's our target.

Every row for the above would contain information related to an individual learner. Each of these rows is called an observation or a feature vector. It's an n-dimensional vector of features.

Let's look at the dataset we'll be working with. The link to our dataset provides us with the following information:

There are a total of 30 attributes, or 30 features.
There are a total of 569 instances or observations.
There are two classes in the target variable:
WDBC-Malignant
WDBC-Benign
The above two classes, or labels, tell us whether a patient has a benign or a malignant tumor. For every observation, there's a corresponding class or label in our data.

Let's load in our dataset using scikit-learn's load_breast_cancer function. The function will return an object with several attributes, a couple of which we will utilize:

data stores the data points.
target stores the value 0 if the tumor is benign or 1 if the tumor is malignant.
Instructions
Import the following libraries:

pandas as pd.
From sklearn.datasets import load_breast_cancer
Call the load_breast_cancer() function.

2.1 Pass the parameter as_frame to the function and set it to True.

This will return the data attribute as a pandas' DataFrame and the target attribute as a Series.
2.2 Save the output to the variable cancer_data.

To a variable cancer_df assign the data attribute from cancer_data.

Add a column called target to cancer_df and assign the target attribute from cancer_data to that column.

Explore the dataset:

Look at the first few observations in the dataset.
Print out the shape of the dataset and confirm that the number of features and observations are same as the ones listed above.
Calculate and print the number of missing values in each column.
Calculate and print the number of patients with a benign tumor and the number of patients with a malignant tumor.
Display the summary statistics for the dataset.