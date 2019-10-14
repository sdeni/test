import React, { Component } from 'react';
import { BrowserRouter, Route, Redirect, Switch} from 'react-router-dom'
import './App.css';

import Posts from './posts/Posts';
import Payment from "./payment/Payment";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
          <Switch>
            <Route exact path='/payment/' component={Payment}/>
            <Route component={Posts}/>
          </Switch>
      </BrowserRouter>
    );
  }
}

export default App;