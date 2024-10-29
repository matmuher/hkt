import React from "react";
import { useParams, } from "react-router-dom";

function BookRenderer() {
    const {user} = useParams();

    const onClickAddBook = (user) => {
        alert('book added to user ' + user)
    };
    
      return (
        <div>
          <div>
                <input type="text" name="firstName"/>
                <button onClick={onClickAddBook(user)}>
                    Add book
                </button>
                
                <BookList></BookList>
              </div>
        </div>
      );
}

export default BookRenderer;