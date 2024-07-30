import React from 'react';
import './Table.css';

function Table({data}){
    return(
        <table className='table'> 
            <thead>
            <tr>
                    <th>Purpose</th>
                    <th>Username</th>
                    <th>Password</th>
                </tr>
            </thead>
            <tbody>
                {data.map((item, index)=> 
                <tr key={index}>
                    <td>{item.passwordPurpose}</td>
                    <td>{item.userUserName}</td>
                    <td>{item.userPassword}</td>
                </tr>
            )}
            </tbody>
        </table>
    );
};

export default Table;