import React from "react";
import "./Result.css";

function Result(props) {
  return (
    <div className="row row-cols-1 row-cols-md-1 mb-3 text-center cards">
      <div className="col-md-8 results">
        <div className="card mb-4 rounded-3 shadow-sm">
          <div className="card-body row">
            {props.combination.map((res, i) => (
              <div key={i} className="col-md-6 restaurant">
                <p className="index">
                  {i === 0 ? "1st restaurant" : "2nd restaurant"}
                </p>
                <div className="row">
                  <div className="col-md-9 restaurant-name">
                    <h3 className="card-title pricing-card-title">
                      {res.restaurant.siteName}
                    </h3>
                  </div>
                  <div className="rating col-md-3">
                    <p>9.0</p>
                  </div>
                </div>
                <div className="details">
                  <p className="details-text">
                    <strong>Address: </strong>
                    {res.restaurant.address.street}
                  </p>
                  <p className="details-text">
                    <strong>Cuisine: </strong>
                    {res.restaurant.description.substring(0, 30) +
                      (res.restaurant.description.length > 30 ? "..." : "")}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className="col-md-4 order">
        <p>
          <strong>Total distance: </strong>1.5 mi
        </p>
        <button
          type="button"
          className="w-100 btn btn-lg btn-success"
          onClick={props.onOrder}
        >
          Order
        </button>
      </div>
    </div>
  );
}

export default Result;
