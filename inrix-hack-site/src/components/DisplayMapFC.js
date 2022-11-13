// src/DisplayMapFC.js

import {useLayoutEffect, useRef} from 'react';

export const DisplayMapFC = () => {
  // Create a reference to the HTML element we want to put the map on
  const mapRef = useRef(null);

  /**
   * Create the map instance
   * While `useEffect` could also be used here, `useLayoutEffect` will render
   * the map sooner
   */
  useLayoutEffect(() => {
    // `mapRef.current` will be `undefined` when this hook first runs; edge case that
    if (!mapRef.current) return;
    const H = window.H;
    console.log(process.env.REACT_APP_HERE_KEY)

    const platform = new H.service.Platform({
        apikey: process.env.REACT_APP_HERE_KEY
    });
    const defaultLayers = platform.createDefaultLayers();
    const hMap = new H.Map(mapRef.current, defaultLayers.vector.normal.map, {
      center: { lat: 37.7749, lng: -122.4194 },
      zoom: 12,
      pixelRatio: window.devicePixelRatio || 1
    });

    var svgMarkup = '<svg width="24" height="24" ' +
    'xmlns="http://www.w3.org/2000/svg">' +
    '<rect stroke="white" fill="#1b468d" x="1" y="1" width="22" ' +
    'height="22" /><text x="12" y="18" font-size="12pt" ' +
    'font-family="Arial" font-weight="bold" text-anchor="middle" ' +
    'fill="white">H</text></svg>';

    var icon = new H.map.Icon(svgMarkup),
    coords = {lat: 37.7749, lng: -122.4194},
    marker = new H.map.Marker(coords, {icon: icon});

    hMap.addObject(marker);
    hMap.setCenter(coords);

    const behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(hMap));

    const ui = H.ui.UI.createDefault(hMap, defaultLayers);

    // This will act as a cleanup to run once this hook runs again.
    // This includes when the component un-mounts
    return () => {
      hMap.dispose();
    };
  }, [mapRef]); // This will run this hook every time this ref is updated

  return <div className="map" ref={mapRef} style={{ height: "100vh" }} />;
};