// SearchForm.js

// Import any necessary dependencies
import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

// Define your SearchForm component
function SearchForm() {
  const [vinCode, setVinCode] = useState('');
  const history = useHistory();

  const handleInputChange = (event) => {
    setVinCode(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    try {
      const response = await fetch(`/carfax/?vin-code=${vinCode}`);
      if (response.ok) {
        const data = await response.json();
        // Handle the 'make' data as needed
        console.log('Make:', data.make);
      } else {
        console.error('Error fetching data:', response.statusText);
      }
    } catch (error) {
      console.error('Error:', error);
    }

    history.push(`/results/?vin-code=${vinCode}`);
  };

  // Define a render function to generate the HTML content
  const render = () => {
    return (
      <div>
        <h2>Search By Vin Code</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="vin-code"
            value={vinCode}
            onChange={handleInputChange}
          />
          <button type="submit">Search</button>
        </form>
      </div>
    );
  };

  return {
    // Return the render function so it can be used externally
    render,
  };
}

export default SearchForm;
