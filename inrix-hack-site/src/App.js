import './App.css';
import {useState} from 'react'

import IconButton from './components/IconButton'
import { BiSearch, BiFilterAlt } from "react-icons/bi"
import {DisplayMapFC} from "./components/DisplayMapFC"
import Geolocation from "./components/Geolocation"
import getLocations from './actions/GetLocations';
import getRoute from './actions/GetRoute';
import getCoords from './actions/GetCoords';
import myData from './data.json'

import markerIconPng from "leaflet/dist/images/marker-icon.png"
import greenLeaf from "./redPin.png"
import { Icon } from 'leaflet';
import { MapContainer, TileLayer, useMap, Marker, Popup, Polyline } from 'react-leaflet'

function App() {

  const searchBar = () => {}
  const [searchInput, setSearchInput] = useState("")
  const [showFilter, setShowFilter] = useState(false)
  const [queryParams, setQueryParams] = useState({
    lat: 37.742120,
    long: -122.480110,
    distance: 20,
    travelTime: 10,
    noiseLevel: 70,
    busyLevel: 5,
    indoor: false,
    outdoor: true,
  })

  const [responses, setResponses] = useState([])
  const [selected, setSelected] = useState(-1)
  const [route, setRoute] = useState([])

  const handleSearchBarChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
  }

  //hardcoded data
  let results = myData

  //query the api and place everything in sidebar and map
  const onSearch = () => {
    if (searchInput){
      //call api and set the queryparams
      getCoords({text: searchInput})
        .then((result) => result.json())
        .then(result => setQueryParams({
          ...queryParams, 
          lat: result[0].referencePosition.latitude,
          long: result[0].referencePosition.longitude}))
        .then(() => finalizeSearch())
      return
    }

    finalizeSearch()    
  }

  const finalizeSearch = () => {
    getLocations(queryParams)
    .then((result) => result.json())
    .then((result) => {
      setResponses(result)
    })
  }

  const onSelection = (index) => {
    console.log(index)

    //set selected for ui
    setSelected(index)

    //request api route
    getRoute({
      w1lat: queryParams.lat, 
      w1long: queryParams.long, 
      w2lat: responses[index].Latitude, 
      w2long: responses[index].Longitude})
      .then((res) => res.json())
      .then((res) => setRoute(res))
  }

  let coords = Geolocation()


  return (
    <>
      {/* sidebar to display results */}
      <div className = 'overflow-auto bg-gray-600 sidebar fixed left-8 top-8 z-30 rounded-3xl  text-white'>
        {responses.map((response, index) => (
          <div key = {index} className = {`location ${index == selected ? 'bg-blue-800' : 'bg-gray-500'} my-2 p-2 rounded-lg`} onClick = {() => {onSelection(index)}}>
            <h3>{response.Name}</h3>
            <p className = 'text-sm'>{response.Address}</p>
            
          </div>
        ))}
      </div>
      
      {/* display map */}
      <MapContainer className = 'h-screen z-0' center={{lng: queryParams.long, lat: queryParams.lat}} zoom={12} scrollWheelZoom={false} >
         <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>
        
        <Marker icon={new Icon({iconUrl: greenLeaf, iconSize: [25, 41], iconAnchor: [12, 41]})}  position={{lng: queryParams.long, lat: queryParams.lat}}>
          <Popup>
            You're here!
          </Popup>
        </Marker>

        {responses.map((response, index) => (
          <Marker key = {index} icon={new Icon({iconUrl: markerIconPng, iconSize: (index !== selected ? [25, 41] : [37.5, 61.5]), iconAnchor: [12, 41]})}  position={{lng: response.Longitude, lat: response.Latitude}}>
            <Popup>
                {response.Address}
            </Popup>
          </Marker>
        ))}
  
        <Polyline pathOptions = {{color: 'lime'}} positions = {route}/>
      </MapContainer>

      {/* filter and search bar  */}
      <div className = 'fixed left-0 top-0 z-10 w-screen'>
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

          <IconButton onClick = {() => {onSearch()}} icon = {<BiSearch/>}/>
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
