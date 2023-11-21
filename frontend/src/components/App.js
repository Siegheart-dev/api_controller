import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import SearchForm from './SearchForm.js';
import ResultsPage from './ResultsPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/carfax/results" component={ResultsPage} />
        <Route path="/carfax/?vin-code=" component={SearchForm} />
      </Switch>
    </Router>
  );
}

export default App;