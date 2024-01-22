// Signup.js
import React, { Component } from 'react';

class Signup extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: '',
      password: '',
      confirmPassword: '',
      error: '',
    };
  }

  handleSignup = async () => {
    const { email, password, confirmPassword } = this.state;
    if (!email || !password || !confirmPassword) {
      this.setState({ error: 'Please fill in all fields' });
      return;
    }

    if (password !== confirmPassword) {
      this.setState({ error: 'Passwords do not match' });
      return;
    }

    const apiUrl = 'https://dev-qualdo.eastus.cloudapp.azure.com/iam/signup';

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (response.ok) {
        console.log('Signup successful');
      } else {
        const errorMessage = await response.text();
        console.error('Signup failed. Error:', errorMessage);
        this.setState({ error: 'Signup failed. Please try again.' });
      }
    } catch (error) {
      console.error('Error during signup:', error);
      this.setState({ error: 'An unexpected error occurred.' });
    }
  };

  render() {
    const { email, password, confirmPassword, error } = this.state;

    return (
      <div>
        <h2>Signup</h2>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <label>Email:</label>
        <input type="email" value={email} onChange={(e) => this.setState({ email: e.target.value })} />
        <br />
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => this.setState({ password: e.target.value })}
        />
        <br />
        <label>Confirm Password:</label>
        <input
          type="password"
          value={confirmPassword}
          onChange={(e) => this.setState({ confirmPassword: e.target.value })}
        />
        <br />
        <button onClick={this.handleSignup}>Signup</button>
        <button >Signin</button>
      </div>
    );
  }
}

export default Signup;
