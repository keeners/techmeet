import React, { Component } from "react"
import TechgroupDetails from "@/components/Techgroup"

const Techgroup = props => (
  <div>
    <h1>Techgroup ID: {props.match.params.id}</h1>
    <TechgroupDetails id={props.match.params.id} />
  </div>
)

export default Techgroup
