import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = ({onLogin}) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const navigate = useNavigate();

  const handleLogin = async () => {
    if (!email || !password) {
      setError('Please fill in all fields');
      return;
    }
    const apiUrl = 'https://app.qualdo.ai/iam/login';

    try {
      let data = JSON.stringify({ email, password });
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Api-Type': 'qualdo_db_auth',
        },
        body: data,
      });
      const result = await response.json();

      if (result.code === 200) {
        localStorage.setItem('auth_token', result.auth_token);
        setIsAuthenticated(true);
        navigate('/App');
        onLogin(result)
      } else {
        setError(result.message);
        onLogin(result)
      }
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  if (isAuthenticated) {
    navigate('/App');
    return null;
  }

  return (
    <div>
      <h2>Login</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <label>Email:</label>
      <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <br />
      <label>Password:</label>
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <br />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;
