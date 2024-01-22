import React, { Component } from 'react';
class Addnumber extends Component {
  constructor(props) {
    super(props);
    this.state = {
      num1: '',
      num2: '',
      result: null,
    };
  }

  handleChange = (event) => {
    const { name, value } = event.target;
    let input=event.target;
    if (!isNaN(value) || value ==='') {
      this.setState({ [name]: value });
    }
  }

  addNumbers = () => {
    const { num1, num2 } = this.state;
    if (num1 !== '' && num2 !== '') {
      const result = parseFloat(num1) + parseFloat(num2);
      this.setState({ result });
    }
  }

  render() {
    const { num1, num2, result } = this.state;
    
    return (
      <div>
        <h3>Add Numbers</h3>
        <div>
          <label>
            Number 1:
            <input type="text" name="num1" value={num1} onChange={this.handleChange} />
          </label>
        </div>
        <div>
          <label>
            Number 2:
            <input type="text" name="num2" value={num2} onChange={this.handleChange} />
          </label>
        </div>
        <div>
          <button type="button" onClick={this.addNumbers}>Add</button>
        </div>
        <div>
        
            <p>Result: {result}</p>
         
        </div>
      </div>
    );
  }
}

export default Addnumber;
