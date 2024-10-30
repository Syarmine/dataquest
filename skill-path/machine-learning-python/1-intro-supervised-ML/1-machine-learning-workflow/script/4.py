# --- continue from 2.py ---

#Import the train_test_split function from the sklearn.model_selection module.
from sklearn.model_selection import train_test_split

#Store the feature columns in the variable X.
X = cancer_df.drop(["target"], axis=1)

#Store the target column in the variable y.
y = cancer_df["target"]

#Call the train_test_split() function and pass the following parameters to it:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state = 417)