# AmazonReviewsClassified

We have amazon reviews dataset which has text reviews of customers, that we will use as our xi and the score will be used for yi.
The .py file here does the cleaning and vectorization part while the modelling part is done in the ipython notebook.

The actual database could not be uploaded as it is too large. You can download it from kaggle, where it is by the name of "AMAZON FINE FOOD REVIEWS".
Dataset Link: https://www.kaggle.com/snap/amazon-fine-food-reviews
Related Article Link: http://i.stanford.edu/~julian/pdfs/www13.pdf

I have used w2v and only done vectorization for 5000 data pts as the time for vectorization grows very strongly with the number of rows.
The features are of 50 dimensions

A csv file is added for someone to see how the data will look after vectorization.

Out of the classification models used, random forest performed best with almost 98% accuracy and a good confusion matrix.
We will thus use this classifier to predict the future data.
