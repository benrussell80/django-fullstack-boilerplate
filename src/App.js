import React from 'react';
// import { Navigation } from './common/components/Navigation';
import './App.css'
import ErrorRoutes from './errors/routes';
import { Switch } from 'react-router-dom';
// import { Footer } from './common/components/Footer';
import 'bootstrap/dist/css/bootstrap.min.css';
import BlogRoutes from './blog/routes';

const App = (props) => {
  return (
    <div id="main">
      <div id="content">
        <Switch>
          {/* {AccountsRoutes} */}
          {BlogRoutes}
          {ErrorRoutes}
        </Switch>
      </div>
    </div>
  );
}

export default App;