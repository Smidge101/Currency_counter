import React, { useState, useEffect } from 'react'
import './App.css'
import { FormGroup, Button, Form, Input } from 'reactstrap';

function App() {
  const [ rates, setRates ] = useState({});
  const [ selection, setSelection ] = useState(0);
  const [ usd, setUSD ] = useState(0);
  useEffect(() => {
    const currencyFetch = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/currency/currencyRate");
          const data =  await response.json();
          setRates(data);
          console.log(data);
      } catch (error) {
        console.error('Error fetching rates', error);
      }
    }
    currencyFetch()
  }, []);
  // const handleChange = (event) => {
  //   //TODO FILL WITH ITEMS TO CHANGE AND VALUES CHANGED
  // }

  // const handleSubmit = async (event) => {
  //   event.preventDefault();
  //   //TODO FILL WITH PAYLOAD OF BACKEND
  // }

  return (
    <>
    {console.log(JSON.stringify(rates, null, 2))}
    <div className='overlay'>
      <h1 className='prompt'>Convert </h1>
      <Form>
        <Input>
        </Input>
          <Input 
          type='select'
          >
            {Object.entries(rates).map(([key,value], index) => (
             <option key={index} value={key}>
              {key}
            </option>))}
          </Input>
      </Form>
      <Button color='primary' size='normal' outline>Convert</Button>
    </div>
    </>
  )
}

export default App;
