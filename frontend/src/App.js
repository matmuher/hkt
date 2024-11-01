import './App.css';
import UsersRenderer from './UsersRenderer';
import UserProfileRenderer from './UserProfileRenderer';
import BookInfo from './BookInfo';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [categories, setCategories] = useState(['Football', 'Volleyball', 'Floorball', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']);

  const [isMiniWindowOpen, setIsMiniWindowOpen] = useState(false);

  const handleClose = () => {
    setIsMiniWindowOpen(false);
    document.body.style.overflowY = ''; // Re-enable scrolling
  };

  const openMiniWindow = (description, x, y) => {
    setIsMiniWindowOpen(true);
    const miniWindow = document.createElement('div');
    miniWindow.className = 'mini-window';
    miniWindow.innerHTML = `
      <style>
        .mini-window {
          position: fixed;
          top: ${y}px;
          left: ${x}px;
          transform: translate(-50%, -50%);
          padding: 20px;
          border-radius: 5px;
          box-shadow: 0 2px 10px rgba(0,0,0,0.1);
          z-index: 9999;
        }
        .close-btn {
          position: absolute;
          top: 10px;
          right: 10px;
          cursor: pointer;
        }
      </style>
      <p>${description}</p>
      <button class="close-btn">Close</button>
    `;

    document.body.appendChild(miniWindow);

    const closeBtn = miniWindow.querySelector('.close-btn');
    closeBtn.addEventListener('click', () => {
      setIsMiniWindowOpen(false);
      miniWindow.remove();
    });

    // Prevent scrolling on the page behind the mini-window
    document.body.style.overflowY = 'hidden';
  };


  const searchResults = [
    { id: 1, title: 'Football' },
    { id: 2, title: 'Volleyball' },
    { id: 3, title: 'Floorball' },
    { id: 4, title: 'Hockey' },
    { id: 5, title: 'Backetball' },
    { id: 6, title: 'Regbi' },
    { id: 7, title: 'Dance' },
    { id: 8, title: 'Skating' },
    { id: 9, title: 'Kerling' },
    { id: 10, title: 'BobSlay' },
  ];

  return (
    <div className="app-container">
      {/* Search Bar */}
      <div className="search-bar" >
        <button>
          Filter
        </button>
        <span>
          <input
            type="text"
            placeholder="Search cashbacks..."
            onChange={(e) => setSearchTerm(e.target.value)}
            value={searchTerm}
            width="10%"
          />
        </span>
      </div>

   
      {/* Search Area and Categories Container */}
      <div className="search-category-container">
        {/* Category Area */}
        <div className="category-area">
          {categories.map((category, index) => (
            <div key={index} className="category-button"> <p> {category} </p></div>
          ))}
        </div>

        {/* Search Results Area */}
        <div className="search-results-area">
          {searchResults.filter(result => 
            !searchTerm || result.title.toLowerCase().includes(searchTerm.toLowerCase())
          ).map(result => (
            <div key={result.id} className="result-box"  style={{position: 'relative'}}
            onClick={(e) => {
              const rect = e.currentTarget.getBoundingClientRect();
              openMiniWindow(result.id, (rect.left + rect.right)/2, (rect.bottom + rect.top)/2);
            }}>
              <p>{result.title}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;

// const App = () => (
//   <Router>
//       <div>
//         <Routes>
//           <Route path="/" element={<UsersRenderer />} />
//           <Route path="/profile/:user/:userId" element={<UserProfileRenderer/>} />
//           <Route path="/book/:book/:bookId" element={<BookInfo />} />
//         </Routes>
//       </div>
//     </Router>
// );

// export default App;
