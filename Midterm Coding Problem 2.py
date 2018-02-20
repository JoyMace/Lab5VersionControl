# Joy Mace Midterm Coding Problem 2


car_speed = int(input('How fast is your car going? Enter in mph:'))

if car_speed > 60:
    print ('\nSLOW DOWN!')
if car_speed < 45:
    print ('\nMinimum speed is 45 mph.')
elif car_speed < 60 and car_speed > 45:
    print ('\nYou are a good driver!')
