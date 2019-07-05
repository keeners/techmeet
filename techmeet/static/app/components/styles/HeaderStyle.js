import styled from "styled-components"

const Header = styled.header`
  background-color: #282c34;
  min-height: 100px;
  display: flex;
  align-items: center;
  font-size: 20px;
  color: white;
  padding: 0 20px;

  img {
    height: 50px;
  }

  a {
    color: white;
  }

  ul {
    list-style: none;
    display: flex;
    justify-content: flex-end;
    flex: 1 1 auto;

    li {
      margin-left: 20px;
    }
  }
`

export default Header
