import React, { useState } from "react";
import "./App.css";
import * as mobilenet from "@tensorflow-models/mobilenet";
import robot from "./assets/robot.jpg";

import "./firebase";
import { storage } from "firebase";
import firebase from "firebase/app";

const App = () => {
  const [image, setImage] = useState([]);
  const [url, setURL] = useState("");
  const [predictions, handlePredictions] = useState([]);
  const [spinner, handleSpinner] = useState(true);

  const showSpinner = () => {
    if (url === "" && spinner === true) {
      setURL(robot);
      handleSpinner(false);
    } else {
      handleSpinner(true);
    }
  };

  const handleImage = async e => {
    setImage(e);

    await db.put(e);

    db.getDownloadURL().then(e => setURL(e));
  };
  const db = storage().ref("/UserPics/" + Math.random());
  const dbResults = () => firebase.database();

  const myRealPrediction = async () => {
    const loadModel = await mobilenet.load();
    const img = document.getElementById("image");
    img.setAttribute("crossOrigin", "");
    console.log(img);
    await loadModel.classify(img).then(function (p) {
      // Classify the image
      console.log("Predictions: ", image, p);
      handlePredictions(p);
    });

    handleSpinner(true);
  };

  const handleResults = async val => {
    await dbResults().ref("/").push({ val });
  };

  handleResults(predictions);
  return (
    <div className="App">
      <h1>Machine Learning real time image classification </h1>

      <br />
      <h2>Browse and Upload an image: </h2>

      <input
        className="button"
        type="file"
        onChange={e => handleImage(e.target.files[0])}
        onClick={e => {
          showSpinner();
          handleImage(e.target.files[0]);
        }}
      />

      <br />

      <hr />

      <button
        className="button"
        onClick={() => {
          myRealPrediction();
          showSpinner();
        }}
      >
        Classification:
      </button>
    <br />
      <img
        id="image"
        src={url}
        alt=""
        height="500"
        width="500"
        crossOrigin="anonymous"
      />
      <h1>AI Classification:</h1>
      {predictions.map((e, k) => (
        <span key={k}>
          <h5>{e.className + ": " + Math.round(e.probability * 100) + "%"}</h5>
        </span>
      ))}
      <br />
    </div>
  );
};

export default App;
