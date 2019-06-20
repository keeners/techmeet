import React, { Component } from "react"
import styled from "styled-components"

import Query from "@/components/Query"

const ALL_ITEMS_QUERY = "getUsers"

class Users extends Component {
  render() {
    return (
      <Query query={ALL_ITEMS_QUERY}>
        {({ data, error, loading }) => {
          if (loading) return <p>Loading...</p>
          if (error) return <p>Error: {error.message}</p>
          return (
            <ul>
              {data.map(item => (
                <li key={item.email}>
                  {item.name} - {item.email}
                </li>
              ))}
            </ul>
          )
        }}
      </Query>
    )
  }
}

export default Users
