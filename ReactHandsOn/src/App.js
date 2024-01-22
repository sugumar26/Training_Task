import React, { Component } from 'react';
import Addnumber from './Tasks/task2';
import Tableform from './Tasks/task1';
import Jsondata from './Tasks/task3';
import WeatherApi from './Tasks/task4';
import './App.css';

class App extends Component {
  render() {
    const currentPath = window.location.pathname;
    
    return (
      <div>
        <h3>Add Number</h3>
        <Addnumber/>
        <h3>Table&Form</h3>
        <Tableform/>
        <h3>Jsondata</h3>
        <Jsondata/>
        <h3>WeatherApi</h3>
        <WeatherApi/>

      </div>
    );
  }
}

export default App;
