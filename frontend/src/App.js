import React, { useState, useEffect} from 'react';
import './App.css';

function resizeBase64Image(base64String, maxWidth = 30, maxHeight = 30) {
  const base64Data = base64String;

  // Create an Image object
  const img = new Image();
  img.src = `data:image/png;base64,${base64Data}`;

  return new Promise((resolve, reject) => {
    img.onload = () => {
      // Calculate aspect ratio
      let width = img.width;
      let height = img.height;

      // Maintain aspect ratio
      if (width > height) {
        height *= maxWidth / width;
        width = maxWidth;
      } else {
        width *= maxHeight / height;
        height = maxHeight;
      }

      // Create canvas
      const canvas = document.createElement('canvas');
      canvas.width = width;
      canvas.height = height;

      // Draw image on canvas
      const ctx = canvas.getContext('2d');
      ctx.drawImage(img, 0, 0, width, height);

      // Convert canvas to base64 string
      resolve(canvas.toDataURL());
    };
    img.onerror = reject;
  });
}

const App = () => {

  const handleImageResize = async (imageBase64) => {
    try {
      const resizedImage = await resizeBase64Image(imageBase64);
      return resizedImage;
    } catch (error) {
      console.error('Error resizing image:', error);
    }
  };

  const [searchResults, setSearchResults] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      try {
        const url = 'http://0.0.0.0:80/search';
        const data = { "session_id": "123456789" };
        const response = await fetch(url, {
          method: 'POST',
          body: JSON.stringify(data),
          headers: { 'Content-Type': 'application/json' },
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const searchData = await response.json();
        const resizedImages = await Promise.all(
          searchData.map(async (result) => await handleImageResize(result.image))
        );
        setSearchResults(searchData.map((result, index) => ({
          ...result,
          resizedImage: resizedImages[index],
        })));
      } catch (error) {
        console.error('Error fetching or resizing images:', error);
      }
    };

    fetchData();
  }, []);

  const [searchTerm, setSearchTerm] = useState('');
  const [categories, setCategories] = useState(['Продукты',
                                                'Одежда',
                                                'Техника',
                                                'Настольные игры',
                                                'Цветы',
                                                'Путешествия']);

  const [isMiniWindowOpen, setIsMiniWindowOpen] = useState(false);

  const handleClose = () => {
    setIsMiniWindowOpen(false);
    document.body.style.overflowY = '';
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
          {searchResults.map(result => (
            <div key={result.description} className="result-box-area"  style={{position: 'relative'}}
            onClick={(e) => {
              const rect = e.currentTarget.getBoundingClientRect();
              openMiniWindow(result.description, (rect.left + rect.right)/2, (rect.bottom + rect.top)/2);
            }}>
              {/* Left Logo */}
              <div className='left-logo'>
                <img src={result.resizedImage}/>
              </div>

              {/* Card Header */}
              <div className='card-header'>
                <p>{result.header}</p>
              </div>

              {/* Right Logo */}
              <div className='right-logo'>
                <img src={`${result.resizedImage}`} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default App;
