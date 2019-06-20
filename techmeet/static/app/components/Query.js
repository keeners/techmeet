import React, { Component } from "react"

import api from "@/api"

class Query extends Component {
  constructor(props) {
    super(props)
    this.state = {
      error: null,
      loading: true,
      data: [],
    }
  }

  componentDidMount() {
    api[this.props.query]()
      .then(response => {
        this.setState({
          loading: false,
          data: response.data.results,
        })
      })
      .catch(error => {
        this.setState({
          loading: false,
          error,
        })
      })
  }

  render() {
    return this.props.children(this.state)
  }
}

export default Query
