import { useEffect, useState } from "react";
import './App.css';
// useEffect is a way to run extra actions after the component already loaded and showed up on the screen
// useState gives your component a way to store and update information (ex. const [scores, setScores] = useState([0, 0, 0]))

export default function App() { // creating a component called 'App' that is available for other parts of the app to use
  const [gameState, setGameState] = useState(null);
  // useState returns an array with two elements: the current state value and a function that lets you update that state
  // gameState holds information about the current state of a game, such as the game board, the current player, or the game's status

  useEffect(() => { // useEffect is a special function in React that allows you to run some code after your component has rendered. 
    fetch("http://localhost:5000/state") // This line sends a request to the backend server (which is running locally at port 5000) to get the current state of the game. 
      // fetches the current game state from your backend server. Once the data is received, you can then use it to update your component's state and display the game board accordingly.

      // .then method is used to handle the result of a promise. Here, it's handling the response from the fetch call.
      .then((res) => res.json()) // (res) => res.json(): is an arrow function that takes the response object (res) and calls its .json() method, which parses it as JSON.
      .then((data) => { // Another arrow function that uses the data that is the result of parsing the response (res) into json format
        console.log("Connected to backend! Game state: ", data);
        setGameState(data); // Save the game state
      })

      // If any of the previous .then() calls throw an error or return a rejected result, the function inside .catch() will be executed
      .catch((err) => {
        console.error("Failed to connect to Flask backend:", err);
      });
  }, []); // The empty [] array means to run this effect only once when the component is created. Otherwise, the code inside the useEffect will 
  // run repeatedly, even when it's not needed. Running this code unnecessarily can slow down your application and may cause it to behave in 
  // unexpected ways.

  function makeMove(row, col) {
    fetch("http://localhost:5000/move", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ row, col, player: "X" }), // or alternate between X and O
    })
      .then((res) => res.json())
      .then((data) => setGameState(data))
      .catch((err) => console.error(err));
  }

  return (
    <div className="App-header">
      <h1 style={{ fontSize: "2rem", fontWeight: "bold", marginBottom: "1rem" }}> {/* rem is the size of the root element. 2rem is twict the root element */}
        Tic-Tac-Toe
      </h1>
      {gameState ? (
        <div className="board">
          {gameState.board.map((row, rowIndex) => (
            <div key={rowIndex} className="board-row">
              {row.map((cell, colIndex) => (
                <button
                  key={colIndex}
                  className="cell"
                  onClick={() => makeMove(rowIndex, colIndex)}
                >
                  {cell}
                </button>
              ))}
            </div>
          ))}
        </div>
      ) : (
        <p style={{ color: "#FBC6CF" }}>Loading game state...</p>
      )}

      {console.log("gamestate: " + JSON.stringify(gameState))}
      {/*
      {gameState ? ( // conditional; if gameState is true. Meaning it is able to return game data (like the board array)
        <pre style={{ // preformatting text tag that creates spaces and breaks that make the text look cleaner
          fontSize: "0.9rem",
          color: "#333",
          backgroundColor: "#FBC6CF",
          padding: "1rem",
          borderRadius: "8px",
          boxShadow: "0 2px 6px rgba(0,0,0,0.1)", // Adds shadow below the element
        }}>
          {JSON.stringify(gameState, null, 2)}
        </pre>
      ) : ( // else (gameState is false)
        <p style={{ color: "#FBC6CF" }}>Loading game state...</p>
      )}*/}
    </div>
  );
}