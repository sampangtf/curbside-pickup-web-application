import React from "react";
import "./Order.css";

function Order(props) {
  return (
    <div className="container">
      <h1 className="display-3">Order successfully placed!</h1>
      <p>
        <strong>Order ID: </strong>
        {props.order.id}
      </p>
      <p>
        <strong>Time Created: </strong>
        {props.order.dateCreated}
      </p>
      <p>
        <strong>Status: </strong>
        {props.order.status}
      </p>
    </div>
  );
}

export default Order;
