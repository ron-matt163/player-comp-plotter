import { useState, useRef } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [players, setPlayers] = useState([{ name: "", id: "" }]);
  const [statType, setStatType] = useState("goals");
  const [suggestions, setSuggestions] = useState({});
  const [plotUrl, setPlotUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const typingTimeoutRef = useRef(null);
  const suggestionClickedRef = useRef(false);

  const handlePlayerChange = (index, value) => {
    const updatedPlayers = [...players];
    updatedPlayers[index] = { name: value, id: "" }; // Reset ID when changing input
    setPlayers(updatedPlayers);

    if (typingTimeoutRef.current) {
      clearTimeout(typingTimeoutRef.current);
    }

    typingTimeoutRef.current = setTimeout(async () => {
      if (value.trim() !== "") {
        try {
          const response = await axios.get(
            `http://localhost:5000/search-players?keyword=${value}`
          );
          setSuggestions((prev) => ({ ...prev, [index]: response.data }));
        } catch (error) {
          console.error("Error fetching player suggestions:", error);
        }
      } else {
        setSuggestions((prev) => ({ ...prev, [index]: {} }));
      }
    }, 500);
  };

  const handleInputFocus = (index) => {
    setSuggestions((prev) => ({ ...prev, [index]: suggestions[index] || {} }));
  };

  const handleInputBlur = (index) => {
    // Delay to allow mouse click to register before clearing suggestions
    setTimeout(() => {
      if (!suggestionClickedRef.current) {
        setSuggestions((prev) => ({ ...prev, [index]: {} }));
      }
      suggestionClickedRef.current = false; // Reset the flag
    }, 200); // Keep this delay minimal
  };

  const selectSuggestion = (index, id, name) => {
    suggestionClickedRef.current = true; // Mark that a suggestion was clicked
    const updatedPlayers = [...players];
    updatedPlayers[index] = { name, id };
    setPlayers(updatedPlayers);

    setSuggestions((prev) => ({ ...prev, [index]: {} }));
  };

  const addNewPlayer = () => {
    setPlayers([...players, { name: "", id: "" }]);
  };

  const removePlayer = (index) => {
    const updatedPlayers = [...players];
    updatedPlayers.splice(index, 1);
    setPlayers(updatedPlayers);
  };

  const handleGenerate = async () => {
    try {
      setLoading(true);
      // Fetch client's IP address
      const ipResponse = await axios.get("https://api64.ipify.org?format=json");
      const clientIp = ipResponse.data.ip;

      // Generate unique request ID
      const requestId = `${Date.now()}-${clientIp}`;
      const response = await axios.post("http://localhost:5000/generate-plot", {
        players,
        stat_type: statType,
        request_id: requestId, // Add the request ID here
      });

      const base64Image = response.data.image_base64;
      setPlotUrl(`data:image/png;base64,${base64Image}`);
    } catch (error) {
      console.error("Error generating plot:", error);
    } finally {
      setLoading(false);
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
              <div className="input-suggestions-container">
                <input
                  type="text"
                  style={{ width: "90%" }}
                  value={player.name}
                  onChange={(e) => handlePlayerChange(index, e.target.value)}
                  onFocus={() => handleInputFocus(index)}
                  onBlur={() => handleInputBlur(index)}
                  placeholder={`Player ${index + 1}`}
                />
                {suggestions[index] && Object.keys(suggestions[index]).length > 0 && (
                  <ul className="suggestions-list">
                    {Object.entries(suggestions[index]).map(([id, name]) => (
                      <li
                        key={id}
                        onMouseDown={() => {
                          suggestionClickedRef.current = true; // Set flag early
                        }}
                        onClick={() => selectSuggestion(index, id, name)}
                      >
                        {name}
                      </li>
                    ))}
                  </ul>
                )}
              </div>
              <button className="remove-button" onClick={() => removePlayer(index)}>
                -
              </button>
            </div>
          ))}

          <button
            style={{
              display: "block",
              margin: "10px auto",
              backgroundColor: "#007bff",
              color: "white",
              border: "none",
              padding: "10px 20px",
              borderRadius: "5px",
              cursor: "pointer",
            }}
            onClick={addNewPlayer}
          >
            Add New Player
          </button>
          <button
            style={{
              display: "block",
              margin: "10px auto",
              backgroundColor: "#28a745",
              color: "white",
              border: "none",
              padding: "10px 20px",
              borderRadius: "5px",
              cursor: "pointer",
            }}
            onClick={handleGenerate}
          >
            Generate
          </button>
        </div>
      </div>

      <div className="plot-container">
        {loading ? (
          <div className="spinner"></div> // Show spinner while loading
        ) : plotUrl ? (
          <img src={plotUrl} alt="Player Stats Plot" />
        ) : (
          <p>The generated comparison plot will appear here.</p>
        )}
      </div>
    </div>
  );
}

export default App;
