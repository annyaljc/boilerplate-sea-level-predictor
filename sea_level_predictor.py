import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
        # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    print(df.head())
    plt.figure(figsize=(12,8))
    plt.scatter(x='Year',y='CSIRO Adjusted Sea Level',data=df)
    # The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.

    slope, intercept, r_value, p_value, std_err =linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Function to calculate the line of best fit
    def predict(x):
        return slope * x + intercept



    years_extended = np.arange(min(df['Year']), 2051)
    year_2050=2050
    sea_level_2050=predict(year_2050)
    plt.plot(years_extended, predict(years_extended), color='red')
    plt.scatter([year_2050], [sea_level_2050], color='green', marker='x', s=100, label=f'Prediction for 2050: {sea_level_2050:.2f} mm')
    plt.text(year_2050, sea_level_2050, f'  Prediction: {sea_level_2050:.2f} mm', color='green', verticalalignment='bottom')

        # Create scatter plot


    # Create first line of best fit


    # Create second line of best fit
    df_new=df[df['Year']>=2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
    def predict2(x):
        return slope2 * x + intercept2
    year_2050 = 2050
    sea_level_2050_2 = predict2(year_2050)

    # Generate years for plotting the new line of best fit (extend to 2050)
    years_extended2 = np.arange(2000, 2051)

    # Plot the new line of best fit
    plt.plot(years_extended2, predict2(years_extended2), color='red', label='New Line of Best Fit (2000 Onwards)')

    # Highlight predicted value for 2050
    plt.scatter([year_2050], [sea_level_2050_2], color='green', marker='x', s=100)
    plt.text(year_2050, sea_level_2050_2, f'  Prediction: {sea_level_2050_2:.2f} mm', color='green', verticalalignment='bottom')

    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()