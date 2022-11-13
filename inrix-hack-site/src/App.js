import './App.css';
import {useState} from 'react'

import IconButton from './components/IconButton'
import { BiSearch, BiFilterAlt } from "react-icons/bi";

function App() {
  const searchBar = () => {}
  const [searchInput, setSearchInput] = useState("")
  const [showFilter, setShowFilter] = useState(false)
  const [queryParams, setQueryParams] = useState({
    distance: 10,
    travelTime: 10,
    noiseLevel: 5,
    busyLevel: 5,
    indoor: true,
    outdoor: true,
  })

  const handleSearchBarChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
  }

  //hardcoded data
  let results = [
    {
      location: 'My house',
      travelTime: 20,
      distance: 0,
      weather: 'rainy',
    },
    {
      location: 'My house',
      travelTime: 20,
      distance: 0,
      weather: 'rainy',
    },
    {
      location: 'My house',
      travelTime: 20,
      distance: 0,
      weather: 'rainy',
    },
    {
      location: 'My house',
      travelTime: 20,
      distance: 0,
      weather: 'rainy',
    },
  ]

  return (
    <>
      {/* sidebar to display results */}
      <div className = 'overflow-auto bg-gray-600 test fixed left-0 top-8 z-30 rounded-3xl p-4 text-white'>
        {results.map((result, index) => (<p key = {index}>{result.location}</p>))}
      </div>

      {/* filter and search bar  */}
      <div>
        <div className = 'flex justify-center items-center'>
          <h1 className ='text-center pt-3'> Hello, Let's Find Someplace Quiet </h1>
        </div>
        
        {/* search bar centered */}
        <div className = 'flex space-x-4 px-6 py-2 bg-gray-600 rounded-full m-3 max-w-xl mx-auto'>
          <input className = 'flex-grow max-w-md focus:outline-0 bg-transparent placeholder-gray-400 text-white m-1'
            type="text"
            placeholder="Your Location"
            onChange={handleSearchBarChange} value={searchInput}
          />

          <IconButton onClick = {() => {console.log('hi')}} icon = {<BiSearch/>}/>
          <IconButton onClick = {() => setShowFilter(!showFilter) } icon = {<BiFilterAlt/>}/>
        </div>

        {/*filtering results*/}
        <div>
          { showFilter && (
            <form className = "bg-gray-600 text-white rounded-3xl p-6 max-w-xl mx-auto" action="">
            <div className = 'form-control-check flex align-center justify-between'>
              <label> Outdoor locations </label>
                <input
                  className = 'accent-transparent'
                  type ='checkbox'
                  checked = {queryParams.outdoor}
                  value = {queryParams.outdoor}
                  onChange = {(e) => setQueryParams({...queryParams, outdoor: e.currentTarget.checked })}
                />       
            </div>

            <div className = 'form-control-check flex align-center justify-between'>
              <label> Indoor locations </label>
                <input
                  className = 'accent-transparent'
                  type ='checkbox'
                  checked = {queryParams.indoor}
                  value = {queryParams.indoor}
                  onChange = {(e) => setQueryParams({...queryParams, indoor: e.currentTarget.checked })}
                />       
            </div>

            <div className = 'form-control-check flex align-center justify-between'>
              <label> Max distance (miles)</label>
              <p className = 'flex-grow'> </p>
              <p className = 'pr-3'>{queryParams.distance}</p>
              <input className = 'accent-white' type="range" value = {queryParams.distance} onChange = {(e) => {setQueryParams({...queryParams, distance: e.target.value})}} />
            </div>

            <div className = 'form-control-check flex align-center justify-between'>
              <label> Max Travel Time(minutes)</label>
              <p className = 'flex-grow'> </p>
              <p className = 'pr-3'>{queryParams.travelTime}</p>
              <input className = 'accent-white' type="range" value = {queryParams.travelTime} onChange = {(e) => {setQueryParams({...queryParams, travelTime: e.target.value})}} />
            </div>

            <div className = 'form-control-check flex align-center'>
              <label> Max Business Levels</label>
              <p className = 'flex-grow'> </p>
              <p className = 'pr-3'>{queryParams.busyLevel}</p>
              <input
                className = 'accent-white'
                max = {10}
                min = {0}
                type="range"
                value = {queryParams.busyLevel}
                onChange = {(e) => {setQueryParams({...queryParams, busyLevel: e.target.value})}} />
            </div>
            </form>
            )
          }
        </div>

      </div>
    </>
  );
}

export default App;
