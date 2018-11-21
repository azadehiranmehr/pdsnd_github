import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city= input("please entyer a city among chicago, new york city or washington: ")
        city=city.lower()
        if (city=='chicago') | (city=='new york city') | (city=='washington') :
            break
        else:
            print("please enter a correct city!")

    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
       month=input("please input month among first six month of the year or all for all first six month: ")
       month=month.lower()
       if month in months:
          break
       else:
          print("you entered wrong month!!!")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday','tuesday', 'wednesday','thursday','friday','saturday','sunday','all']
    while True:
         day= input("please enter day of the week or all to select all 7 days : ")
         day=day.lower()
         if day in days:
            break
         else:
            print("you entered wrong day!!!")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start month:', popular_month)

    # TO DO: display the most common day of week
    # extract day from the Start Time column to create a day column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # find the most popular day
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start day:', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Popular Start Station:', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('Most Popular End Station:', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['popular station']=df['Start Station']+' and '+df['End Station']
    print('Most Popular Start and End Station:',  df['popular station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print(' Total Trip Duration is:',  total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print(' Average Trip Duration is:',  mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    size_user_type=df.groupby(['User Type']).size()
    print('Count of user type is :\n',  size_user_type)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_size=df.groupby(['Gender']).size()
        print('Count of gender is:\n',  gender_size)
    else:
        print('Gender is not available for this city')



    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        earliest=df['Birth Year'].sort_values().dropna().iloc[0]
        print()
        print('earliest year of birth is: \n',  earliest)
        most_recent=df['Birth Year'].sort_values().dropna().iloc[-1]
        print()
        print('most recent year of birth is: \n',  most_recent)
        most_common_year=df['Birth Year'].mode()[0]
        print()
        print('most common year of birth is: \n',  most_common_year)
        print()
    else:
        print('No birth day data for this city')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_rows(df):
    """Displays rows of dataframe (raw data )"""
    i=0
    while i < len(df):
       print('data', df.iloc[i:i+5])
       answer=input("Do you want to see 5 more rows? Enter yes or no.\n ")
       if answer.lower()=='yes':
            i=i+5
       else:
            break











def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.shape)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ans=input("Do you want to see raw data for this city? Enter yes or no.\n ")
        if ans.lower()=='yes':
            show_rows(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
