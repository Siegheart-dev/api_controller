import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

function ResultsPage() {
  const location = useLocation();
  const vinCode = new URLSearchParams(location.search).get('vin-code');
  const [make, setMake] = useState('');

  useEffect(() => {
    // Check if the VIN code is present and fetch the 'make' data
    if (vinCode) {
      fetch(`/carfax/?vin-code=${vinCode}`)
        .then((response) => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Error fetching data');
          }
        })
        .then((data) => {
          if (data.make) {
            setMake(data.make);
          } else {
            console.error('Make not found in response');
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
  }, [vinCode]);

  return (
    <div>
      <h2>Make Information</h2>
      {vinCode ? (
        make ? (
          <p>Make: {make}</p>
        ) : (
          <p>Loading...</p>
        )
      ) : (
        <p>No VIN code provided.</p>
      )}
    </div>
  );
}

export default ResultsPage;
