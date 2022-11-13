import L from "leaflet";
import { createControlComponent } from "@react-leaflet/core";
import "leaflet-routing-machine";

const createRoutineMachineLayer = ({ routes }) => {
  let waypoints = []
  for (let route of routes){
    waypoints.push(L.latLng(route[0], route[1]))
  }

  console.log(waypoints)

  const instance = L.Routing.control({
    waypoints: waypoints,
  });

  return instance;
};

const RoutingMachine = createControlComponent(createRoutineMachineLayer);

export default RoutingMachine;