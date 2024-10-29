import { React, useEffect, useState } from "react";
import { useParams, useNavigate } from 'react-router-dom';

function DeleteBook(book) {
  const data = {id: book}

  fetch('http://51.250.103.111:80/delete-book', {
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

function UserProfileRenderer() {
  const { user, userId } = useParams();

  const navigate = useNavigate();
  const [books, setBooks] = useState([]);
  const [inputValue, setInputValue] = useState('');


  const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

  const ff = () => {
      fetch('http://51.250.103.111:80/books', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ id: userId }),
      })
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
            setBooks(data || []);
          } catch (parseError) {
            console.error('Failed to parse JSON:', parseError);
          }
        })
        .catch(error => {
          console.log("Fetch error:", error);
        });
    }

  useEffect(ff, []);

  const handleDelete = async (bookId) => {
      await DeleteBook(bookId);
      await delay(100);
      await ff();
    };
  const onClickAddBook = async (userId) => {
    const input = inputValue.trim();

    if (!input) {
      alert('Please enter book name');
      return;
    }

    if (input.length < 2 || input.length > 64) {
      alert('Name should be from 2 to 64 symbols');
      return;
    }

    const pattern = /^[a-zA-Z0-9\s]*$/;
    if (!pattern.test(input)) {
      alert('Use only latin letters, digits or spaces');
      return;
    }

    try {
      const response = await fetch('http://51.250.103.111:80/add-book', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: inputValue, "user": { id: userId } }),
      });
      const data = await response.json();
      if (data["code"] === 404) {
        alert('something strange');
        throw new Error();
      } else if (data["code"] === 403) {
        throw new Error();
      }
      console.log(data);
      setInputValue('');
    } catch (error) {
      console.error('Error adding book:', error);
      alert('Book exists');
    }
  };

  const handleAdd = async (userId) => {
    await onClickAddBook(userId);
    await delay(100);
    await ff();
  };
    
      return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '50px' }}>
          <h1>{user}</h1>
          <input 
            type="text" 
            placeholder="Add book" 
            value={inputValue} 
            onChange={(e) => setInputValue(e.target.value)}
            style={{ margin: '10px' }} />
          <button onClick={() => handleAdd(userId)}>Add book</button>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '50px' }}>
        {books.map(book => (
          <div key={book["id"] + 999}>
          <button 
            key={book["name"]}
            onClick={() => navigate(`/book/${book["name"]}/${book["id"]}`)}
            style={{ margin: '5px' }}>
            {book["name"]}
          </button>
          <button 
            key={book["name"] + "as"}
            onClick={() => {
              handleDelete(book["id"])}}
              style={{ margin: '5px' }}>
            -
          </button>
        </div>
        ))}
      </div>
        </div>
      );
}

export default UserProfileRenderer;