"""A small, dependency-free command-line tic-tac-toe game."""

from __future__ import annotations

from dataclasses import dataclass, field


WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


@dataclass
class Game:
    """Track a game and enforce its rules."""

    board: list[str] = field(default_factory=lambda: [" "] * 9)
    current_player: str = "X"

    @property
    def winner(self) -> str | None:
        for first, second, third in WINNING_LINES:
            if (
                self.board[first] != " "
                and self.board[first] == self.board[second] == self.board[third]
            ):
                return self.board[first]
        return None

    @property
    def is_draw(self) -> bool:
        return self.winner is None and all(cell != " " for cell in self.board)

    @property
    def is_over(self) -> bool:
        return self.winner is not None or self.is_draw

    def move(self, position: int) -> None:
        """Place the current player's mark in a 1-based position."""
        if self.is_over:
            raise ValueError("the game is over")
        if not 1 <= position <= 9:
            raise ValueError("position must be between 1 and 9")
        index = position - 1
        if self.board[index] != " ":
            raise ValueError("position is already occupied")
        self.board[index] = self.current_player
        self.current_player = "O" if self.current_player == "X" else "X"

    def render(self) -> str:
        cells = [
            cell if cell != " " else str(index + 1)
            for index, cell in enumerate(self.board)
        ]
        return "\n---+---+---\n".join(
            (" | ".join(cells[row : row + 3]) for row in range(0, 9, 3))
        )


def main() -> None:
    game = Game()
    print("Tic-tac-toe: choose a position from 1 to 9 (or q to quit).")
    while not game.is_over:
        print(f"\n{game.render()}")
        choice = input(f"\n{game.current_player}'s move: ").strip().lower()
        if choice in {"q", "quit"}:
            print("Goodbye!")
            return
        try:
            game.move(int(choice))
        except ValueError as error:
            print(f"Invalid move: {error}")

    print(f"\n{game.render()}")
    print(f"\n{game.winner} wins!" if game.winner else "\nIt's a draw!")


if __name__ == "__main__":
    main()
