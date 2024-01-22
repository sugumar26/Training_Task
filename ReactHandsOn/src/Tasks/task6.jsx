import React from 'react';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();

  const handleRedirect = () => {
    navigate('/login');
  };

  return (
    <div>
      <h1>Are you trying to logout ?</h1>
      <button onClick={handleRedirect}>Log out</button>
    </div>
  );
};

export default Logout;
