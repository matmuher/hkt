import React, {useState, useEffect} from "react";
import { useParams } from 'react-router-dom';

function DeleteNote(note) {
    const data = {id: note}
  
    fetch('http://51.250.103.111:80/delete-note', {
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

function BookInfo() {
    const {book, bookId} = useParams()

    const [notes, setNotes] = useState([]);
  
      const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
  
      const ff = () => {
        fetch('http://51.250.103.111:80/notes', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ id: bookId }),
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
              setNotes(data || []);
            } catch (parseError) {
              console.error('Failed to parse JSON:', parseError);
            }
          })
          .catch(error => {
            console.log("Fetch error:", error);
          });
      }
  
      const handleDelete = async (noteId) => {
        await DeleteNote(noteId);
        await delay(100);
        await ff();
      };
  
      useEffect(ff, []);

    const [chapterTitle, setChapterTitle] = useState('');
    const [comment, setComment] = useState('');

    const handleAddNote = async () => {
        // check chapter name

        const chapter = chapterTitle.trim();

        if (!chapter) {
            alert('Please enter note header');
            return;
        }

        if (chapter.length > 64) {
            alert('Note header cannot be more than 64 symbols');
            return;
        }

        // check comment

        const com = comment.trim();

        if (!com) {
            alert('Comment should not be empty');
            return;
        }

        if (com.length > 512) {
            alert('Comment cannot be more than 64 symbols');
            return;
        }

        // Логика добавления заметки
        try {
            const response = await fetch('http://51.250.103.111:80/add-note', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ name: chapter, txt: com, book: {id: bookId} }),
            });
            const data = await response.json();
            if (data["code"] === 404) throw new Error();
            console.log(data);
          } catch (error) {
            alert('Error while adding note' + error);
          }
        // Сброс полей после добавления заметки
        setChapterTitle('');
        setComment('');
    }

    const handleAdd = async () => {
        await handleAddNote();
        await delay(100);
        await ff();
      };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '50px' }}>
          <h1>{book}</h1>
          <input 
            type="text" 
            value={chapterTitle} 
            placeholder="Введите название главы" 
            onChange={(e) => setChapterTitle(e.target.value)}
            style={{ margin: '10px' }} 
          />
          <textarea 
            value={comment} 
            placeholder="Введите комментарий" 
            onChange={(e) => setComment(e.target.value)}
            style={{ margin: '10px', width: '300px', height: '200px' }} 
          />
          <button onClick={handleAdd}>Add note</button>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '50px' }}>
        {notes.map((note) => (
          <div key={note["id"]} style={{ margin: '10px', padding: '10px', border: '1px solid #ccc', width: '500px' }}>
            <h3>{note["name"]}</h3>
            <p>{note["txt"]}</p>
            <button onClick={() => { handleDelete(note["id"]) }}>Delete</button>
          </div>
        ))}
      </div>
        </div>
    )
}

export default BookInfo;