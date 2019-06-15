import React, { Component } from 'react';
import styled from 'styled-components';

import api from '@/api';

class Techgroups extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }

  componentDidMount() {
    api.getTechgroups()
      .then(result => {
        this.setState({
          isLoaded: true,
          items: result.data.results,
        });
      })
      .catch(error => {
        this.setState({
          isLoaded: true,
          error
        });
      })
  }

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <ul>
          {items.map(item => (
            <li key={item.id}>
              {item.name} - {item.description}
            </li>
          ))}
        </ul>
      );
    }
  }
}

export default Techgroups;

