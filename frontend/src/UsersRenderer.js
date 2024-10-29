import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function DeleteUser(user) {
  const data = {id: user}

  fetch('http://51.250.103.111:80/delete-user', {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
        })
        .catch(error => {
          console.log("Fetch error:", error);
        });
}

function UsersRenderer() {
  const [inputValue, setInputValue] = React.useState('');

  const navigate = useNavigate();
    const [users, setUsers] = useState([]);

    const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

    const ff = () => {
      fetch('http://51.250.103.111:80/users')
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          return response.text();
        })
        .then(text => {
          console.log('Raw response:', text);
          try {
            const data = JSON.parse(text);
            setUsers(data || []);
          } catch (parseError) {
            console.error('Failed to parse JSON:', parseError);
          }
        })
        .catch(error => {
          console.log("Fetch error:", error);
        });
    }

    const handleDelete = async (userId) => {
      await DeleteUser(userId);
      await delay(100);
      await ff();
    };

    useEffect(ff, []);

  const onClickAddUser = async () => {
    const input = inputValue.trim();

    if (!input) {
      alert('Please enter a name');
      return;
    }

    if (input.length < 4 || input.length > 32) {
      alert('Name should be from 4 to 32 symbols');
      return;
    }

    const pattern = /^[a-zA-Z0-9\s]*$/;
    if (!pattern.test(input)) {
      alert('Use only latin letters, digits or spaces');
      return;
    }

    try {
      const response = await fetch('http://51.250.103.111:80/add-user', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: inputValue }),
      });
      const data = await response.json();
      if (data["code"] === 404) throw new Error();
      console.log(data);
      setInputValue('');
    } catch (error) {
      console.error('Error adding user:', error);
      alert('User exists');
    }
  };

  const handleAdd = async () => {
    await onClickAddUser();
    await delay(100);
    await ff();
  };


  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '50px' }}>
          <h1>Reading Diary</h1>
          <input 
            type="text" 
            placeholder="Add user" 
            value={inputValue} 
            onChange={(e) => setInputValue(e.target.value)}
            style={{ margin: '10px' }} />
          <button 
            onClick={handleAdd}>
              Add user
          </button>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '50px' }}>
        {users.length > 0 ? (
          users.map(user => (
            <div key={user["id"]}>
              <button 
                onClick={() => navigate(`/profile/${user["name"]}/${user["id"]}`)}
                style={{ margin: '5px' }}>
                {user["name"]}
              </button>
              <button 
                onClick={() => {
                  handleDelete(user["id"])}}
                  style={{ margin: '5px' }}>
                -
              </button>
            </div>
          ))
        ) : (
          <p>No users available</p>
        )}
      </div>
    </div>
  )
}

export default UsersRenderer;
