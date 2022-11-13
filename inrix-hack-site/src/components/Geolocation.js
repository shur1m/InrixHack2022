import React from "react";
import { useGeolocated } from "react-geolocated";

const Geolocation = () => {
    const { coords, isGeolocationAvailable, isGeolocationEnabled } =
        useGeolocated({
            positionOptions: {
                enableHighAccuracy: false,
            },
            userDecisionTimeout: 5000,
        });

    return coords
};

export default Geolocation;