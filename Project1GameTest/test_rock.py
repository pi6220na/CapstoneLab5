# Lab5 - Part2 - Test Game

import rock
from unittest import TestCase
from unittest.mock import patch

class TestRockGame(TestCase):
    '''This test suite validates the game logic and program logic are correct based on which object (rock,paper,scissors) the player has'''

    def test_determine_winner(self):
        '''verify all winner/loser combinations return correct result.'''
        firstCall = rock.determine_winner(1,1)
        # print(firstCall)
        self.assertEqual(firstCall, 'tie')

        firstCall = rock.determine_winner(1,2)
        # print(firstCall)
        self.assertEqual(firstCall, 'computer wins - paper wraps rock')
        firstCall = rock.determine_winner(1,3)
        # print(firstCall)
        self.assertEqual(firstCall, 'player wins - rock breaks scissors')

        firstCall = rock.determine_winner(2,1)
        # print(firstCall)
        self.assertEqual(firstCall, 'player wins - paper wraps rock')
        firstCall = rock.determine_winner(2,3)
        # print(firstCall)
        self.assertEqual(firstCall, 'computer wins - scissors cuts paper')

        firstCall = rock.determine_winner(3,1)
        # print(firstCall)
        self.assertEqual(firstCall, 'computer wins - rock breaks scissors')
        firstCall = rock.determine_winner(3,2)
        # print(firstCall)
        self.assertEqual(firstCall, 'player wins - scissors cuts paper')

    def test_get_computer_pick(self):
        '''This function validates that the random function returns 1, 2, or 3'''

        firstCall = rock.get_computer_pick()
        # print(firstCall)
        self.assertIn((firstCall), (1, 2, 3))

        for x in range(1,4):             # iterate 1, 2, and 3
            with patch('rock.get_computer_pick', side_effect=[x]):

                firstCall = rock.get_computer_pick()
                # print(firstCall)
                self.assertIn((firstCall),(1,2,3))
                self.assertNotIn((firstCall),(4,5,6))

            with patch('random.randint', return_value=[x]):
                self.assertTrue(x, rock.get_computer_pick())


    @patch('rock.get_computer_pick', side_effect=[2])
    @patch('builtins.input', side_effect=['1', 'q'])
    @patch('builtins.print')
    def test_run_full_game(self, mock_print, mock_input, mock_menu):
        '''This test simulates one game play invoking the program rock.py'''

        # Call main function to start program.
        rock.main()

        # assert user was asked to make a selection
        mock_input.assert_called_with('Please make a selection: ')

        # Assert computer chose paper and printed
        mock_print.assert_any_call('Computer chose: Paper')

        # Assert the winner string printed
        mock_print.assert_any_call('computer wins - paper wraps rock')

        # Assert that program printed the quit message .
        mock_print.assert_any_call('Thanks for playing')

        # final print statement is blank
        mock_print.assert_called_with('')


    def test_run_auto_calc_stats(self):
        '''Validate for computer generated game play that the statistics are accumulated correcly based on winner string'''

        #use a dictionary to hold win/loss counts and stats
        #re-intialize player1 and player2 dictionaries for each invocation
        player1 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        player2 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}

        winner = 'tie'
        rock.run_auto_calc_stats(winner,player1,player2)
        self.assertEqual(player1['3-tie'],player2['3-tie'])

        player1 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        player2 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        winner = 'computer wins - paper wraps rock'
        rock.run_auto_calc_stats(winner, player1, player2)
        self.assertEqual(player1['2-loss'], player2['1-win'])
        self.assertEqual(player2['5-paper'], 1)

        player1 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        player2 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        winner = 'player wins - rock breaks scissors'
        rock.run_auto_calc_stats(winner, player1, player2)
        self.assertEqual(player1['1-win'], player2['2-loss'])
        self.assertEqual(player1['4-rock'], 1)

        player1 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        player2 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        winner = 'player wins - paper wraps rock'
        rock.run_auto_calc_stats(winner, player1, player2)
        self.assertEqual(player1['1-win'], player2['2-loss'])
        self.assertEqual(player1['5-paper'], 1)

        player1 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        player2 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        winner = 'computer wins - scissors cuts paper'
        rock.run_auto_calc_stats(winner, player1, player2)
        self.assertEqual(player1['2-loss'], player2['1-win'])
        self.assertEqual(player2['6-scissors'], 1)

        player1 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        player2 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        winner = 'computer wins - rock breaks scissors'
        rock.run_auto_calc_stats(winner, player1, player2)
        self.assertEqual(player1['2-loss'], player2['1-win'])
        self.assertEqual(player2['4-rock'], 1)

        player1 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        player2 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
        winner = 'player wins - scissors cuts paper'
        rock.run_auto_calc_stats(winner, player1, player2)
        self.assertEqual(player1['1-win'], player2['2-loss'])
        self.assertEqual(player1['6-scissors'], 1)

