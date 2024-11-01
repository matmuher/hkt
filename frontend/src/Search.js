import React, { useState } from 'react';

function Search() {

  const [searchField, setSearchField] = useState("");
  const [searchShow, setSearchShow] = useState(true);

  const handleChange = e => {
    setSearchField(e.target.value);
    if(e.target.value===""){
      setSearchShow(false);
    }
    else {
      setSearchShow(true);
    }
  };


  return (
    <section className="garamond">
			<div className="pa2">
				<input
					className="pa3 bb br3 grow b--none bg-lightest-blue ma3"
					type = "search"
					placeholder = "Search cashback"
					onChange = {handleChange}
				/>
			</div>
		</section>
  );
}

export default Search;