# --- continue from 4.py ---
from sklearn.svm import LinearSVC

model = LinearSVC(penalty="l2", loss="squared_hinge", C=10, random_state=417)
model.fit(X_train, y_train)