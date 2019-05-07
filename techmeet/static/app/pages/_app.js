import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'

import GlobalStyle from '@/components/styles/GlobalStyle';
import Header from '@/components/Header';

import Index from './index';
import Users from './users';
import Groups from './groups';
import Techgroups from './techgroups';

class App extends Component {
  render() {
    const { Component, pageProps } = this.props
    return (
      <div className="App">
        <GlobalStyle/>
        <Header/>

        <Switch>
          <Route exact path="/app" component={Index}/>
          <Route path="/app/users" component={Users}/>
          <Route path="/app/groups" component={Groups}/>
          <Route path="/app/techgroups" component={Techgroups}/>
        </Switch>
      </div>
    );
  }
}

export default App;
