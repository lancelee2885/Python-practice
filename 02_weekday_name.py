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
    # TODO: make into a list
    if day_of_week == 1:
        print("'Sunday'")
    elif day_of_week == 2:
        print("'Monday'")
    elif day_of_week == 3:
        print("'Tuesday'")
    elif day_of_week == 4:
        print("'Wednesday'")
    elif day_of_week == 5:
        print("'Thursday'")
    elif day_of_week == 6:
        print("'Friday'")
    elif day_of_week == 7:
        print("'Saturday'")
