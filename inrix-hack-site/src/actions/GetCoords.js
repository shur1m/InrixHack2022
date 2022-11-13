//get weather for api
const getCoords = async ({text}) => {
    console.log(text)

    return await fetch('https://inrix-hack-api.herokuapp.com/geocode/txtToPoint?' + new URLSearchParams({
        searchText: text
    }));


}

export default getCoords