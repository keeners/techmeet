import React, { Component } from "react"
import styled from "styled-components"

import Query from "@/components/Query"

const ALL_ITEMS_QUERY = "getTechgroups"

class Techgroups extends Component {
  render() {
    return (
      <Query query={ALL_ITEMS_QUERY}>
        {({ data, error, loading }) => {
          if (loading) return <p>Loading...</p>
          if (error) return <p>Error: {error.message}</p>
          return (
            <ul>
              {data.map(item => (
                <li key={item.id}>
                  <a href={`/techgroups/${item.id}/`}>
                    <img src={item.logo} alt="" />
                    {item.name} - {item.description}
                  </a>
                </li>
              ))}
            </ul>
          )
        }}
      </Query>
    )
  }
}

export default Techgroups
