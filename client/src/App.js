import React, { useState, useEffect } from "react";
import NavBar from "./components/NavBar";
import Result from "./components/Result";

function App() {
  const [data, setData] = useState([[]]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/search-results")
      .then((res) => res.json())
      .then((data) => {
        setData(data["results"]);
        console.log(data);
      });
  }, []);

  return (
    <div>
      <NavBar />
      {data.map((result, i) => {
        return <Result key={i} restaurants={result} />;
      })}
    </div>
  );
}

export default App;
