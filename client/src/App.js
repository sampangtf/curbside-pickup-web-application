import React, { useState } from "react";
import NavBar from "./components/NavBar";
import Start from "./components/Start";
import Result from "./components/Result";
import NoResult from "./components/NoResult";
import Order from "./components/Order";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [customerInput, setCustomerInput] = useState({});
  const [customer, setCustomer] = useState({});
  const [keywords, setKeywords] = useState(["", ""]);
  const [searchResults, setSearchResults] = useState([[]]);
  const [searchStarted, setSearchStarted] = useState(false);
  const [searched, setSearched] = useState(false);
  const [ordered, setOrdered] = useState(false);
  const [order, setOrder] = useState({});

  // Create new customer and start result search
  const start = () => {
    createCustomer();
    setLoggedIn(true);
    setSearchStarted(true);
    startSearch();
  };

  // Post to Python API to create new customer
  const createCustomer = () => {
    fetch("http://127.0.0.1:5000/customers", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(customerInput),
    })
      .then((res) => res.json())
      .then((data) => setCustomer(data["results"]));
  };

  // Call Python backend for searched results
  const startSearch = () => {
    const url = `http://127.0.0.1:5000/search-results?k1=${keywords[0]}&k2=${keywords[1]}`;

    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        const results = data["results"];

        console.log(results);
        // setSearchResults(results);

        // console.log(typeof searchResults);
        // console.log(searchResults);

        if (typeof results !== "string") {
          var res = [];
          for (var i = 0; i < results["distance_list"].length; i++) {
            const result = {
              restaurants: results["combinations"][i],
              distance: results["distance_list"][i],
              avg_rating: results["avg_rating_list"][i],
            };
            res.push(result);
          }
          console.log(res);
          setSearchResults(res);
          setSearched(true);
        }
      });
  };

  // Call Python backend to create new order
  const placeOrder = () => {
    fetch("http://127.0.0.1:5000/orders", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(order),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data["results"]);
        setOrder(data["results"]);
        setOrdered(true);
      });
  };

  if (!loggedIn) {
    return (
      <div>
        <Start
          keywords={keywords}
          onKeywordInput={setKeywords}
          customer={customerInput}
          setCustomer={setCustomerInput}
          onSubmit={start}
        />
      </div>
    );
  } else if (searchStarted && !searched) {
    return (
      <div>
        <NavBar
          keywords={keywords}
          onKeywordInput={setKeywords}
          onSubmit={startSearch}
        />
        {typeof searchResults === "string" ? (
          <NoResult keywords={keywords} />
        ) : (
          <p>Loading...</p>
        )}
      </div>
    );
  } else if (searched && !ordered) {
    return (
      <div>
        <NavBar
          keywords={keywords}
          onKeywordInput={setKeywords}
          onSubmit={startSearch}
        />
        {searchResults.map((result, i) => {
          return <Result key={i} combination={result} onOrder={placeOrder} />;
        })}
      </div>
    );
  } else if (ordered) {
    return (
      <div>
        <Order order={order} />
      </div>
    );
  }
}

export default App;
