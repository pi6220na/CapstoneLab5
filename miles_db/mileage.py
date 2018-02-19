# Lab5 - Part1a

import sqlite3

db_url = 'mileage.db'   # Assumes the table miles have already been created.

def main():

    while True:

        while True:
            vehicle = input('Enter vehicle name or enter to quit')

            if not vehicle:
                break

            # changed float to int
            miles = int(input('Enter new miles for %s' % vehicle))  ## TODO input validation

            if miles > 0 and vehicle:
                add_miles(vehicle, miles)
            else:
                print('Please enter a vehicle name and integer miles')

        while True:

            myString = input('Enter a vehicle to search for or enter to exit: ')

            if not myString:
                break

            result = search_for_vehicle(myString.upper())

            if result == None:
                print("None")
            else:
                print(result[1])

        break

def search_for_vehicle(mySearchStr):
    ''' search for the vehicle passed in parameter. If found, return the corresponding miles for that vehicle.
        If not found, return none'''

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    row = cursor.execute('SELECT * FROM MILES WHERE vehicle = ?', (mySearchStr,))

    for r in row:
        return r

    conn.commit()
    conn.close()


def add_miles(vehicle, new_miles):
    '''If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles

    If the vehicle is None or new_miles is not a positive number, raise Error
    '''

    if not vehicle:
        raise Exception('Provide a vehicle name')
    if isinstance(new_miles, float) or new_miles < 0:
        raise Exception('Provide a positive number for new miles')

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle.upper()))
    if rows_mod.rowcount == 0:
        cursor.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle.upper(), new_miles))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
