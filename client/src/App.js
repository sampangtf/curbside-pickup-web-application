import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      <form action="">
        <label htmlFor="">First Restaurant</label>
        <input type="text" placeholder="Fried chicken" />
        <label htmlFor="">Second Restaurant</label>
        <input type="text" placeholder="Boba tea" />
      </form>
    </div>
  );
}

export default App;
