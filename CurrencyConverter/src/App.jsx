import React, { useState } from 'react'
import Navigation from './NavBar'
import './App.css'
import { FormGroup } from 'reactstrap';

function App() {

  // const handleSubmit = async (event) => {
  //   event.preventDefault();
  //   //TODO FILL WITH PAYLOAD OF BACKEND
  // }

  // const handleChange = (event) => {
  //   //TODO FILL WITH ITEMS TO CHANGE AND VALUES CHANGED
  // }

  return (
    <>
      <Navigation />
      <h1>Placeholder yall hehe</h1>
      <Form 
      // onSubmit={handleSubmit}
      >
        <FormGroup>
          <Input 
            type='select'
            name='currencytype'
            // onChange={handleChange}
          >
          </Input>
        </FormGroup>

      </Form>




    </>
  )
}

export default App
