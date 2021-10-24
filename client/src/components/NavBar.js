import React from "react";
import "./NavBar.css";

function NavBar(props) {
  return (
    <nav className="navbar navbar-expand-md navbar-dark bg-dark">
      <div className="container-fluid">
        <a className="navbar-brand" href="/">
          Expand at md
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarsExample04"
          aria-controls="navbarsExample04"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <form
          className="collapse navbar-collapse"
          id="navbarsExample04"
          onSubmit={(e) => e.preventDefault()}
        >
          <ul className="navbar-nav me-auto mb-2 mb-md-0">
            <li className="nav-item">
              <input
                className="form-control"
                type="text"
                placeholder="First Restaurant"
                value={props.keywords[0]}
                onInput={(e) =>
                  props.onKeywordInput([e.target.value, props.keywords[1]])
                }
              />
            </li>
            <li className="nav-item">
              <input
                className="form-control"
                type="text"
                placeholder="Second Restaurant"
                value={props.keywords[1]}
                onInput={(e) =>
                  props.onKeywordInput([props.keywords[0], e.target.value])
                }
              />
            </li>
            <li>
              <i className="fas fa-plus-circle"></i>
            </li>
            <i className="fas fa-plus-circle"></i>
            <li>
              <button
                className="btn btn-large btn-primary"
                onClick={props.onSubmit}
              >
                Search
              </button>
            </li>
          </ul>
        </form>
      </div>
    </nav>
  );
}

export default NavBar;
