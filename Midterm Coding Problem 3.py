# Joy Mace Midterm Coding Problem 3

tuple = ('Winter', 'Spring', 'Summer', 'Fall');

season = int(input('Enter an integer from 1 to 4:'))

if season == 1:
    print ('\nThe number',season, 'is the season code for',tuple[0])
    
if season == 2:
    print ('\nThe number',season, 'is the season code for',tuple[1])
    
if season == 3:
    print ('\nThe number',season, 'is the season code for',tuple[2])
    
if season == 4:
    print ('\nThe number',season, 'is the season code for',tuple[3])

    
if season > 4 or season < 1:
    print ('There is no season associated with that code number.')
