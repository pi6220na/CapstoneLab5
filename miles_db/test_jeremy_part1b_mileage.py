##### Starting from scratch, this test seems to be working #######

# Lab5 - Part 1b

import mileage
import sqlite3
from unittest import TestCase

class TestMileageDBPart1b(TestCase):

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
        conn.execute("INSERT INTO miles ('vehicle', 'total_miles') values(?, ?)", ('BLUE', int(222),))
        conn.execute("INSERT INTO miles ('vehicle', 'total_miles') values(?, ?)", ('RED', int(333),))

        conn.commit()
        conn.close()


    # changed expected dictionaries in 4 tests below to match new requirement for upper case vehicle name

    def test_search_for_vehicle(self):
        testMe = mileage.search_for_vehicle('WHITE')
        self.assertIn('WHITE', testMe)
        self.assertNotIn('PURPLE', testMe)

        # self.assertIn('White', testMe) this fails

        testMe = mileage.search_for_vehicle('White')   # returns None
        self.assertEqual(None, testMe)

