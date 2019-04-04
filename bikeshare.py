import pandas as pd
import numpy as np
import time

CITY_DATA = {'chicago':'chicago.csv',
             'washington':'washington.csv',
             'new_york':'new_york_city.csv'}
#Giving csv file's to their respective cities.

def get_filters():
    """
    Asks the user to specify a city, month, and day and returns specified filter.
    Returns:
        (str) city - name of the city to filter by
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    months = ['january','february','march','april','may','june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    print("Hello..!! Let's explore some US bikeshare data! \nWhich city you want to see data for Chicago, New York, or Washington?")

    city = input()
    city_name = city.lower().replace(' ','_')
    
    while 1:
        if city_name not in CITY_DATA:
            #To filter the input entered by the user 
            print("Entered city is invalid. should be one of chicago, washington or new york! enter again..")
            city = input()
            city_name = city.lower().replace(' ','_')
        else: 
            break
    print("\n")

    print("Would you like to filter data by month, day, both, or not at all? Type 'none' for no time filter.")
    choice_data = ['month','day','both','none']
    data_choice = input()
    choice = data_choice.lower()
    
    while 1:
        if choice not in choice_data:
        #To filter the input entered by the user
            print("Entered choice is invalid. should be one of month, day, both or none..enter again!")
            data_choice = input()
            choice = data_choice.lower()
        else:
            break
    print("\n")

    if choice == 'month':
        print("Which month? January, February, March, April, May, June")
        month = input()
        month = month.lower()
        day_of_week = 'all'
        
        while 1:
            if month not in months:
                print("Entered choice is invalid..should be one of January, February, March, April, May, June..enter again!")
                month = input().lower()
            else:
                break
        print("\n")
        
    elif choice == 'day':
        print("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ")
        day_of_week = input().lower()
        month = 'all'
        
        while 1:
            if day_of_week not in days:
                print("Entered choice is invalid..should be one of Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday..enter again!")
                day_of_week = input().lower()
            else:
                break
        print("\n")
        
    elif choice == 'both':
        print("Which month? January, February, March, April, May, June")
        month = input()
        month = month.lower()
        
        while 1:
            if month not in months:
                print("Entered choice is invalid..should be one of January, February, March, April, May, June..enter again!")
                month = input().lower
            else:
                break
        print("\n")
        
        print("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ")
        day_of_week = input().lower()
        
        while 1:
            if day_of_week not in days:
                print("Entered choice is invalid..should be one of Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday..enter again!")
                day_of_week = input().lower
            else:
                break
        print("\n")
        
    else:
        month = 'all'
        day_of_week = 'all'
        print("\n")

    return city_name,month,day_of_week

def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day from the bikeshare data
    Args:
        (str) city - name of the city to filter by
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #converts into standard time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        #if choice not none
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'all':
        #if choice not none
        df = df[df['day_of_week'] == day.title()]

    return df
    print("\n")

def time_stats(df):

    #first statistics is printed
    print("Calculating the first statistic...")
    start_time = time.time()
    #time in seconds 

    frequent_month = df['Start Time'].dt.month.mode()[0]
    frequent_day = df['Start Time'].dt.weekday_name.mode()[0]
    frequent_hour = df['Start Time'].dt.hour.mode()[0]

    print("Most popular hour: %s " % (frequent_hour))
    #print additionl detail like popular day of travel
    print("Most popular Day: %s " % (frequent_day))
    #print additional detail like popular month of travel
    print("Most popular Month: %s " % (frequent_month))

    print("That took %s seconds." % (time.time() - start_time))
    #prints total time to print the above details
    print("\n")
    
          
def trip_duration_stats(df):

    #Next statistics.. the total and average trip duration
    print("Calculating the next statistic...trip duration:")
    start_time = time.time()
    #time in seconds

    total_trip_time = df['Trip Duration'].sum()
    #Total time

    mean_trip_time = df['Trip Duration'].mean()
    #Mean time

    print("Total Duration %s in seconds. " % (total_trip_time))
    print("Avg Duration %s in seconds. " % (mean_trip_time))

    print("That took %s seconds." % (time.time() - start_time))
    #prints total time to print the above details 
    print("\n")


def station_stats(df):

    #Next statistics.. the most popular stations and the most popular trip
    print("Calculating the next statistic...popular_station:")
    start_time = time.time()
    #time in seconds

    popular_start_station = df['Start Station'].mode()[0]
    #popular start station fron bikeshare data

    popular_end_station = df['End Station'].mode()[0]
    #popular end station from bikeshare data
    
    trip_counts = df.groupby(['Start Station','End Station']).size().reset_index(name = 'trips')
    sort_trips = trip_counts.sort_values('trips', ascending = False)
    start_trip = sort_trips['Start Station'].iloc[0]
    end_trip = sort_trips['End Station'].iloc[0]

    print("Most popular Start Station: %s " % (popular_start_station))
    print("Most popular End Station: %s " % (popular_end_station))
    print("Most popular trip:(' %s',' %s') " % (start_trip,end_trip))

    print("That took %s seconds." % (time.time() - start_time))
    #prints total time to print the above details
    print("\n")
    

def user_stats(df,city):

    #Next statistics... user type , gender and birth year
    print("Calculating the next statistic...user_type")
    start_time = time.time()
    #time in seconds

    if 'User Type' in df.columns:
        print(df['User Type'].value_counts())
    else:
        print("invalid User Type")
          
    print("That took %s seconds." % (time.time() - start_time))
    #prints total time to print the above details
    print("\n")

    print("Calculating the next statistic...gender")

    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("invalid Gender")
          
    print("That took %s seconds." % (time.time() - start_time))
    #prints total time to print the above details
    print("\n")
          
    print("Calculating the next statistic...birth_year")
    
    if 'Birth Year' in df.columns:
        max_birth_year = df['Birth Year'].max()
        print("Most Recent Birth Year: %s " % (max_birth_year))

        min_birth_year = df['Birth Year'].min()
        print("Most Earliest Birth Year: %s " % (min_birth_year))

        popular_birth_year = df['Birth Year'].mode()[0]
        print("Most popular Birth Year: %s " % (popular_birth_year))
    else:
        print("invalid Birth Year")
    
    print("That took %s seconds." % (time.time() - start_time))
    #prints total time to print the above details
    print("\n")
   

def main():
    while True:
        city,month,day = get_filters()
        df = load_data(city,month,day)

        time_stats(df)
        trip_duration_stats(df)
        station_stats(df)
        user_stats(df,city)

        print("Would you like see five rows of data ?? Enter 'yes' or 'no' ")
        display_data = input()
        display_data = display_data.lower()
        
        i = 5
        while display_data == 'yes':
            print(df[:i])
            print("Would you like to see five more rows of data ?? Enter 'yes' or 'no' ")
            i += 5
            display_data = input()
            display_data = display_data.lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        print("\n")

if __name__ == "__main__":
	main()