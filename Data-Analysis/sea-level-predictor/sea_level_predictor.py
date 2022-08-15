import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress



def draw_plot():
    # Read data from file
    df = pd.read_csv(r'epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(data=df,x='Year',y='CSIRO Adjusted Sea Level',color='blue',s=5)
    

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    line1 = linregress(x, y)

    xExtended = pd.Series(range(df['Year'].min(), 2051))

    pre = line1.intercept + line1.slope*xExtended
    plt.plot(xExtended,pre, color="green", label="Fitted line")



    # Create second line of best fit
    x2 = df[df['Year']>=2000]['Year']
    y2 = df[df['Year']>=2000]['CSIRO Adjusted Sea Level']
    xExtended2 = pd.Series(range(2000, 2051))
    line2 = linregress(x2, y2)
    pre2 = line2.intercept + line2.slope*xExtended2
    plt.plot(xExtended2,pre2, color="red", label="Fitted line")



    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
