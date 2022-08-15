import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r'fcc-forum-pageviews.csv',index_col='date',parse_dates=True)


# Clean data
df = df[ (df['value']>=df['value'].quantile(0.025)) & 
          (df['value']<=df['value'].quantile(0.975)) ].reset_index()


def draw_line_plot():
    # Draw line plot
    fig = df.plot(x='date', y='value', 
                  color='red', figsize=(14,6), 
                  xlabel='Date',ylabel='Page Views',title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019'
                  ).figure
  




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    columns = ['Year','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    years = [2016, 2017, 2018, 2019]
    df_bar = pd.DataFrame(data=None,columns=columns)
    df_bar['Year'] = years

    df_x = df.groupby(pd.Grouper(key='date', freq='M')).mean().reset_index()

    

    for x in range(len(df_x)):
      df_bar.loc[ df_bar['Year']==int(df_x['date'][x].year) , columns[df_x['date'][x].month]] = df_x['value'][x]

    # Draw bar plot
    fig = df_bar.plot(x='Year',y=columns[1:], kind="bar",figsize=(8, 8),xlabel='Years',ylabel='Average Page Views').figure


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    #print(df_box)

    # Draw box plots (using Seaborn)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2)
    sns.set(rc={"figure.figsize":(15, 5)})
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0]).set(xlabel='Year',ylabel='Page Views',title='Year-wise Box Plot (Trend)')

    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1],order=months).set(xlabel='Month',ylabel='Page Views',title='Month-wise Box Plot (Seasonality)')





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
