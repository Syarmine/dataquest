# Evaluating The Model
On the previous screen, we implemented the algorithm and used it to classify a sample input from the test set.

We'll now evaluate our model's performance by calculating how accurately it is able to correctly classify a given value. We can calculate the accuracy by comparing how many predictions the model gets correct compared to the total number of predictions.

$accuracy \% = \frac{number\ of\ correct\ predictions}{total\ number\ of\ predictions} \times 100$
$

In order to do that, we'll classify every data point in our test set and compare the predictions to the actual labels for those data points.

## Instructions
1. Use knn() for every row in X_test. Store the predictions in a new column, age_predicted_y, in X_test. Use the same arguments for knn() as before:
    - feature = "age".
    - k = 3.
2. Compare predicted_y to y_test and calculate the number of correct predictions.
3. Calculate and print the accuracy of the model.
Repeating the steps above with feature = "campaign", create a new column in X_test called campaign_predicted_y.