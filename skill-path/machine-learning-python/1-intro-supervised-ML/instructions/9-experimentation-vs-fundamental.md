## Experimentation vs Fundamental

Our accuracy increased!

By just playing around with a couple of parameters, we were able to improve how our model performed. Our model is now better at predicting whether a patient has breast cancer.

It's really amazing how we managed to:

- Train a randomly selected model from scikit-learn.
- Experiment with a few of its parameters, and
- Get it to predict, with reasonably high accuracy, whether a patient has breast cancer.

We managed to do that without understanding:

- What the model actually does.
What the different parameters of that model are for.
What most of the dataset's features are.
While there is clearly a case to be made for the value of being able to quickly iterate and experiment with different models, we can't lose sight of the bigger picture either.

Remember we set max_iter to 3500? If we'd set it to 3000 instead, our accuracy would have dropped precipitously!

What would we have done in that situation? There are 12 parameters in scikit-learn's LinearSVC.

- How many of those parameters could we experiment with?
- What possible permutations and combinations of values could we have tried?
- What happens if we lower C instead of increasing it? What does C actually do in the model? Would lowering it make our model perform better on the test set?
- If we were to get more data with some new features, would our selected values yield similar results or would we have to go through the process all over again?
- What if we had millions of observations instead? Could we afford to run any model any number of times on such a large dataset? Which model would even be suitable for such a large dataset?
- What if we kept trying random models with random parameters, but there was an issue with the dataset itself? What if we could've identified whether some of the features were more relevant or vice-versa? Would that have helped us more than trying all those models, or would that have made things worse for us?

Experimentation and iteration through direct application have their place in the field of machine learning. However, trying to achieve good-to-great results given certain constraints is a challenging task. Blind experimentation won't get us far.

Understanding the fundamentals or understanding how a machine learning algorithm works "under the hood" opens up additional insights to rely on when trying to answer some of the questions above. It can allow us to experiment and iterate from an informed perspective.

In the next few lessons, we'll learn from that other perspective. We'll learn about a different machine learning algorithm, implement it from scratch, and then use scikit-learn again.