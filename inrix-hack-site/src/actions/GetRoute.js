//get weather for api
const getRoute = async (props) => {
    console.log(props)

    return await fetch('https://inrix-hack-api.herokuapp.com/route/route?' + new URLSearchParams({
        wp_1lat: props.w1lat,
        wp_2lat: props.w2lat,
        wp_1long: props.w1long,
        wp_2long: props.w2long,
    }));


}

export default getRoute