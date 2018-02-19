# Lab5 - Part2 - Test Game

import rock
from unittest import TestCase

class TestRockGame(TestCase):

    def test_determine_winner(self):
        
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
        firstCall = rock.get_computer_pick()
        # print(firstCall)
        self.assertIn((firstCall),(1,2,3))
        firstCall = rock.get_computer_pick()
        # print(firstCall)
        self.assertNotIn((firstCall),(4,5,6))

    # def test_computer_play(self):
    #     # use a dictionary to hold win/loss counts and stats
    #     # player1 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
    #     # player2 = {'3-tie': 0, '1-win': 0, '2-loss': 0, '4-rock': 0, '5-paper': 0, '6-scissors': 0}
    #     pass

    def test_run_auto_calc_stats(self):
        #use a dictionary to hold win/loss counts and stats
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
