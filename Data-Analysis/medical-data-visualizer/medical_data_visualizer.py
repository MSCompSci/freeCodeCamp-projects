import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(r'medical_examination.csv')
# Add 'overweight' column
df['overweight'] = 0
df.loc[df['weight'] / ((df['height']/100)**2) >25, 'overweight'] = 1




# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df["cholesterol"] == 1, 'cholesterol'] = 0
df.loc[df["cholesterol"] > 1, 'cholesterol'] = 1
df.loc[df["gluc"] == 1, 'gluc'] = 0
df.loc[df["gluc"] > 1, 'gluc'] = 1





# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    
    

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(["cardio","variable","value"], as_index=True)["value"].count()).rename(columns={"value":"total"}).reset_index()
    
    
    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x="variable", y="total", col="cardio", hue="value", data=df_cat, kind="bar").fig



    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
          (df['height'] >= df['height'].quantile(0.025))&
          (df['height'] <= df['height'].quantile(0.975))&
          (df['weight'] >= df['weight'].quantile(0.025))&
          (df['weight'] <= df['weight'].quantile(0.975))
              ] 

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib 
    with sns.axes_style("dark"):
      fig, ax = plt.subplots(figsize=(8, 8))
    

    # Draw the heatmap with 'sns.heatmap()'
    ax = ax = sns.heatmap(corr, mask=mask, vmax=1, square=True, annot=True, fmt=".1f",linewidths=.5,cmap="BuPu")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
