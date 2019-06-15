import React, { Component } from 'react';
import { Link } from 'react-router-dom'
import logo from '@/assets/logo.svg';
import HeaderStyle from './styles/HeaderStyle';

class Header extends Component {
  render() {
    return (
      <HeaderStyle>
        <img src={logo} alt="logo" />
        <Link to="/app">Techmeet</Link>

        <ul>
          <li>
            <Link to="/app/users">Users</Link>
          </li>
          <li>
            <Link to="/app/groups">Groups</Link>
          </li>
          <li>
            <Link to="/app/techgroups">Techgroups</Link>
          </li>
        </ul>
      </HeaderStyle>
    )
  }
}
export default Header;
