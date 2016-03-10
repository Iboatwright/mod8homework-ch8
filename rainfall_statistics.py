# rainfall_statistics.py
# Exercise selected: Chapter 8 program 3
# Name of program: Rainfall Statistics
# Description of program: This program allows the user to enter the total
#   rainfall for each month.  It calculates the total rainfall
#   for the year, the average monthly rainfall, and the months with the
#   highest and lowest amounts.  Then it displays the results.
#
# Ivan Boatwright
# March 10, 2016

def main():
    # Local constants
    MONTHS = ('january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december')
    
    # Local variables
    rainfall = []
    yearlyTotal = 0.0
    avgMonthly = 0.0
    lowestMonth = ''
    highestMonth = ''
    
    
    # Display intro to user.
    fluffy_intro()
    
    # Have the user enter the rainfall amount for each month.
    get_rainfall(MONTHS, rainfall)
    
    # Calculate yearly rainfall total.
    yearlyTotal = sum(rainfall)
    
    # Calculate average monthly rainfall.
    avgMonthly = calc_average(yearlyTotal, 12)
    
    # Get month with the least amount of rain.
    lowestMonth = merge_sort(rainfall, MONTHS)[0][1]
    
    # Get month with the highest amount of rain.
    highestMonth = merge_sort(rainfall, MONTHS)[-1][1]
    
    # Display results.
    display_results(yearlyTotal, avgMonthly, lowestMonth, highestMonth)


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('Welcome to the Rainfall Statistics program.\n'
          'This program has you enter the total rainfall for each month.\n'
          'It then displays the total rainfall for the year, the monthly\n'
          'average, and the months with the highest and lowest rainfall\n'
          'amounts.\n')
    return None


# Iterates through the list of months.  Each iteration has the user input
#   the rainfall for that month.  The value is assigned to the rainfall array
#   with the same index as that month.
def get_rainfall(MONTHS, rainfall):
    print('{}\nPlease enter the rainfall for each month.\n'.format('_' * 41))
    for k, month in enumerate(MONTHS):
        rainfall[k] = input('{}:  '.format(month.capitalize()))
    return None


# Calculates the average of two numbers and return the value.  Optionally
#   specify how many decimal places are returned.  If percent is True or if
#   there is no fractional component, the value is converted to an integer
#   and returned.
def calc_average(x, xTotal, precision=2, percent=False):
    avg = round(x / xTotal, precision)
    if percent: avg = '{}%'.format(int(avg * 100))
    elif x % xTotal == 0: avg = int(avg)
    return avg


# Sorts two arrays and returns a list of tuple pairs.  The arrays are
#   sorted by the first parameter in ascending order.
def merge_sort(first, second):
    return sorted(zip(first, second))


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(yearlyTotal, avgMonthly, lowestMonth, highestMonth):
    print('_' * 41)
    print('The total rainfall for the year is: ' + yearlyTotal)
    print('The average monthly rainfall is: ' + avgMonthly)
    print('The month with the least rain was: ' + lowestMonth.capitalize())
    print('The month with the most rain was: ' + highestMonth.capitalize())