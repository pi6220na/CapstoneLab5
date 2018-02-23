##### adding records to the database broke this test #####

# Lab5 - Part1a


import mileage
import sqlite3
from unittest import TestCase

class TestMileageDB(TestCase):

    test_db_url = 'test_miles.db'

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        # Overwrite the mileage
        mileage.db_url = self.test_db_url
        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('DELETE FROM miles')

        # add test records for Lab 5 - Part 1b

        conn.execute("INSERT INTO miles ('vehicle', 'total_miles') values(?, ?)", ('WHITE', int(111),))
        conn.execute("INSERT INTO miles ('vehicle', 'total_miles') values(?, ?)", ('GINGER', int(222),))
        conn.execute("INSERT INTO miles ('vehicle', 'total_miles') values(?, ?)", ('PINK', int(333),))

        conn.commit()
        conn.close()


    # changed expected dictionaries in 4 tests below to match new requirement for upper case vehicle name

    def test_add_new_vehicle(self):
        mileage.add_miles('Blue Car', 100)
        expected = { 'BLUE CAR': 100, 'WHITE':111, 'GINGER':222, 'PINK':333 }
        self.compare_db_to_expected(expected)

        mileage.add_miles('Green Car', 50)
        expected['GREEN CAR'] = 50
        self.compare_db_to_expected(expected)


    def test_increase_miles_for_vehicle(self):
        mileage.add_miles('Red Car', 100)
        expected = { 'RED CAR': 100, 'WHITE':111, 'GINGER':222, 'PINK':333  }
        self.compare_db_to_expected(expected)

        mileage.add_miles('Red Car', 50)
        expected['RED CAR'] = 100 + 50
        self.compare_db_to_expected(expected)


    def test_add_new_vehicle_no_vehicle(self):
        with self.assertRaises(Exception):
            mileage.add_miles(None, 100)


    def test_add_new_vehicle_invalid_new_miles(self):
        with self.assertRaises(Exception):
            mileage.add_miles('Car', -100)
        with self.assertRaises(Exception):
            mileage.add_miles('Car', 'abc')
        with self.assertRaises(Exception):
            mileage.add_miles('Car', '12.def')



    # Lab 5 - Part 1a: Test that new vehicles test added to DB in upper case

    def test_add_new_vehicle_mixed_case(self):
        mileage.add_miles('OrAnGe car', 100)
        expected = {'ORANGE CAR': 100, 'WHITE':111, 'GINGER':222, 'PINK':333 }
        self.compare_db_to_expected(expected)

        mileage.add_miles('orange car', 50)
        expected['ORANGE CAR'] = 100 + 50
        self.compare_db_to_expected(expected)




    # This is not a test method, instead, it's used by the test methods
    def compare_db_to_expected(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM MILES').fetchall()

        #print(expected)
        #print()
        #print(all_data)

        # Same rows in DB as entries in expected dictionary
        self.assertEqual(len(expected.keys()), len(all_data))               #### WHy this check ?????????????????
                                                                            #### So that the followiing for in loop works?
        for row in all_data:
            # Vehicle exists, and mileage is correct
            self.assertIn(row[0], expected.keys())

            #print('looping through row in all_data')
            #print(row[0])
            #print(expected[row[0]])
            #print(row[1])
            self.assertEqual(expected[row[0]], row[1])

        conn.close()

