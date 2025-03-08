import React, { useState } from 'react'
import './App.css'
import { FormGroup, Button, Form, Input } from 'reactstrap';

function App() {
  const [ rates, setRates ] = useState({});
  const [ selection, setSelection ] = useState(0);
  // useEffect(() => {
  //   const currencyFetch = async () => {
  //     try {
  //       const response = await fetch("http://127.0.0.1:8000/currencyRate/");
  //         const data =  await response.json();
  //         setRates(data);
  //         console.log(data);
  //     } catch (error) {
  //       console.error('Error fetching rates', error);
  //     }
  //   }
  //   currencyFetch
  // }, []);
  // const handleSubmit = async (event) => {
  //   event.preventDefault();
  //   //TODO FILL WITH PAYLOAD OF BACKEND
  // }

  // const handleChange = (event) => {
  //   //TODO FILL WITH ITEMS TO CHANGE AND VALUES CHANGED
  // }

  return (
    <>
    <div className='overlay'>
      <h1>Convert from USD to: </h1>
      <Form>
          <Input 
          type='select'
          >
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
          </Input>
      </Form>
      <Button>Convert</Button>
    </div>
    </>
  )
}

export default App
