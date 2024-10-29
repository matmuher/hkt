import './App.css';
import UsersRenderer from './UsersRenderer';
import UserProfileRenderer from './UserProfileRenderer';
import BookInfo from './BookInfo';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

const App = () => (
  <Router>
      <div>
        <Routes>
          <Route path="/" element={<UsersRenderer />} />
          <Route path="/profile/:user/:userId" element={<UserProfileRenderer/>} />
          <Route path="/book/:book/:bookId" element={<BookInfo />} />
        </Routes>
      </div>
    </Router>
);

export default App;
