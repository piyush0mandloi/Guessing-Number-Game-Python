from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_no = random.randint(1, 10)
attempts_left = 5

def reset_game():
    global attempts_left
    global secret_no
    attempts_left = 5
    secret_no = random.randint(1,10)

    return True


@app.route("/", methods=["GET", "POST"])
def home():
    global secret_no
    global attempts_left

    message = ""

    if request.method == "POST" and attempts_left > 0:

        guess = int(request.form["guess"])

        attempts_left -= 1

        if guess < secret_no:
            message = "Too Low!"
        elif guess > secret_no:
            message = "Too High!"
        else:
            message = "🎉 Correct! You Win!"
            reset_game()

        if attempts_left == 0 and guess != secret_no:
            message = f"❌ Game Over! The number was {secret_no}"
            reset_game()

    return render_template(
        "index.html",
        message=message,
        attempts_left=attempts_left
    )


if __name__ == "__main__":
    app.run(debug=True)