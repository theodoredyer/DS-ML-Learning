# K-means clustering:
- Unsupervised clustering algorithm where we know how many clusters are appropriate
- Used to predict subgroups within a dataset
- Used for quickly predicting groupings in an unlabeled dataset
- Predicions based on the number of centroids present (K) and nearest mean values, given a Euclidian distance measurement between observations



### Keep in mind:
- Need to scale variables
- Look at scatterplot or data table to estimate the appropriate number of centroids to use for K parameter value

### Evaluating Results
- Recall = measure of the model's completeness
- Precision = measure of the model's relevancy
- High precision and high recall = highly accurate model results
- 0: for all points predicted to have a 0 label, 100% of the retreived instances were relevant (ex)


# Hierarchical Clustering
- Predict subgroups within data by finding the distance between each data point and its nearest neighbors, and then linking the most nearby neighbors
- To guess the number of subgroups, first look at a dendogram visualization of the clustering results
- Dendogram = tree graph that useful for visually displaying taxonomies, lineages, and relatedness
- Try every combination of params possible and use the one with most accurate results

### Clustering Parameters
- Distance metrics = euclidian, manhattan, cosine
- Linkage parameters = ward, complete, average

