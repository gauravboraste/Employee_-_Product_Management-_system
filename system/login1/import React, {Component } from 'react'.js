import React, {Component } from 'react'
import axios from 'axios';
import ReactHTMLTableToExcel from 'react-html-table-to-excel';
import './App.css';
export class CascadingDropdown extends Component {
constructor(props) {
super(props)
this.state = {
StateId: '',
CountryId: '',
CountryData: [],
StateData: [],
CityData: []
}
}
componentDidMount() {
axios.get('http://localhost:3000/countries-list').then(response => {
console.log(response.data);
this.setState({
CountryData: response.data
});
});
}
ChangeteState = (e) => {
this.setState({
CountryId: e.target.value
});
axios.get('http://localhost:3000/get-states-by-country?CountryId=' + e.target.value).then(response => {
console.log(response.data);
this.setState({
StateData: response.data,
});
});
}

render() {  
return (  
<div>  
<div class="row" className="hdr">  
<div class="col-sm-12 btn btn-info">  
Cascading Dropdown in ReactJS  
</div>  
</div>  
<div className="form-group dropdn">  
<select className="form-control" name="country" value={this.state.CountryId} onChange={this.ChangeteState}  >  
<option>Select Country</option>  
{this.state.CountryData.map((e, key) => {  
return <option key={key} value={e.CountryId}>{e.CountryName}</option>;  
})}  
</select>  
<select className="form-control slct" name="state" value={this.state.StateId} onChange={this.ChangeCity} >  
<label for="company">State Name</label>    
{this.state.StateData.map((e, key) => {  
return <option key={key} value={e.StateId}>{e.StateName}</option>;  
})}  
</select>  
<select className="form-control slct" name="city" value={this.state.CityData}  >  
{this.state.CityData.map((e, key) => {  
return <option key={key} value={e.CityId}>{e.cityName}</option>;  
})}  
</select>  
</div>  
</div>  
)  
}  
}  
export default CascadingDropdown  



axios.get('/user', {
    params: {
      ID: 12345
    }
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
    // always executed
  });  
