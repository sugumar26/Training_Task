import React, { Component } from 'react';

class Tableform extends Component {
  render() {
    return (
      <div>
        <div className="table-container">
          <h3>Table</h3>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Age</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>sugu</td>
                <td>22</td>
              </tr>
              <tr>
                <td>2</td>
                <td>vijay</td>
                <td>66</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="form-container">
          <h3>Form</h3>
          <form>
            <div className="form-element">
              <label>
                Name:
                <input type="text" name="name" />
              </label>
            </div>
            <br />
            <div className="form-element">
              <label>
                Email:
                <input type="email" name="email" />
              </label>
            </div>
            <div className="form-element">
              <label>
                Completed Task:
              </label>
              <label>
                <input type="checkbox" name="Task32" />
                Task32
              </label>
              <label>
                <input type="checkbox" name="Task12" />
                Task12
              </label>
              <label>
                <input type="checkbox" name="Task87" />
                Task87
              </label>
            </div>
            <div className="form-element">
              <label>
                Team:
              </label>
              <label>
                <input type="radio" name="radioGroup" value="product" />
                Product
              </label>
              <label>
                <input type="radio" name="radioGroup" value="delivery" />
                Delivery
              </label>
            </div>
            <div className="form-element">
              <label>
                Leave Type:
                <select name="leaveType">
                  <option value="sick">Sick Leave</option>
                  <option value="casual">Casual Leave</option>
                  <option value="wfh">Work from home</option>
                </select>
              </label>
            </div>
            <button type="submit">Submit</button>
          </form>
        </div>
      </div>
    );
  }
}

export default Tableform;
