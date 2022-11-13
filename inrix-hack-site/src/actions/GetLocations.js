
//get weather for api
const getLocations = async (props) => {


    return await fetch('https://inrix-hack-api.herokuapp.com/places?' + new URLSearchParams({
        lat: props.lat,
        long: props.long,
        noise:props.noise,
        distance:props.distance,
        indoor:props.indoor,
        time:props.time,
    }));


}

export default getLocations