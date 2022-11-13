import markerIconPng from "leaflet/dist/images/marker-icon.png"
import {Icon, Marker, Popup} from 'leaflet'

const MapMarker = () => {
  return (
    <Marker icon={new Icon({iconUrl: markerIconPng, iconSize: [25, 41], iconAnchor: [12, 41]})}  position={{lng: -122.673447, lat: 45.522558}}>
        <Popup>
            Some kind of description. <br /> Easily customizable.
        </Popup>
    </Marker>
  )
}

export default MapMarker
