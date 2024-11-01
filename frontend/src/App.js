import './App.css';
import UsersRenderer from './UsersRenderer';
import UserProfileRenderer from './UserProfileRenderer';
import BookInfo from './BookInfo';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import React, { useState } from 'react';
import './App.css';
import Search from './Search';

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [categories, setCategories] = useState(['Football', 'Volleyball', 'Floorball', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']);

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
            <div key={result.id} className="result-box">
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
