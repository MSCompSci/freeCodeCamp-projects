import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # Filtered data by men, selected age, calculated mean, rounded to 1 dec place
    average_age_men = round(df[df['sex']=='Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    #Selected by Bachelors, found total Bachelors with len(), divided total Bachelors by total education entries, multiplied by 100 to get %, and rounded to 1 dec place
    percentage_bachelors = round( ( len( (df[df['education']=='Bachelors']) ) / df['education'].count() ) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # Selected entries with B, M, and D degrees
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Selected entries without B, M, and D degrees using ~
    lower_education = df[~ df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    #Counted salaries higher than 50K in higher_education, divided by total higher_education entries, multiplied by 100 to get %, and rounded to 1 dec place
    higher_education_rich = round( ( higher_education['salary'].value_counts()['>50K'] / len(higher_education) ) * 100, 1)

    # Repeated above process for lower_education
    lower_education_rich = round( ( lower_education['salary'].value_counts()['>50K'] / len(lower_education) ) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    # Found min() in hours-per-week column
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum numbe.minr of hours per week have a salary of >50K?
    # Found value_counts() of min-work-hours in hours-per-week colunm
    num_min_workers = df['hours-per-week'].value_counts()[min_work_hours]

    # Found value_counts() of >50K salary in min workers, divided by total num_min_workers, multiplied by 100 to get %, and rounded to 1 dec place
    rich_percentage = round( df[ df['hours-per-week']==min_work_hours]['salary'].value_counts()['>50K'] / num_min_workers * 100,1)

    # What country has the highest percentage of people that earn >50K?
    # Made data frame of number of >50K salaries by country. Divided by data frame of number of entries per each native-country to calc earner percentage by country. Used idxmax() to return index/country name with max >50K earner percentage.
    highest_earning_country = (df[ df['salary']=='>50K']['native-country' ].value_counts() / df['native-country'].value_counts() ).idxmax()

    # Found earner percentage by country as above. Used max() to find maximum earner percentage. Multiplied by 100 and rounded to 1 dec place to format.
    highest_earning_country_percentage = round( (df[ df['salary']=='>50K']['native-country' ].value_counts() / df['native-country'].value_counts()).max() * 100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    # Created data frame from entries with >50K salary and India as native-country. Found number of entries per occupation using value_counts(). Used idxmax() to return index/title of most popular occupation
    top_IN_occupation = df[(df['salary']=='>50K') & (df['native-country']=='India')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
