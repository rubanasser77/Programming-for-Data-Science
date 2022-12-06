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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('ENTER THE CITY: ')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ("CHOOSE BETWEEN chicago, new york city OR washington: ").lower()


    # get user input for month (all, january, february, ... , june)
    month = input('ENTER MONTH: ').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input('ENTER MONTH january, february, ... , june : ').lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('ENTER DAY : ').lower()


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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month = df['Month'].value_counts().idmax()
       print("The most common month is {}".format(common_month))
      seperator("-")

    # display the most common day of week
    common_day = df['Day'].value_counts().idmax()
        print("The most common day is {}".format(common_day))
        seperator("-")

    # display the most common start hour
     common_hour = df['Hour'].value_counts().idmax()
        print("The most common hour is {}".format(common_hour))
        seperator("-")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idmax()
    print("The most commonly used start station is {}.".format(common_start_station))
    seperator("-")

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idmax()
    print("The most commonly used end station is {}.".format(common_end_station))
    seperator("-")

    # display most frequent combination of start station and end station trip
 most_Station= df.groupby(['Start Station' , 'End Station']).count()
    print("The most frequent combination of start is {} ,and of end is {}.".format(most_Station.idmax()[0][0], most_Station.idmax()[0][1]))
   seperator("-")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total of travel time is {:,.0f} seconds.".format(total_travel))
   
    print("In minutes = {:,.2f}".fromat(total_travel/60))
    print("In hours = {:,.2f}".fromat(total_travel/60/60))
    print("In days = {:,.2f}".fromat(total_travel/60/60/24))
    seperator("-")

    # display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print("The mean of travel time is {:,.2f} seconds.".fromat(travel_mean))
   
    print("In minutes = {:,.2f}".fromat(mean_travel/60))
    print("In hours = {:,.2f}".fromat(mean_travel/60/60))
    print("In days = {:,.2f}".fromat(mean_travel/60/60/24))
    seperator("-")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
   user_type = df["User Type"].value_counts()
    print("Displaying the counts of user types: \n")
    for k, v in user_type.iteritems():
       print("{:10} : {:,}".format(k,v))
    seperator("-")

    # Display counts of gender
     if "Gender" in df.columns:
        gender = df["Gender"].value_counts()
        print("Displaying the counts of gender: \n")
        for k, v in gender.iteritems():
           print("{:7} : {:,}".format(k,v))
        seperator("-")

    # Display earliest, most recent, and most common year of birth
    #1st earliest year of birth
    if "Birth Year" in df.columns:
      earliest_year = df["Birth Year"].min()
      print("The earliest year of birth is {:,0f}.".format(earliest_year))
      if earliest_year < 1900
      print("oops!! Looks like some one entered their date of birth incorrectly.")
    seperator("-")
  
   #2nd the most recent year of birth
   recent_year = df["Birth Year"].max()
   print("The most recent year of birth is {:,0f}.".format(recent_year))
    if recent_year > 2011
      print("oops!! Looks like some one entered their date of birth incorrectly.")
    seperator("-")
   
    #3rd the most common year of Birth
    common_year = df["Birth Year"].value_counts().idmax()
    print("The most common year of Birth is {:0f}".format(common_year))
    seperator("-")
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
