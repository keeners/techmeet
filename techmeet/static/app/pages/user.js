import React, { Component } from "react"
import UserDetails from "@/components/User"

const User = props => (
  <div>
    <h1>User ID: {props.match.params.id}</h1>
    <UserDetails id={props.match.params.id} />
  </div>
)

export default User
