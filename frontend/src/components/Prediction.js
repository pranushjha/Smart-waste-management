import React, { useEffect, useState } from "react";
import axios from "axios";

const Prediction = () => {
  const [prediction, setPrediction] = useState(null);

  // Function to fetch prediction from the backend
  const fetchPrediction = async () => {
    try {
      const data = {}; // You can send relevant data here
      const response = await axios.post('http://localhost:5001/predict', data);
      setPrediction(response.data); // Set the response data to state
    } catch (error) {
      console.error('Error fetching prediction:', error);
    }
  };

  // Fetch prediction on component mount
  useEffect(() => {
    fetchPrediction(); // Call fetchPrediction when the component mounts
  }, []);

  return (
    <div>
      <h3>AI-Based Overflow Prediction</h3>
      {prediction ? (
        <p>Next Overflow Expected: <strong>{prediction.time}</strong></p> // Display prediction time
      ) : (
        <p>Loading prediction...</p> // Show loading message while fetching data
      )}
    </div>
  );
};

export default Prediction;
