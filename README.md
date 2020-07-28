# AmazonReviewsClassified

This py file is the python file i used to vectorize a database that had a text field in order to predict the score.
The ipython file further uses the created vectorized and filtered out file and performs various modelling tasks on it.

The actual database could not be uploaded as it is too large. You can download it from kaggle, where it is by the name of "AMAZON FINE FOOD REVIEWS".

I have used w2v and only done vectorization for 1000 data pts as the file was too big for it.
The features are of 50 dimensions

A csv file is added for someone to see how the data will look after vectorization.

Out of the classification models used, random forest performed best with almost 98% accuracy and a good confusion matrix.
We will thus use this classifier to predict the future data.
