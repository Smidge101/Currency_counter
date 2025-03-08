import React, { useState } from 'react'
import Navigation from './NavBar'
import './App.css'
import { FormGroup } from 'reactstrap';

function App() {
  const [ rates, setRates ] = useState({});
  useEffect(() => {
    const currencyFetch = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/currencyRate/");
          const data =  await response.json();
          setRates(data);
          console.log(data);
      } catch (error) {
        console.error('Error fetching rates', error);
      }
    }
    currencyFetch
  }, []);
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
      {console.log(rates)}
      <Button onClick={currencyFetch}></Button>
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
