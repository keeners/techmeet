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
    api[this.props.query](this.props.variables)
      .then(response => {
        this.setState({
          loading: false,
          // data will have results prop only when requesting DRF ListViews,
          // otherwise it should just return the detail object
          data: response.data.results ? response.data.results : response.data,
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
