def displayWelcome ():
    print('This program will convert a range of temperatures.')
    print('Enter (F) to convert Fahrenheit to Celsius.')
    print('Enter (C) to convert Celsius to Fahrenheit.')
#Kelvin
    print('Enter (CK) to convert Celsius to Kelvin.')
    print('Enter (FK) to convert Fahrenheit to Kelvin.')
    print('Enter (KC) to convert Kelvin to Celsius.')
    print('Enter (KF) to convert Kelvin to Fahrenheit.')

def getConvertTo():
    
    which = input('Enter selection: ')
    while which != 'F' and which != 'C'and which != 'CK' and which != 'FK' and which != 'KC' and which != 'KF':
        which = input('Enter selection: ')

    return which

def displayFahrenToCelsius(start, end):
    print('\n  Degrees', ' Degrees')
    print('Fahrenheit', 'Celsius')

    for temp in range(start, end + 1):
        converted_temp = (temp - 32) * 5/9
        print(' ', format(temp, '4.1f'), '  ', format(converted_temp, '4.1f'))

def displayCelsiusToFahren(start, end):
    print('\n Degrees', ' Degrees')
    print(' Celsius', 'Fahrenheit')

    for temp in range(start, end + 1):
        converted_temp = (9/5 * temp) + 32
        print(' ', format(temp, '4.1f'), '  ', format(converted_temp, '4.1f'))
        
# adding Kelvin

def displayCelsiusToKelvin(start, end):
    print('\n Degrees', ' Degrees')
    print(' Celsius', 'Kelvin')

    for temp in range(start, end +1):
        converted_temp = temp + 273.15
        print(' ', format(temp, '4.1f'), '  ', format(converted_temp, '4.1f'))
        
def displayFahrenToKelvin(start, end):
    print('\n Degrees', ' Degrees')
    print('Fahrenheit', 'Kelvin')
    
    for temp in range(start, end +1):
        converted_temp = (temp + 459.67) * (5/9)
        print(' ', format(temp, '4.1f'), '  ', format(converted_temp, '4.1f'))

def displayKelvinToCelsius(start, end):
    print('\n Degrees', '  Degrees')
    print(' Kelvin', '  Celsius')
    
    for temp in range(start, end +1):
        converted_temp = temp - 273.15
        print(' ', format(temp, '4.1f'), '  ', format(converted_temp, '4.1f'))

def displayKelvinToFahren(start, end):
    print('\n Degrees', ' Degrees')
    print(' Kelvin', 'Fahrenheit')
    
    for temp in range(start, end +1):
        converted_temp = (temp - 273.15) * (9/5) + 32
        print(' ', format(temp, '4.1f'), '  ', format(converted_temp, '4.1f'))


    
#---- main

# Display program welcome
displayWelcome()
which = getConvertTo()
temp_start = int(input('Enter starting temperature to convert: '))
temp_end = int(input('Enter ending temperature to convert: '))
if which == 'F':
    displayFahrenToCelsius(temp_start, temp_end)
if which == 'C':
    displayCelsiusToFahren(temp_start, temp_end)
if which == 'KC':
    displayKelvinToCelsius(temp_start, temp_end)
if which == 'KF':
    displayKelvinToFahren(temp_start, temp_end)
if which == 'CK':
    displayCelsiusToKelvin(temp_start, temp_end)
if which == 'FK':
    displayFahrenToKelvin(temp_start, temp_end)
                          
