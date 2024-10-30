## Introduction to Machine Learning Workflow
Dataquest wants to figure out whether or not a new learner will complete a specific course. We are confident that the course has a good balance that allows a learner to understand any concept by applying it. Unfortunately, that doesn't always imply that everyone will complete a course.

So, how could we predict that a new learner will complete the course?

Let's say we've collected data for every current learner on the website. We know:

- How many lessons they've completed previously on the website.
- How many of the other courses they've completed.
- How many exercises they've successfully passed.
- How many hours they've spent on each individual lesson.
- Whether they've already completed the course.

Based on the data, we already know whether an existing learner has completed the course. Are there relevant details in the rest of the data that could help us find a pattern that relates a learner's actions on the website to the likelihood of their completing the course?

Maybe, upon exploring the data, we find that 90% of learners who completed the course:

Completed more than L lessons previously.
Spent more than H hours, on average, per lesson.
Passed more than E exercises.
Given these patterns, can we say that a new learner who satisfies the above criteria will complete that course also?

Well, we can't guarantee it. But, the likelihood of that happening might be high if the new learner satisfies the above rules. What if we learn something new from the data that changes that likelihood? It could get lower or higher.

We can't always identify these patterns one at a time, especially when we have lots of data. This is exactly where machine learning can help.

Instead of making decisions based on patterns identified from information we already have, we can use machine learning to do it for us.

The small set of rules or criteria we identified above is essentially what a machine learning model does without us explicitly programming those rules. We train the model so it learns to identify those patterns from the data on its own. We then use the model to predict something given a new, unseen, input. That "something" might seem a bit ambiguous, but what we want to predict depends on the intended outcome or task. In this and the next few courses, we will cover such tasks and learn machine learning models that can help us with those tasks.

What we learned above gives us a quick introduction to the machine learning workflow:

- Data Collection.
- Data Exploration and Wrangling.
- Data Preparation (Feature Engineering).
- Building and training a model.
- Evaluating the model performance.
- Fine-tuning the model.
- Evaluating the model performance.

![1.1-m736](..\images\1.1-m736.svg)

That might seem like a lot of steps and terminology! Some things might not be explicitly clear right away, but don't worry. Throughout this course, we will go through each step of the above workflow in more detail.

For the rest of this lesson, we will use a popular, python-based machine learning library called scikit-learn and learn more about this workflow. We'll also train a simple machine learning model to predict if a patient has breast cancer.

Please note that this lesson will focus on helping us familiarize with the workflow. Any concepts or terminology that might come across as confusing or challenging will be covered in varying depths across the remaining lessons and courses.