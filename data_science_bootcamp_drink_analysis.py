#!/usr/bin/env python
# coding: utf-8

import pandas as pd

drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')

drinks.head(10)

drinks['continent'].value_counts(normalize=True)

import matplotlib.pyplot as plt


plt.scatter(x=drinks['beer_servings'],
            y=drinks['wine_servings'])


plt.figure(figsize=(15, 9))

plt.scatter(x = drinks['beer_servings'],
            y = drinks['wine_servings'])

plt.title('Compare Beer Servings to Wine Servings per Year by Country', fontsize=24)
plt.xlabel('Average Servings of\n Wine per Year', fontsize=20, rotation=0, ha='right')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16);

# Generate a scatterplot of beer_servings compared
# to wine_servings.
# Change the size of my image.
plt.figure(figsize=(15, 9))
plt.scatter(x = drinks['beer_servings'],
            y = drinks['wine_servings'])
# Add mean horizontal and vertical lines.
plt.hlines(y=drinks['wine_servings'].mean(),
           xmin=drinks['beer_servings'].min(), 
           xmax=drinks['beer_servings'].max(),
           lw=5,
           ls='--',
           color='red')
plt.vlines(x=drinks['beer_servings'].mean(),
           ymin=drinks['wine_servings'].min(), 
           ymax=drinks['wine_servings'].max(),
           lw=5,
           ls='--',
           color='red')
plt.title('Compare Beer Servings to Wine Servings per Year by Country',
          fontsize=24)
plt.xlabel('Average Servings of Beer per Year', fontsize=20)
plt.ylabel('Average Servings of\nWine per Year', fontsize=20, rotation=0, ha='right')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16);


# Use the machine learing package in Python: scikit-learn
from sklearn.linear_model import LinearRegression


# Step 1 to build a model: Instantiate model
model = LinearRegression()

# Step 2 to build a model: Fit model
model.fit(X = drinks[['beer_servings']],
         y = drinks['wine_servings'])

# Step 3 Generate predictions
predictions = model.predict(X = drinks[['beer_servings']])


# Generate a scatterplot of beer_servings compared
# to wine_servings.
# Change the size of my image.
plt.figure(figsize=(15, 9))
plt.scatter(x = drinks['beer_servings'],
            y = drinks['wine_servings'])
# plt.plot is the Line Plotting function.
plt.plot(drinks['beer_servings'],
         predictions,
         lw = 5, # lw means "line width"
         color = 'red')
plt.title('Compare Beer Servings to Wine Servings per Year by Country',
          fontsize=24)
plt.xlabel('Average Servings of Beer per Year', fontsize=20)
plt.ylabel('Average Servings of\nWine per Year', fontsize=20, rotation=0, ha='right')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16);
# plt.legend(fontsize=16)




