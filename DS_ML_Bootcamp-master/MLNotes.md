# Machine Learning Intro

Each Segment: 
##### Theory
##### Optional Reading
##### Python Implementation
##### Portfolio Exercise
##### Solution Walkthrough


### Supervised Learning
- Trained using **Labeled Examples** such as an input where the desired output is known
- Segment of text could have a label : Spam vs. Legit for an email
- Positive vs. Negative for a review
- Neural network receives a set of input data and what output it should produce. 
- Supervised learning is used to predict likely future events. 

#### Steps 
- Data Acquisition - Get your data
- Data Cleaning - clean and format so your neural net can process it
- Split data between test and training, use the training set to fit the model to the data, and then test it against test data. 
- Test the model and adjust the model parameters
- Deploy the model

### Data Sets
- Training data used to train the model params
- Validation Data used to determine what mdoel hyperparameters to adjust
- Test data used for final performance metrics.


### Evaluating Performance - Classification
- Accuracy = number of correct predictions made by the model divided by the total number of predictions. Accuracy is good to use when there are a roughly equal number of target class members, if you're trying to predict if somehting is a dog or a cat, its best when there are 50% of each in the test set.
- Recall = ability of a model to find all the relevant cases within a dataset, number of true positives divided by the number of true positives + false negatives
- Precision = ability of a classification model to identify only the relevant datapoints, the number of true positives divided by the number of true positives + false positives
- F1 Score = combination of precision and recall, harmonic mean of precision and recall. 

In classification, our model is either correct or incorrect. 

### Evaluating Performance - Regression
A model is trying to predict a continuous value.

- Accuracy / recall are not useful here

##### Example: lets predict the price of a house given features
#### Common metrics for regression:
- Mean Absolute Error = mean of the absolute value of errors, comparing our continuous value to the true y label
- Mean Squared Error = Mean of the squared errors, larger errors are noted more than with MAE, MSE is more popular
- Root Mean Square Error = Root of the mean of the squared errors = just the square root of MSE, most popular metric

#### Context is everything when evaluating performance.
try to compare your error metric to the average value of a label in your data set to get an intuition for the performance.








