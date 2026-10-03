from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[5],[10],[6],[20],[50],[25]])
y = [10,20,12,40,100,50]

model = LinearRegression()
model.fit(X,y)

num = [[7]]
prediction = model.predict(num)

