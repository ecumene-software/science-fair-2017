from yt_articles import *
from tw_articles import *

import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from keras.layers.normalization import BatchNormalization
import timeit

model = Sequential()
model.add(Dense(output_dim=1000, input_dim=6, init="normal"))
model.add(BatchNormalization())
model.add(Dense(output_dim=900, activation='relu'))
model.add(Dense(output_dim=2048, activation='relu'))
model.add(Dense(output_dim=2))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

start = 0

#Case 1
X_test = np.array([[500000, 1000000, 10, 30, 200, 5]])
X_test = np.array([[500000, 1000000, 20, 60, 200, 5]])

#Case 2
X_test = np.array([[1000000, 5000000, 10, 30, 2000, 5]])
X_test = np.array([[1000000, 5000000, 20, 60, 2000, 5]])

#Case 3
X_test = np.array([[5000000, 1000000000, 10, 30, 3000, 5]])
X_test = np.array([[5000000, 1000000000, 20, 60, 3000, 5]])

def calcYTResponse():
    start = timeit.timeit()
    X = []
    Y = []

    for key, value in yt_namedrop.iteritems():
        X.append(key.to_arr())
        Y.append(value.to_arr())

    model.fit(np.array(X), np.array(Y), nb_epoch=150, batch_size=32, verbose=1)
    end   = timeit.timeit()

    print "Building YT Response... " + str(end - start)
    print model.predict(X_test)

def calcTWResponse():
    start = timeit.timeit()
    X = []
    Y = []

    for key, value in tw_namedrop.iteritems():
        X.append(key.to_arr())
        Y.append(value.to_arr())

    model.fit(np.array(X), np.array(Y), nb_epoch=150, batch_size=32, verbose=1)

    end   = timeit.timeit()
    print "Building Twitter Response... " + str(end - start)
    print model.predict(X_test)

calcYTResponse()

model = Sequential()
model.add(Dense(output_dim=1000, input_dim=6, init="normal"))
model.add(BatchNormalization())
model.add(Dense(output_dim=900, activation='relu'))
model.add(Dense(output_dim=2048, activation='relu'))
model.add(Dense(output_dim=2))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

calcTWResponse();
