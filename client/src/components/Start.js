import React from "react";
import "./Start.css";

function Start(props) {
  const inputFields = [
    "Username",
    "Phone number",
    "Street 1",
    "Street 2",
    "City",
    "State",
    "Postal Code",
  ];
  const inputRestaurants = ["First restaurant", "Second restaurant"];

  return (
    <div className="row">
      <div className="rol-md-6 account">
        <form>
          <h1 class="h3 mb-3 fw-normal">Account Information</h1>
          {inputFields.map((field, i) => (
            <div key={i} class="form-floating">
              <input
                type="text"
                class="form-control"
                id={field}
                placeholder="_"
              />
              <label for={field}>{field}</label>
            </div>
          ))}
        </form>
      </div>
      <div className="rol-md-6 food">
        <form onSubmit={(e) => e.preventDefault()}>
          <h1 class="h3 mb-3 fw-normal">Food </h1>

          <div class="form-floating right">
            <input
              type="text"
              class="form-control"
              id={inputRestaurants[0]}
              placeholder="_"
              value={props.keywords[0]}
              onInput={(e) => {
                props.onKeywordInput([e.target.value, props.keywords[1]]);
              }}
            />
            <label for={inputRestaurants[0]}>{inputRestaurants[0]}</label>
          </div>
          <div class="form-floating right">
            <input
              type="text"
              class="form-control"
              id={inputRestaurants[1]}
              placeholder="_"
              value={props.keywords[1]}
              onInput={(e) => {
                props.onKeywordInput([props.keywords[0], e.target.value]);
              }}
            />
            <label for={inputRestaurants[1]}>{inputRestaurants[1]}</label>
          </div>

          {/* <div class="checkbox mb-3">
            <label>
              <input type="checkbox" value="remember-me" /> Remember me
            </label>
          </div> */}
          <button class="w-100 btn btn-lg btn-primary" onClick={props.onSubmit}>
            Go!
          </button>
          {/* <p class="mt-5 mb-3 text-muted">&copy; 2017–2021</p> */}
        </form>
      </div>
    </div>
  );
}

export default Start;
