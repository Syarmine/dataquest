## Data Preparation

When we explored our data, we noticed that our target column, y, stores the labels as yes or no strings. While those are reasonable categories and we can continue working with them as is, we'll encode those strings as the numbers 0 for no and 1 for yes.

In the previous lesson, we learned how to split the dataset into a training and test set. Instead of using scikit-learn's train_test_split() function, we'll implement the split ourselves. We'll opt for a 85-15% split.

In order to split the dataset, we could take a direct approach of selecting the first N observations as the training set and the rest as the test set. But that poses a problem. We don't know how many observations of those N have a label of 0 and how many have a label of 1.

Let's say N = 100. What if, out of those 100, only 5 observations had a label of 1?

When the dataset is imbalanced, a machine learning model might struggle to accurately predict the labels because it hasn't had enough information to learn to distinguish between the classes. Ideally, the model should have enough data corresponding to each class so it can learn from the data effectively.

Even though our dataset has a reasonably balanced class distribution, we need to make sure that both the train and test sets have a similar percentage of subscribed customers.

The data collection process can also introduce certain biases. It's possible that the clients were selected in a specific order. 

For example, the collection process could've added the newest clients first. If we were to select the first N observations, we could be introducing bias into our model. That's why, when creating our training and test sets, randomly selecting observations is important, as it can help reduce any such biases.

Fortunately for us, this isn't complicated to implement in pandas.

### Instructions

1. Convert the yes values in the column y to 1 and no values to 0.

2. Using pandas.DataFrame.sample

    2.1. Randomly sample 85% of the dataset and assign to train_df.Set random_state to 417.

    2.2. Assign remaining rows to test_df.

3. Using pandas' value_counts() function, print the distribution of the labels as percentages for both train_df and test_df.

4. For train_df:

    4.1. Store the feature columns, excluding the target column, in the variable X_train.

    4.2. Store the the target column in the variable y_train.

5. For test_df:

    5.1. Store the feature columns, excluding the target column, in the variable X_test.

    5.2. Store the the target column in the variable y_test.