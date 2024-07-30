import React from 'react';
import ReactDOM from 'react-dom/client';
import { useState } from "react";
import {Link} from 'react-router-dom';
import './Login.css';

function Login(){
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
  
    const handleLogin = async (e) => {
      e.preventDefault();
      const user_info = {
        username: username,
        password: password
      };
           
      try {
        const response = await fetch('/login', {
          method: 'POST',
          headers: {
            'Content-Type' : 'application/json',
          },
          body: JSON.stringify(user_info),
        });
  
        if (response.ok) {
          // alert('Login successful');
          /*route user to the home page*/
          window.location.replace('/home');
        } else {
          alert('Login failed');
        }
      } catch (error) {
        console.error('Error logging in:', error);
        alert('Login failed');
      }
    };
  
    return (
      <div className="login-container">
       

        <form className="login-form" onSubmit={handleLogin}>
          <h2>Login</h2>
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
          
          <button type="submit">Login</button>
           
          < Link to = "/SignUp"><a href="">Not a member? 
          Sign Up</a>
          </Link>
        </form>
      </div>
    );
  

}

export default Login ;