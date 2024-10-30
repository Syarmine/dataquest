We'll now implement the k-nearest neighbor algorithm for multiple features.

The only change we need to make is to our distance calculation. As we discussed on the fourth screen, the Euclidean distance for 
n
 features is calculated as:

$distance = \sqrt{(\Chi_1 - \gamma_1)^2 + (\Chi_n - \gamma_n)^2}$

Note that for each _i_ in {1,…,n}, 
- $\Chi_i$ is the value for a feature for one observation, and 
- $\gamma_i$ is the value for the same feature for another observation.

We'll modify our `knn()` function to account for this and select the following features for the model:

- `age`
- `campaign`
- `marital_married`
- `marital_single`

The training and test sets have already been defined in the code editor.

## Instructions
1. Create a function `knn()` that has the following parameters:
    - `features`: the list of features we want to use to calculate the distance.
    - `single_test_input`: a data point from the test set.
    - `k`: the number of neighbors.
2. Inside the function:
    - Calculate the Euclidean distance between the `single_test_input` and every observation in `X_train` for the given features. Save the distances in a new column, `distance`, in `X_train`.
    - For the k rows in `distance` with the smallest distance values, identify the most common label for the same rows in `y_train`. Save the label to the variable `prediction`.
    - Return `prediction`.
3. Call the function, `knn()` with the following arguments:
    - `features = ["age", "campaign", "marital_married", "marital_single"]`.
    - For `single_test_input`, select a random observation from `X_test`.
    - `k = 3`.
4. Print the output of the above step.
5. Use `knn()` for every row in `X_test`. Store the predictions in a new column, `predicted_y`, in `X_test`. Use the same arguments for `k` and `features` as above.
6. Compare `predicted_y` to `y_test` and calculate the number of correct predictions.
7. Calculate and print the accuracy of the model.