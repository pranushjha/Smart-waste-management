import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const BinStatus = () => {
  const [binData, setBinData] = useState([]);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchBinData = () => {
    const hypotheticalData = {
      binId: 1,
      fillLevel: Math.floor(Math.random() * 100),
      status: Math.random() > 0.5 ? 'Full' : 'Empty',
      timestamp: new Date().toISOString(),
    };

    const newDataPoint = {
      time: hypotheticalData.timestamp,
      fillLevel: hypotheticalData.fillLevel,
    };

    setBinData((prevData) => {
      const updatedData = [...prevData, newDataPoint];
      localStorage.setItem('binData', JSON.stringify(updatedData));
      return updatedData;
    });
  };

  const getOverflowPrediction = async (currentLevel, previousFillTime, trafficStatus) => {
    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', {
        current_level: currentLevel,
        previous_fill_time: previousFillTime,
        traffic_status: trafficStatus,
      });
      setPrediction(response.data.time_to_overflow);
    } catch (error) {
      console.error('Error fetching overflow prediction:', error);
      setPrediction('Error fetching prediction');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const storedData = localStorage.getItem('binData');
    if (storedData) {
      setBinData(JSON.parse(storedData));
    }

    const interval = setInterval(() => {
      fetchBinData();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (binData.length > 0) {
      const latestData = binData[binData.length - 1];
      getOverflowPrediction(latestData.fillLevel, 10, 2);
    }
  }, [binData]);

  const binCoordinates = [
    { id: 1, lat: 28.5616, lng: 77.3259, fillLevel: binData.length > 0 ? binData[binData.length - 1].fillLevel : 0 },
  ];

  return (
    <div style={{ padding: '20px', backgroundColor: '#f4f4f4', borderRadius: '10px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
      <h3>Bin Fill Levels</h3>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={binData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis
            dataKey="time"
            tickFormatter={(timeStr) => {
              const date = new Date(timeStr);
              return date.toLocaleTimeString();
            }}
          />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="fillLevel" stroke="#8884d8" />
        </LineChart>
      </ResponsiveContainer>

      <MapContainer center={[28.5616, 77.3259]} zoom={12} style={{ height: '400px', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        {binCoordinates.map((bin) => (
          <Marker key={bin.id} position={[bin.lat, bin.lng]}>
            <Popup>
              Bin {bin.id} <br /> Fill Level: {bin.fillLevel}%
            </Popup>
          </Marker>
        ))}
      </MapContainer>

      {loading && <p>Loading prediction...</p>}

      {prediction && !loading && (
        <div>
          <h4>Predicted Time to Overflow: {prediction} minutes</h4>
        </div>
      )}

      {prediction === 'Error fetching prediction' && (
        <div>
          <h4>{prediction}</h4>
        </div>
      )}
    </div>
  );
};

export default BinStatus;