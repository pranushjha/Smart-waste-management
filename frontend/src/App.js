import React from 'react';
import BinStatus from './components/BinStatus';  // Import the BinStatus component

function App() {
  return (
    <div className="App">
      <h1>Welcome to the Bin Management System</h1>
      <BinStatus />  {/* Add the BinStatus component here */}
    </div>
  );
}

export default App;
