<img width="1609" height="903" alt="Screenshot 2026-05-31 115807" src="https://github.com/user-attachments/assets/465213c8-6bfd-41c6-9c8d-2d689e829520" />

# Number Guessing Game

A simple web-based number guessing game built with Python and Flask. The app chooses a random number between 1 and 10, and the player gets 5 attempts to guess it.

## Features

- Random secret number from 1 to 10
- 5 attempts per round
- Feedback for each guess: too high, too low, or correct
- Automatic game reset after a win or game over
- Retro arcade-style interface using HTML and CSS

## Tech Stack

- Python
- Flask
- HTML
- CSS

## Project Structure

```text
.
+-- a.py
+-- templates/
|   +-- index.html
+-- static/
    +-- style.css
```

## Requirements

Make sure Python is installed on your system. Then install Flask:

```bash
pip install flask
```

## How To Run

1. Open a terminal in the project folder.
2. Run the Flask app:

```bash
python a.py
```

3. Open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## How To Play

1. Enter a number between 1 and 10.
2. Click **Guess**.
3. Use the message to adjust your next guess.
4. Win by guessing the correct number before your 5 attempts run out.

## Main Files

- `a.py` - Flask app, game logic, random number generation, and route handling.
- `templates/index.html` - Main game page.
- `static/style.css` - Styling for the retro game interface.

## Future Improvements

- Add input validation for non-number guesses.
- Add a working manual reset button.
- Let the player choose a difficulty level.
- Show previous guesses during the round.
