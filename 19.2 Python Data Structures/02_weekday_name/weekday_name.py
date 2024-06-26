def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    
    days_list = [None,'Sunday', 'Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday']
    if isinstance(day_of_week, int) and day_of_week >= 1 and day_of_week <= 7:
        return days_list[day_of_week]
    else: 
        return None