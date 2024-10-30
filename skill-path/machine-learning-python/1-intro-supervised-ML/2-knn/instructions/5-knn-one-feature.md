Now that we have our training and test sets, we can implement our algorithm!

Before we begin, we need to select a distance metric to calculate the distance between observations.

One of the most common distance metrics is the Euclidean distance. The Euclidean distance between two observations (x1,...,xn) and (y1,...,yn) with n features can be calculated as:

$distance = \sqrt{(\Chi_1 - \gamma_1)^2 + (\Chi_n - \gamma_n)^2} $

Note that, for each _i_ in {1,…
n},

- $\Chi_i$ is the value for a feature for one observation, and
- $\gamma_i$ is the value for the same feature for another observation.

When we are working with only one feature, the above formula simplifies to:

$distance = \sqrt{(\Chi_1 - \gamma_1)^2} = |\Chi_1 - \gamma_1|$

We'll implement our algorithm with this distance metric. You're encouraged to learn about some of the other distance metrics that can be used as well:

- [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry)
- [Minkowski distance](https://en.wikipedia.org/wiki/Minkowski_distance)
- [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)

As per the algorithm, we'll calculate how far an unseen observation is from all the observations in the training data for a specific feature.

But wait a minute. We learned that a machine learning model is trained over some data and then the trained model can be used to classify unseen data. Why are we using an unseen observation to implement the k-NN algorithm? Aren't we training the model using unseen data?

K-nearest neighbors is a bit of a unique case. It works at the time of prediction and it doesn't technically have a "training phase." The model classifies every new input by comparing it to its neighbors. Those neighbors are from the training set.

As a result, the algorithm can be time-consuming depending on the number of observations and features in our dataset.

So why did we have to create a separate test set?

Even though there's no training phase, the algorithm does rely on an unseen observation to be able to make a prediction. In the next exercise, we'll use a random value from our test set to implement the algorithm.

Instructions

1. Create a function knn() that has the following parameters:
    - feature: the feature we want to use to calculate the distance.
    - single_test_input: a data point from the test set.
    - k: the number of neighbors.
2. Inside the function:
    - Calculate the Euclidean distance between the single_test_input and every observation in X_train for the given feature. Save the distances in a new column, distance, in X_train.
    - For the k rows in distance with the smallest distance values, identify the most common label for the same rows in y_train. Save the label to the variable prediction.
    - Return prediction.
3. Call the function, knn() with the following arguments:
    - feature = "age".
    - For single_test_input, select a random observation from X_test.
    - k = 3.
4. Print the output of the above step.
5. Print the true label (y_test) corresponding to the single_test_input used above.
    - Was the prediction correct?