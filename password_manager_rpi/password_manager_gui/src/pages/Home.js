import React from 'react';
import './Home.css';
import Table from '../components/Table.js';
import {useState} from 'react';

function Home() {
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [tableData, setTableData] = useState([]);
  const [passwordPurpose, setPasswordPurpose] = useState('');
  const [userUserName, setUserUserName] = useState('');
  const [userPassword, setUserPassword] =useState('');

  const handlePasswordPurpose = (e) => {
    setPasswordPurpose(e.target.value);
  }

  const handleUserUserName = (e) => {
    setUserUserName(e.target.value);
  }

  const handleUserPassword = (e) => {
    setUserPassword(e.target.value);
  }


  const handleSubmit = async (e) => {
    e.preventDefault();

    const userInfo = {
      passwordPurpose: passwordPurpose,
      userUserName: userUserName,
      userPassword: userPassword
    };

    if(!passwordPurpose || !userUserName || !userPassword){
        alert('Please fill out all fields');
        return;
    }
    
    try {
      const response = await fetch('/home', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(userInfo)
      });
      
      if( response.ok){
        alert('Thank you for entering your data!');
      } else {
        alert('Data not received');
      }

    } catch(error){
      console.error('Error filling out form:', error);
      alert('Data not recieved');
    }
    // Add the input value to the table data array
    setTableData([...tableData, {passwordPurpose, userUserName, userPassword}]);
    setPasswordPurpose(''); // Clear input value after submitting
    setUserPassword(''); 
    setUserUserName(''); 
    setIsFormVisible(false); // Hide the form after submitting
  
  }

  const toggleFormVisibility = () => {
    setIsFormVisible(prevState => !prevState);
  }


    return(
        <div className='home-container'>
            <div className='header'>
                <h1>Password Manager</h1>
                <button className='add-password-button' onClick={toggleFormVisibility}>
                        Add password
                </button>
            </div>

            {isFormVisible && (
            <form className='password-form' onSubmit={handleSubmit}>
                <h2>Enter Information</h2>

                <div className='input-group'>
                    <input
                    type="organization"
                    value={passwordPurpose}
                    onChange={handlePasswordPurpose}
                    placeholder="What organization is this for?"
                    />
                </div>

                <div className='input-group'>
                <input
                    type="username"
                    value={userUserName}
                    onChange={handleUserUserName}
                    placeholder="What is the username or email?"
                    />
                </div>

                <div className='input-group'>
                <input
                    type="password"
                    value={userPassword}
                    onChange={handleUserPassword}
                    placeholder="Enter the password to be saved."
                    />
                </div>

                <button type="submit">Submit</button>
            </form>
            )}
            <Table data={tableData} />
        </div>

    );
};

export default Home;