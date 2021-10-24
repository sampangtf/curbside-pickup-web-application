import React from "react";
import "./NoResult.css";

function NoResult(props) {
  return (
    <div className="container con">
      <h1 className="display-3">Oops!</h1>
      <p>
        Your search -{" "}
        <strong style={{ color: "red" }}>
          [{`${props.keywords[0]}, ${props.keywords[1]}`}]
        </strong>{" "}
        - did not match any restaurants.
        <br />
        <br />
        Suggestions:
        <br />
        Make sure all words are spelled correctly.
        <br />
        Try different keywords.
        <br />
        Try more general keywords.
      </p>
    </div>
  );
}

export default NoResult;
