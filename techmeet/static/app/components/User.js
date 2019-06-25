import React, { Component } from "react"
import styled from "styled-components"

import Query from "@/components/Query"

const SINGLE_USER_QUERY = "getUser"

class User extends Component {
  render() {
    return (
      <Query query={SINGLE_USER_QUERY} variables={{ id: this.props.id }}>
        {({ data, error, loading }) => {
          if (loading) return <p>Loading...</p>
          if (error) return <p>Error: {error.message}</p>
          return (
            <div>
              <h2>{data.name}</h2>
              <dl>
                <dt>Email</dt>
                <dd>{data.email}</dd>
                <dt>Date joined</dt>
                <dd>{data.date_joined}</dd>
                <dt>Groups</dt>
                <dd>{data.groups}</dd>
              </dl>
            </div>
          )
        }}
      </Query>
    )
  }
}

export default User
