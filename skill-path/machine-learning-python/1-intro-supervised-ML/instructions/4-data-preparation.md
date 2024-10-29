In the previous screens, we came across a couple of concepts:

- Training a model on our data.
- Using the model to make a prediction on unseen data.

The data that we use to train our model is called training data, a training set or a training dataset.

The unseen data, as the name suggests, is data that our model hasn't seen before. The model has not trained on that data and will only use that data and predict a label for it.

This unseen data is called test data, a test set or a test dataset. It's used to evaluate the model's performance. Since we don't have any additional data to use as a test set, we can randomly select a small set of observations from our original dataset and set it aside. That way, we can train our model on the rest of the dataset and test it later using the test set.

Next we'll prepare our training and test datasets using scikit-learn's train_test_split function. There will be two stages to this process:

1. The function expects the feature columns and the target column as inputs. If we look at the examples in the documentation, those two are passed to the function as X and y. As we work with the library more, we'll notice this convention often--the input data is usually stored in X and the target variable is stored in y. We'll follow the same convention here.

2. The function will split the dataset into a training set and a test set based on a proportion that we decide. Usually, the test set's size is about 15 to 20 percent of the dataset's. Different factors, such as the original dataset's size, can also play a part in deciding that percentage.

- The function splits the data randomly into each set. We'll learn why that's relevant in a future lesson.
- The output of train_test_split() is a list containing 4 elements:
    - The training set features.
    - The test set features.
    - The training set labels.
    - The test set labels.

Note that there can be, and usually are, multiple steps as part of preparing the data. For example, we might have to clean our data before we train a model on it. We'll cover this topic in more detail in a later lesson.

### Instructions

1. Import train_test_split from sklearn.model_selection
2. Store the feature columns in the variable X.
Note that X should not contain the target column.
3. Store the target column in the variable y.
4. Call the train_test_split() function and pass the following parameters to it:
    - X
    - y
    - test_size=0.15
    - random_state=417
        - Since the data is split randomly, setting a random_state to a specific number allows us to reproduce the same results every time we run the code.
5. Save the output of the function to the variables X_train, X_test, y_train, y_test.