## Introduction to K-Nearest Neighbors


### Introduction to the Dataset
In the previous lesson, we looked at the machine learning workflow and trained a simple classifier to predict if a patient has breast cancer. We learned how we can quickly prototype a machine learning model and experiment with it to get reasonable results.

While there is a benefit to being able to quickly experiment and iterate, not understanding how the algorithm for a model actually works can impact the outcome of those random experiments.

In this lesson, we'll learn a different machine learning algorithm and implement it from scratch. We'll use it to build and train a classifier that can predict whether a bank customer will subscribe to a term deposit or not.

We'll use a modified version of the [Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/bank+marketing). It contains data on customers of a Portuguese banking institution that ran marketing campaigns to assess whether customers would subscribe to their product. The dataset consists of 21 columns, including the target variable:

- age: (numeric)
- job: type of job (categorical: 'admin','blue collar','entrepreneur','housemaid','management','retired','self employed','services','student','technician','unemployed','unknown')
- marital: marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
education: (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
- default: has credit in default? (categorical: 'no','yes','unknown')
- housing: has housing loan? (categorical: 'no','yes','unknown')
- loan: has personal loan? (categorical: 'no','yes','unknown')
- contact: contact communication type (categorical: 'cellular','telephone')
month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
- day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
- duration: last contact duration, in seconds (numeric).
- campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
- pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
previous: number of contacts performed before this campaign and for this client (numeric)
- poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')
- emp.var.rate: employment variation rate - quarterly indicator (numeric)
- cons.price.idx: consumer price index - monthly indicator (numeric)
- cons.conf.idx: consumer confidence index - monthly indicator (numeric)
euribor3m: euribor 3 month rate - daily indicator (numeric)
nr.employed: number of employees - quarterly indicator (numeric)
y: has the client subscribed a term deposit? (binary: 'yes','no')
Let's explore our dataset.

### Instructions
1. Read subscription_prediction.csv into a DataFrame banking_df.
2. Explore the dataset:
    - Look at the first few observations in the dataset.
    - Identify the number of categorical and numerical features in the dataset.
    - Print out the number of features and observations.
    - Calculate and print the number of missing values in each column.
    - Calculate and print the number of customers who subscribed to the term deposit and the number of customers who didn't.
    - Display the summary statistics for the dataset.