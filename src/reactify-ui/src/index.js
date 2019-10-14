import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Windows from './Windows';

// import registerServiceWorker from './registerServiceWorker';
ReactDOM.render(<App />, document.getElementById('content'));
ReactDOM.render(<Windows />, document.getElementById('root'));
// registerServiceWorker();
