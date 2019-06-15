import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'

import Page from '@/components/Page';

import Index from './index';
import Users from './users';
import Techgroups from './techgroups';

class App extends Component {
  render() {
    const { Component, pageProps } = this.props
    return (
      <Page>
        <Switch>
          <Route exact path="/" component={Index}/>
          <Route path="/users" component={Users}/>
          <Route path="/techgroups" component={Techgroups}/>
        </Switch>
      </Page>
    );
  }
}

export default App;
