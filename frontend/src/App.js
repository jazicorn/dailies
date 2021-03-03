import React, { Component } from "react";
import Root from "./Root"; 
import { Route, Switch } from "react-router-dom"; 
import Home from "./components/Home/Home";
import Signup from "./components/Signup/Signup";
import Login from "./components/Login/Login";
import Dashboard from "./components/Dashboard/Dashboard";

class App extends Component {
  render() {
    return (
      <div>
        <Root> 
          <Switch>
            <Route path="/signup" component={Signup} />
            <Route path="/login" component={Login} />
            <Route path="/dashboard" component={Dashboard} />
            <Route exact path="/" component={Home} />
          </Switch>
        </Root>
      </div>
    );
  }
}

export default App;