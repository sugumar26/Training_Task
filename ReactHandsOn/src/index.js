import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import './style.css';
import './LoginForm.css';
import './loginpage.css';
import Logout from './Tasks/task6';
import App from './App';
import Signup from './Tasks/signup';
import Login from './Tasks/task5';
import {
  BrowserRouter as Router,
  Route,
  Link,
  Routes
} from "react-router-dom";  
import reportWebVitals from './reportWebVitals';

const RootComponent = () => {
  const [login, setLogin] = useState(false);

  const handleLogin = (response) => {
    if (response && response.code === 200) {
      setLogin(true);
    }
  };

  return (
    <div>
      <Router>
        {!login ? (
          <nav>
            <ul>
              <li>
                <Link to="/Login">Login</Link>
              </li>
              <li>
                <Link to="/signup">Signup</Link>
              </li>
              <li>
                <Link to="/Logout">Logout</Link>
              </li>
            </ul>
          </nav>
        ) : (
          <App/>
        )}
        <div>
          <Routes>
            <Route path="/Login" element={<Login onLogin={handleLogin} />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/logout" element={<Logout />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
};

const root = document.getElementById('root');
ReactDOM.createRoot(root).render(<RootComponent />);
reportWebVitals();
