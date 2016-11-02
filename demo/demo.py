import numpy as np
from keras.models import Sequential
from keras.layers import Dense


# Teach "Table 3" to the network 
trainX = np.array([1, 2 ,3 ,4 ,  5 , 6 , 7,  8,  9, 10])
trainY = np.array([3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

model = Sequential()
model.add(Dense(8, input_dim=1, activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, nb_epoch=1200, batch_size=2, verbose=2)


# Predict  3x20, answer = 60
dataPrediction = model.predict(np.array([20]))
print int(dataPrediction[0][0]), '<--- Predicted number'
print '60 <-- Correct answer \n'

# Predict  3x25, answer = 75
dataPrediction = model.predict(np.array([25]))
print int(dataPrediction[0][0]), '<--- Predicted number'
print '75 <-- Correct answer \n'

# Predict  3x345, answer = 1035
dataPrediction = model.predict(np.array([345]))
print int(dataPrediction[0][0]), '<--- Predicted number'
print '1035 <-- Correct answer \n'

# Predict  3x2, answer = 6
dataPrediction = model.predict(np.array([2]))
print int(dataPrediction[0][0]), '<--- Predicted number'
print '6 <-- Correct answer \n'
