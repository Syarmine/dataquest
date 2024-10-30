## Supervised Machine Learning Classification

On the previous screen, we identified that our data has no missing values. We can, for now, work with the assumption that our data is clean and doesn't require further wrangling. That's always a dangerous assumption to make, but, for this lesson, our focus is on exploring the machine learning workflow from a broader perspective.

Our next step is to prepare our data before we input it to our model. However, we haven't really discussed what this model is.

Let's say we don't know what a giraffe looks like. Someone shows us a photo of a giraffe and we are able to identify some features that we think are unique to a giraffe. The next time we see a photo of a giraffe, even if it's a completely different one than before, we are highly likely to know that it's a giraffe. Our innate pattern-matching abilities could fail us, and we might confuse it for an ostrich just because of the long neck. But that's unlikely.

![3.1-m736](..\images\3.1-m736.png)

We were supplied with a label, along with a set of features, and our brains learned to associate that label with those features. The next time we saw a similar set of features, we were able to predict the correct label. That's the intuition behind the subset of machine learning we'll learn about in this course--supervised machine learning.

It's supervised because our model learns from existing data and the corresponding labels. There are usually two types of labels that we encounter:

- Continuous labels.
    - For example, we could be working with a dataset that contains features that describe different types of cars, and the labels could be the price of those cars. Our model would then learn to predict the price of a car, given those features as input.

- Categorical labels.
    - Our breast cancer dataset has only two labels--benign and malignant, or 0 and 1. Each observation is categorized by its own label or class.
If the label or target we want to predict is a categorical value, we call it a classification task. The model, a classifier, will try to classify a given set of inputs into a category. There are other types of machine learning models that can be used for different kinds of tasks. We'll learn about those later.

So, what exactly does the model learn from the data?

This is dependent on the machine learning algorithm we end up using for our model. Throughout this course, we will cover several algorithms that will answer that question for us. But, intuitively, think of our dataset as a bunch of points on a chart:

![3.2-m736](..\images\3.2-m736.svg)

The points on the charts above are our features in a two-dimensional space. This space is called a **feature space** and the colors represent the labels. The line that we see is a     **decision boundary** and it divides the feature space into two. Points on one side of the boundary belong to one class, and points on the other side of the boundary belong to the other class.

That decision boundary is our classifier. Since we only have two labels, it's called a **binary classifier**. If we had more labels, it would be a **multi-class classifier**.

![3.3-m736](..\images\3.3-m736.svg)


If we had more features, we would have an n-dimensional space and the decision boundary would be a hyperplane instead of a line.

But where does that line come from?

We know that a line or a curve can be defined using a parametric equation. That's what the model tries to learn - the parameters of that equation. The model estimates those parameters from the data, and those estimated parameters define the decision boundary.

Now that we have a better idea of what kind of machine learning task we're carrying out, let's prepare our data so that we can then train a model on it