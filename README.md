# 💣 Minesweeper

**Author:** [Your Name / Your GitHub Username]

## 🎯 Project Overview

This is a console (or graphical, if Pygame is integrated) implementation of the classic Minesweeper game. The project is created to demonstrate solid knowledge of **Object-Oriented Programming (OOP)**, fundamental **algorithms**, and **data structures** in Python.

### Key Implementation Goals:

1.  **OOP Architecture:** Clear separation of game logic into dedicated classes (`GamePole` and `Cell`).
2.  **Algorithms:** Implementation of an efficient algorithm for placing mines and counting surrounding mines.
3.  **Testability:** Developing clean code that supports Unit Testing (using `pytest`).

***

## 🏗️ Architecture and Code Structure

The project is built upon two core classes, showcasing the principle of **Separation of Concerns**:

| Class | Responsibility |
| :--- | :--- |
| **`Cell`** | Stores the state of a single cell: mine presence (`mine`), number of surrounding mines (`around_mines`), and the open status (`fl_open`). |
| **`GamePole`** | Manages the overall game process: field initialization, mine placement, neighbor counting, handling clicks (`open`), and display (`show`). |

### OOP and Encapsulation

* **Private Attributes:** Private (protected) attributes, such as `__lose` and `__length`, are used to strictly control and protect the internal state of the game.
* **Encapsulation:** The `init()` method fully encapsulates the complex logic of field creation, mine placement, and neighbor counting.

***

## 🚀 How to Run the Project

### Requirements

The project requires Python 3.8+ and `pygame` (if you are running the graphical version) and `pytest` for testing.

1.  **Cloning the repository:**
    ```bash
    git clone [https://github.com/Your_Username/Minesweeper.git](https://github.com/Your_Username/Minesweeper.git)
    cd Minesweeper
    ```

2.  **Installing dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Running the game (console version):**
    ```bash
    python game.py 
    # After running, you can call methods interactively: pole_game.open(i, j)
    ```

***

## 🧪 Testing (Using Pytest)

Unit tests are implemented to verify the correctness of core game algorithms, such as the mine-counting logic (`GamePole.get_around`) and the game-over condition (`GamePole.open`).

**Running Tests:**

```bash
pytest
