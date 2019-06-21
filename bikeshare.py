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
    while True:
        try:
            city = str(input("Please select which city would you like to search? Chicago, New York City, or Washington? ")).lower()
            if (city != 'chicago') and (city != 'new york city') and (city != 'washington'):
                print('Your finding is not in the database, please enter a valid city name!')
                continue
            else:
                break
        except ValueError:
            print("You input is invalid, please try again.")
            continue

    while True:
        try:
            month = str(input("Which month would you want to access? ")).lower()
            if (month != 'all') and (month != 'january') and (month != 'february') and (month != 'march') and (month != 'april') and (month != 'may') and (month != 'june'):
                print('Your finding is not in the database, please enter a valid month!')
                continue
            else:
                break
        except ValueError:
            print("You input is invalid, please try again.")
            continue

    while True:
        try:
            day = str(input("Which day of week would you want to access? ")).lower()
            if (day != 'all') and (day !='monday') and (day !='tuesday') and (day !='wednesday') and (day !='thursday') and (day !='friday') and (day !='saturday') and (day !='sunday'):
                print('Your finding is not in the database, please enter a valid day of week!')
                continue
            else:
                break
        except ValueError:
            print("You input is invalid, please try again.")
            continue

    print('-' * 40)
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
    # Open the csv file
    df = pd.read_csv(CITY_DATA[city])
     # Convert the Start Time column to datetime
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
    else:
        df

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    else:
        df
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # find the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month of travel:', most_common_month)

    # TO DO: display the most common day of week
    # extract day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # find the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week of travel:', most_common_day_of_week)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common start hour of travel:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start Station'] + ' to ' + df['End Station']
    most_fre_comb = combination.mode()[0]
    print('The most frequent combination of start station and end station trip is {}.'.format( most_fre_comb))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is {} seconds.'.format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time is {} seconds.'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_type_counts = df['User Type'].value_counts()
    print('Counts of user types: \n',User_type_counts)

    # TO DO: Display counts of gender
    try:
        User_gender_counts = df['Gender'].value_counts()
        print('Counts of user gender: \n',User_gender_counts)
    except KeyError:
        print('This file does not contain gender column!')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        print('The earliest year of birth is {}.'.format(earliest_birth_year))

        most_recent_birth_year = int(df['Birth Year'].max())
        print('The most recent year of birth is {}.'.format(most_recent_birth_year))

        most_common_birth_year = int(df['Birth Year'].mode())
        print('The most common year of birth is {}.'.format(most_common_birth_year))
    except KeyError:
        print('This file does not contain birth year column!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#get raw data function
def get_raw_data(df):
    i = 0
    while True:
        try:
            get_data = str(input("Would you like to view individual data? Yes/No ")).lower()
            if get_data == 'yes':
                print(df.iloc[[i, i + 1, i + 2, i + 3, i + 4]])
                i += 5
                continue
            elif get_data != 'no':
                print('invaid input, please enter again!')
                continue
            else:
                break
        except ValueError:
            print("You input is invalid, please try again.")
            continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
