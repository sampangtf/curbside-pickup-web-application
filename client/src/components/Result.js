import React from "react";
import "./Result.css";

function Result(props) {
  return (
    <div className="row row-cols-1 row-cols-md-3 mb-3 text-center">
      {props.restaurants.map((res, i) => (
        <div className="col">
          <div className="card mb-4 rounded-3 shadow-sm">
            <div className="card-header py-3">
              <h4 className="my-0 fw-normal">
                {i === 0 ? "1st restaurant" : "2nd restaurant"}
              </h4>
            </div>
            <div className="card-body">
              <h1 className="card-title pricing-card-title">{res.siteName}</h1>
              <ul className="list-unstyled mt-3 mb-4">
                <li>10 users included</li>
                <li>Help center access</li>
              </ul>
              <button
                type="button"
                className="w-100 btn btn-lg btn-outline-primary"
              >
                Order
              </button>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Result;
