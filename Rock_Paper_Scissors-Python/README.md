# Rock Paper Scissors Game

A simple Python implementation of the classic **Rock, Paper, Scissors** game where you play against the computer.

## Features

- User can choose the number of rounds to play.
- Accepts input in a flexible way: `r`, `rock`, `R`, `RoCk` — all are recognized.
- Displays computer's random choice.
- Shows running score after every round.
- Declares the final winner.

## How It Works

1. The program asks you how many games you want to play.
2. In each round, you type **R**, **P**, or **S** (case-insensitive).
3. The computer randomly selects Rock, Paper, or Scissors.
4. The winner of the round is decided based on the classic rules:
   - Rock beats Scissors
   - Scissors beat Paper
   - Paper beats Rock
5. The score is displayed after each round.
6. The game ends when all rounds are played and the winner is announced.

## Example

```bash
Enter the number of games you want to play: 3

User's input: r
Computer's Input: Paper
Score:
User Score: 0   Computer Score: 1

User's input: p
Computer's Input: Rock
Score:
User Score: 1   Computer Score: 1

User's input: s
Computer's Input: Scissors
TIE
Score:
User Score: 1   Computer Score: 1

        OOPS! IT'S A TIE!
```

## Requirements

- Python 3.x

No additional libraries are required (uses only the built-in `random` module).

## Running the Game

Run the script from your terminal:

```bash
python rock_paper_scissors.py
```

## Author Name:
[Raul Dumitrele](https://github.com/Raul-Dumitrele)
