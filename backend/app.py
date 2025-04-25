from flask import Flask, request, jsonify
from flask_cors import CORS
from game_logic import TicTacToeGame

# Flask(...) is saying: Create a Flask application. You're calling the Flask constructor — like when you make a new object in a game 
# __name__ is a special Python variable that means: Use this file that you’re writing in right now as the starting point
# app = ... You're saving the Flask app you just created into a variable called app, so you can use it later
# CORS(app) Allows your frontend to talk to Flask without being blocked by the browser
# CORS is a security rule that says Websites are only allowed to make requests to the same origin they came from (to protect you from 
# malicious sites). By adding CORS(app) in the Flask app, you're saying it’s safe to let other origins (like React) make requests to me.

app = Flask(__name__) # Creates a Flask app instance. You always add this line (or something very similar) to every Flask app
CORS(app, origins="http://localhost:3001") # You must add this line because you're using Flask as a backend and React as the frontend, so they’re running on different ports

# You're creating a new variable and setting it to an object of the class TicTacToeGame?
game = TicTacToeGame()

# POST request that starts new game
@app.route('/start', methods=['POST'])
def start_game():
    game.reset() # Calling reset() function in game_logic class
    return jsonify({"message": "New game started", "board": game.board})

# POST request for when player makes move
@app.route('/move', methods=['POST'])
def make_move():
    data = request.get_json() # In the data variable, we are storing JSON data that was sent by the frontend
    row = data.get("row") # We are taking value from the JSON data and storing it in the row variable (ex. row = 1)
    col = data.get("col") # We are taking value from the JSON data and storing it in the col variable (ex. col = 2)
    player = data.get("player") # We are taking value from the JSON data and storing it in the player variable (ex. player = X)

    if row is None or col is None or player not in ["X", "O"]: # Preventing any possible errors
        return jsonify({"error": "Invalid move data"}), 400

    result = game.make_move(row, col, player) # Calling the make_move function in the game_logic class and storing it in the result variable
    return jsonify(result) # Sends the result back to the frontend in JSON format

# GET request that returns the state of the current board
@app.route('/state', methods=['GET'])
def get_state():
    return jsonify({
        "board": game.board, # Calls the board function in the game_logic class and sets its value to the board variable
        "winner": game.winner, # Calls the winner function in the game_logic class and sets its value to the winner variable
        "is_draw": game.is_draw # Calls the is_draw function in the game_logic class and sets its value to the is_draw variable
    })

if __name__ == '__main__': # This is saying to only run the code below if this file is being run directly — not if it's being imported in another file. Only the code inside the indented block (underneath that line) runs when the file is executed directly
    app.run(debug=True) # This line actually starts the Flask web server

    # debug=True turns on "debug mode" which:
    #   - automatically reloads the server when you change your code
    #   - Shows helpful error messages in the browser if something breaks