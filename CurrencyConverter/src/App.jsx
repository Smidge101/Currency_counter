import React, { useState, useEffect } from 'react'
import './App.css'
import { FormGroup, Button, Form, Input } from 'reactstrap';

function App() {
  const [ rates, setRates ] = useState({});
  const [ selection, setSelection ] = useState('');
  const [ usd, setUSD ] = useState(0.0);
  const [ convertedAmount, setConvertedAmount ] = useState(0.0);
  const [ error, setError ] = useState("");

  useEffect(() => {
    const currencyFetch = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/currency/");
          const data =  await response.json();
          setRates(data);
          console.log(data);
      } catch (error) {
        console.error('Error fetching rates', error);
      }
    }
    currencyFetch()
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if(selection == ''){
      setConvertedAmount(parseFloat(usd).toFixed(2));
      return;
    }
    const data = {
      usd: parseFloat(usd),
      selection: selection
    };
    console.log("SELECTION: ",selection);
    console.log(usd)

    try {
      const response = await fetch('http://127.0.0.1:8000/currency/convert/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      const result = await response.json();
  
      if(response.ok) {
        setConvertedAmount(result.converted_amount.toFixed(2));
        setError('');
      } else {
        setError('Conversion failed');
        setConvertedAmount(null);
      }
    }
    catch (error) {
      setError('An error occured while converting.');
      setConvertedAmount(null);
    }
  };

  return (
    <>
    <div className='overlay'>
      <h1 className='prompt'>Convert from USD</h1>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Input type='number' onChange={(e) => setUSD(e.target.value)}>
          </Input>
        </FormGroup>
        <FormGroup>
            <Input 
            type='select'
            value={selection}
            onChange={(e) => setSelection(e.target.value)}
            >
              {Object.entries(rates).map(([key, value], index) => (
              <option key={index} value={key} required>
                {key}
              </option>))}
            </Input>
          </FormGroup>
      <Button type='submit' color='primary' size='normal' outline>Convert</Button>
      </Form>
      {convertedAmount !== null && (
                <div>
                    <h2>Converted Amount: {convertedAmount}</h2>
                </div>
            )}

            {error && (
              <div style={{ color: 'red' }}>
              <p>{error}</p>
            </div>
            )}
    </div>
    </>
  )
}

export default App;
