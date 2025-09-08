import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const RouteMap = () => {
  const position = [28.6139, 77.2090]; // Example: Delhi coordinates

  return (
    <div>
      <h3>Optimized Route</h3>
      <MapContainer center={position} zoom={13} style={{ height: "300px", width: "100%" }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <Marker position={position}>
          <Popup>Optimized Route Point</Popup>
        </Marker>
      </MapContainer>
    </div>
  );
};

export default RouteMap;
