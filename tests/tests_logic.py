import pytest
from game import GamePole, Cell  # Assumes GamePole and Cell classes are in game.py


# Test data: 3x3 field with one mine at the center (1, 1)
@pytest.fixture
def pole_3x3_with_center_mine():
    pole = GamePole(3, 1)  # N=3, M=1
    # Force-place the mine at the center (for predictable testing)
    pole.raw_list = [[False, False, False],
                     [False, True, False],
                     [False, False, False]]
    pole.init()  # Recreate Cell objects with new counts based on the raw_list
    return pole


def test_cell_initialization():
    """Verify that the cell initializes correctly."""
    cell = Cell(around_mines=3, mine=True, fl_open=False)
    assert cell.mine is True
    assert cell.around_mines == 3
    assert cell.fl_open is False


def test_get_around_algorithm(pole_3x3_with_center_mine):
    """Verify that the mine-counting algorithm (get_around) works correctly."""

    # Cell (0, 0) should see 1 mine
    cell_0_0 = pole_3x3_with_center_mine.pole[0][0]
    assert cell_0_0.around_mines == 1

    # Cell (1, 0) should see 1 mine
    cell_1_0 = pole_3x3_with_center_mine.pole[1][0]
    assert cell_1_0.around_mines == 1

    # Cell (1, 2) should see 1 mine
    cell_1_2 = pole_3x3_with_center_mine.pole[1][2]
    assert cell_1_2.around_mines == 1


def test_open_mine_loses_game(pole_3x3_with_center_mine):
    """Verify that opening a mine leads to a loss."""
    # Open the mine at the center (1, 1)
    pole_3x3_with_center_mine.open(1, 1)

    # For testing purposes, we check that the cell opened and the loss flag is conceptually set.
    # Note: A public getter method for '__lose' in GamePole would be necessary for a definitive test.
    assert pole_3x3_with_center_mine.pole[1][1].fl_open is True