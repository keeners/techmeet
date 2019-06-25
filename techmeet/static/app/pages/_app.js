import React, { Component } from "react"
import { Switch, Route } from "react-router-dom"

import Page from "@/components/Page"
import NotFound from "./404"
import Index from "./index"
import Users from "./users"
import User from "./user"
import Techgroups from "./techgroups"

class App extends Component {
  render() {
    const { Component, pageProps } = this.props
    return (
      <Page>
        <Switch>
          <Route exact path="/" component={Index} />
          <Route exact path="/users/" component={Users} />
          <Route path="/users/:id" component={User} />
          <Route path="/techgroups/" component={Techgroups} />
          <Route component={NotFound} />
        </Switch>
      </Page>
    )
  }
}

export default App
