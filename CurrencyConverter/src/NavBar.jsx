import React, { useState } from 'react'
import {
  Navbar,
  Nav, 
  NavItem,
  NavbarText
} from 'reactstrap'
import './App.css'

function Navigation() {
    return(
        <>
            <Navbar light expand='md' className='fixed-top navBar'>
                <NavbarText>Placeholder # 1</NavbarText>

            </Navbar>
        </>
    );
}

export default Navigation;