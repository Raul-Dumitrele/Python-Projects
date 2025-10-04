# Dice Game 🎲

![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

A simple dice game where players compete to reach **50 points** or more.  
The game is turn-based, and each player rolls the dice trying to accumulate points.  
If a player rolls a **1**, their current turn score is reset, and the turn passes to the next player.

## 📌 Features

- Supports **2 to 4 players**
- Roll dice to accumulate points
- Turn-based gameplay
- Game ends when a player reaches or exceeds 50 points

## 🛠️ Requirements

- Python 3.x (no external libraries needed)

## 🚀 How to Run

1. Save the code to a file, e.g. `dice_game.py`
2. Run the script:

```bash
python dice_game.py
```

3. Enter the number of players (**between 2 and 4**).
4. Take turns rolling the dice.

   - Press `y` to roll
   - Any other key to stop and keep your score

5. The first player to reach **50 points** wins!

## 📝 Example Gameplay

```
Enter the number of players: 3

Player 1 is your turn!

Your score is: 0
Would you like to roll the dice (y)? y
You got: 5!
Your score is: 5
Total score if you stop now is: 5
Score if you get 1 is: 0
...
The winner is player 2 with a score of: 52
```

