# predict_stock_py
This is a submission for the "Predicting Stock Prices challenge" by @Sirajology on [Youtube](https://www.youtube.com/watch?v=SSu00IRRraY).


## Overview
The python script "predict_stock.py" does the following:

1. Asks the user for a stock quote from NASDAQ (e.j: AAPL, FB, GOOGL)
2. Uses Tweepy to retrieve tweets about that stock.
3. Uses TextBlob to determine if the majority of the tweets are positive using sentiment analisys.
4. If the last is True, downloads the last year of prices for that stock, and trains a neural net with that data to predict the price for tomorrow.

The folder "demo" contains a test training 'Table 3' to the same network that is used to predict the price.


## Dependencies
* numpy (http://www.numpy.org/)
* tweepy (http://www.tweepy.org/)
* textblob (https://textblob.readthedocs.io/en/dev/)
* requests(http://docs.python-requests.org/en/master/)
* keras(https://keras.io/) Runs with [TensorFlow](https://www.tensorflow.org/) or [Theano](http://deeplearning.net/software/theano/), so you will need one of them.


# Usage
Install all the necesary dependencies.
Then just run:
```
python predict_stock.py
```
It will ask you for a NASDAQ quote, e.j: AAPL, then if the sentiment is positive and the stock you entered exists it will start training the network and give you a result.


# Credits
Credits to [Siraj](https://github.com/llSourcell) and to this [blog post](http://machinelearningmastery.com/time-series-prediction-with-deep-learning-in-python-with-keras/).


# Disclaimer
Do not use this code to invest in the stock market, if you are interested in stocks start by reading "The Intelligent Investor" by Benjamin Graham.
