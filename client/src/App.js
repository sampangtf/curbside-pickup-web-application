import React, { useState } from "react";
import NavBar from "./components/NavBar";
import Start from "./components/Start";
import Result from "./components/Result";
import NoResult from "./components/NoResult";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [customer, setCustomer] = useState({});
  const [keywords, setKeywords] = useState(["", ""]);
  const [searchResults, setSearchResults] = useState([[]]);

  const startSearch = () => {
    const url = `http://127.0.0.1:5000/search-results?k1=${keywords[0]}&k2=${keywords[1]}`;

    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        setSearchResults(data["results"]);
      });
  };

  const start = () => {
    // createCustomer();
    setLoggedIn(true);
    startSearch();
  };

  const createCustomer = () => {
    const url = `http://127.0.0.1:5000/customers?profileUsername=${customer.profileUsername}&mobile=${customer.mobile}&line1=${customer.line1}&line2=${customer.line2}&city=${customer.city}&state=${customer.state}&postalCode=${customer.postalCode}`;
    console.log(url);

    fetch(url)
      .then((res) => {
        console.log(typeof res);
        console.log(res);
        res.json();
      })
      .then((data) => console.log(data["results"]));
  };

  return (
    <div>
      {!loggedIn ? (
        <Start
          keywords={keywords}
          onKeywordInput={setKeywords}
          customer={customer}
          setCustomer={setCustomer}
          onSubmit={start}
        />
      ) : (
        <div>
          <NavBar
            keywords={keywords}
            onKeywordInput={setKeywords}
            onSubmit={startSearch}
          />
          {typeof searchResults === "string" ? (
            <NoResult keywords={keywords} />
          ) : (
            searchResults.map((result, i) => {
              return <Result key={i} restaurants={result} />;
            })
          )}
        </div>
      )}
    </div>
  );
}

export default App;
