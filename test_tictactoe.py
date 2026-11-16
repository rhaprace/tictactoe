import unittest

from tictactoe import Game


class GameTests(unittest.TestCase):
    def test_move_alternates_players_and_detects_winner(self):
        game = Game()
        for position in (1, 4, 2, 5, 3):
            game.move(position)

        self.assertEqual(game.winner, "X")
        self.assertTrue(game.is_over)
        self.assertEqual(game.current_player, "O")

    def test_rejects_invalid_and_occupied_positions(self):
        game = Game()
        with self.assertRaisesRegex(ValueError, "between 1 and 9"):
            game.move(0)
        game.move(1)
        with self.assertRaisesRegex(ValueError, "already occupied"):
            game.move(1)

    def test_detects_draw(self):
        game = Game()
        for position in (1, 2, 3, 5, 4, 6, 8, 7, 9):
            game.move(position)

        self.assertIsNone(game.winner)
        self.assertTrue(game.is_draw)

    def test_rejects_moves_after_game_ends(self):
        game = Game()
        for position in (1, 4, 2, 5, 3):
            game.move(position)

        with self.assertRaisesRegex(ValueError, "game is over"):
            game.move(6)


if __name__ == "__main__":
    unittest.main()
