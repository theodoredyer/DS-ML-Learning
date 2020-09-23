### Descriptive Statistics
two types:
- Those that describe the values of observations in a variable (sum, median, mean, max)
- Those that describe a variable spread (std dev, variance, counts, quartiles)

Uses:
- Detecting outliers
- Planning data prep requirments for ML
- Selecting features for ML

### Summarizing Categorical Data
- Accepts only a limited and fixed number of values. 
- Each observation is assigned to a subgroup

### Crosstab
- A cross-tabulation of two or more features
- Default shows frequency counts for features


### Parametric Correlation Analysis
- Used to find correlation between linearly related continuous numeric variables
- Correlation does not imply causation. 
- Pearson Correlation Coefficient: R = 1 is strong positive relationship, 0 not linear correlated, -1 strong negative relationship. Assumes normally distributed data, continuous numeric, and linearly related vars
- Use Pearson correlation to uncover linear relationships between variables. 
- Don't use it to rule out possible nonlinear relationships between vars. 

### Nonparametric Correlation Analysis
- Used to find correlation between categorical, nonlinearly related, non-normally distributed variables
- Spearman's Rank and Chi tables. 
- Spearman's Rank = finds R correlation between variable-pairs of ordinal data type, variable pairs are then able to be ranked according to strength of correlation between them. Assumes variables are ordinal; numeric, but able to be ranked, assumes nonlinear, and non-normally distributed
- Chi-Square test. p < 0.05 = reject null hypothesis (variables are correlated) & p > 0.05 = accept null hypothesis (variables are independent)
- Use Chi square tables if variables are categorical or numeric, and we have binned numeric variables


### Transforming dataset distributions
- Important to scale data to ensure differing magnitude among variables doesn't produce erraneous results
- Normalization = putting each observation on a relative scale between 0-1
- Standardization = rescaling data so that it has a zero mean and unit variance
- Done with scikit-learn to scale, center, normalize, bin, and imputing


### Extreme Value Analysis

- Most ML methods assume that the data has been treated for outliers already
- Used to detect fraud, equipment faulure, etc


### Multivariate Outlier Detection
- Find outliers that only show up within combinations of observations from two or more different variables
