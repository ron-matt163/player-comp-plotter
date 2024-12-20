import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [players, setPlayers] = useState([""]);
  const [statType, setStatType] = useState("Goals");
  const [plotUrl, setPlotUrl] = useState("");

  const handlePlayerChange = (index, value) => {
    const updatedPlayers = [...players];
    updatedPlayers[index] = value;
    setPlayers(updatedPlayers);
  };

  const addPlayerInput = () => {
    setPlayers([...players, ""]);
  };

  const removePlayerInput = (index) => {
    const updatedPlayers = [...players];
    updatedPlayers.splice(index, 1);
    setPlayers(updatedPlayers);
  };

  const handleGenerate = async () => {
    try {
      const response = await axios.post("http://localhost:5000/generate-plot", {
        players,
        stat_type: statType,
      });
      setPlotUrl(response.data.plot_url);
    } catch (error) {
      console.error("Error generating plot:", error);
    }
  };

  return (
    <div className="App">
      <div className="form-container">
        <h1 style={{ textAlign: "center" }}>Player Stats Comparison</h1>
        <div>
          <h3>Stat Type</h3>
          <select
            id="statType"
            value={statType}
            onChange={(e) => setStatType(e.target.value)}
          >
            <option value="goals">Goals</option>
            <option value="assists">Assists</option>
            <option value="xG">Expected Goals</option>
            <option value="xA">Expected Assists</option>
          </select>
        </div>
        <div>
          <h3>Players</h3>
          {players.map((player, index) => (
            <div key={index} className="player-input-row">
              <input
                type="text"
                value={player}
                onChange={(e) => handlePlayerChange(index, e.target.value)}
                placeholder={`Player ${index + 1}`}
              />
              {players.length > 1 && (
                <button
                  className="remove-button"
                  onClick={() => removePlayerInput(index)}
                >
                  -
                </button>
              )}
            </div>
          ))}
          <div className="button-container">
            <button onClick={addPlayerInput}>Add Another Player</button>
            <button onClick={handleGenerate}>Generate</button>
          </div>
        </div>
      </div>
      <div className="plot-container">
        {plotUrl ? (
          <img src={plotUrl} alt="Player Stats Plot" />
        ) : (
          <p>The generated comparison plot will appear here.</p>
        )}
      </div>
    </div>
  );
}

export default App;
