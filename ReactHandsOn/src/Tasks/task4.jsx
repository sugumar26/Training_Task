import React, { Component } from 'react';

class WeatherApi extends Component {
  constructor(props) {
    super(props);
    this.state = {
      city: '',
      weatherData: null,
    };
  }

  handleClick = async () => {
    const { city } = this.state;

    try {
      const response = await fetch(`https://weatherapi-com.p.rapidapi.com/current.json?q=${city}`, {
        method: 'GET',
        headers: {
          'X-RapidAPI-Key': 'ea1736c136msh0f5c187e704eedbp15d852jsn9c8eb45d2ffd',
          'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com',
        },
      });

      const data = await response.json();
      this.setState({ weatherData: data });
    } catch (error) {
      console.error('Error');
      this.setState({ weatherData: null });
    }
  };

  render() {
    const { city, weatherData } = this.state;

    return (
      <div>
        <h2>Weather Information</h2>
        <label htmlFor="city">Enter City: </label>
        <input
          type="text"
          id="city"
          value={city}
          onChange={(e) => this.setState({ city: e.target.value })}
        />
        <button onClick={this.handleClick}>Get Weather</button>
          <div>
            <h3>Weather Information for {city}</h3>
            <pre>{JSON.stringify(weatherData, null, 2)}</pre>
          </div>
      
      </div>
    );
  }
}

export default WeatherApi;
