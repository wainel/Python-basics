def find_fridays(start_date, end_date):
    """
    Write a function that given a start date and end date returns how many 
    Fridays there are between the two dates.
    start_date and end_date should be 'YYYY-MM-DD' strings, e.g. '2014-01-31'
    """
    
    number_of_fridays = 0
    
    # write you code here
    import datetime
    import calendar

    start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    diff = end - start
    days = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}
    full_weeks = (diff.days) // 7
    remainder = (diff.days) % 7
    first_day = start.weekday()
    for day in days.keys():
        days[day] = full_weeks
    
    for i in range(0, remainder):
        days[(first_day + i) % 7] += 1
    
    number_of_fridays = days[4]
    
    return number_of_fridays
