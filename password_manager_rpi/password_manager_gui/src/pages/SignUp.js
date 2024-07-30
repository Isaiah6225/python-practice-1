import React from 'react';
import { useState } from "react";
import { Link } from 'react-router-dom';
import './SignUp.css';
import Login from './Login';


function SignUp() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');



  const handleSignup = async (e) => {
    e.preventDefault();
    
    const userData = {
      username: username,
      password: password
    };
    
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    try {
      const response = await fetch('/SignUp', {
        method: 'POST' ,
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
      });
      console.log(response.data)

      if (response.ok) {
        alert('Signup successful');
      } else {
        alert('Signup failed');
      }
      
    } catch (error) {
      console.error('Error signing up:', error);
      alert('Signup failed');
    }
  };


  return (
    <div className="signup-container">
      <form className="signup-form" onSubmit={handleSignup}>
        <h2>Sign Up</h2>
        <div className="input-group">
          <input
            type="name"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="input-group">
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div className="input-group">
          <input
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Sign Up</button>
        <Link to="/login">
          Already a member? Login
        </Link>
      </form>
    </div>
  );
}

export default SignUp;