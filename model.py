# %%
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# %%
df = pd.read_csv('avg_wage.csv')
df.head()

# %%
# get all the columns except the last one
X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values

# %%
X

# %%
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create an instance of the LinearRegression model
regressor = LinearRegression()

# Fit the model to the training data
regressor.fit(X_train, y_train)

# Predict the target values for the test data
y_pred = regressor.predict(X_test)

# Evaluate the model performance by comparing the predicted and actual target values
print("R-squared:", regressor.score(X_test, y_test))

# Save the model
import pickle
pickle.dump(regressor, open('model.pkl', 'wb'))


# %%
# get the formula for the model
print(regressor.coef_)

# get the intercept for the model
print(regressor.intercept_)

# %%
# get a scatter plot of the actual and predicted values
import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

# %%
# get mse
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(mse)
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))


