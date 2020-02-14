def duration_check(duration_value):
    number_duration = int(duration_value)
    while number_duration > 2 or number_duration < 1:
        print("Enter Job posted duration: (0-Default, 1- newer than 24 hours, 2- newer than 7 days)")
        duration_value = input()
        number_duration = int(duration_value)
    return duration_value
