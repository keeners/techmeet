import React, { Component } from 'react';
import { Link } from 'react-router-dom'
import logo from '@/assets/logo.svg';
import HeaderStyle from './styles/HeaderStyle';

class Header extends Component {
  render() {
    return (
      <HeaderStyle>
        <img src={logo} alt="logo" />
        <Link to="/">Techmeet</Link>

        <ul>
          <li>
            <Link to="/users">Users</Link>
          </li>
          <li>
            <Link to="/techgroups">Techgroups</Link>
          </li>
        </ul>
      </HeaderStyle>
    )
  }
}
export default Header;
