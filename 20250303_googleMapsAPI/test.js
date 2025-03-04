console.log(google.maps.places);

if("geolocation" in navigator){
    console.log(navigator);
    navigator.geolocation.getCurrentPosition(
        (position) => {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            var accuracy = position.coords.accuracy;
            var altitude = position.coords.altitude;
            var altitudeAccuracy = position.coords.altitudeAccuracy;

            console.log("緯度：" + latitude);
            console.log("経度：" + longitude);
            console.log("位置の精度：" + accuracy);
            console.log("高度：" + altitude);
            console.log("高度の精度：" + altitudeAccuracy);

            initMap(latitude, longitude);
        },
        (error) => {
            console.log(error.message);
        },
        {
            enableHighAccuracy: true,
            timeout: 10000,
            maximumAge: 0
        }
    );
} else {
    console.log("位置情報が取得できません");
};


async function initMap(latitude, longitude) {
    const { Map, InfoWindow } = await google.maps.importLibrary('maps');
    let center = new google.maps.LatLng(latitude, longitude);

    map = new Map(document.createElement('div'), {
        center: center,
        zoom: 15
    });
    nearbySearch(latitude, longitude);
};

async function nearbySearch(latitude, longitude) {
    const { Place, SearchNearbyRankPreference} = await google.maps.importLibrary('places');

    let center = new google.maps.LatLng(latitude, longitude);
    const request = {
        fields: ["displayName", "location", "businessStatus"],
        locationRestriction: {
            radius: 3000,
            center: center
        },
        includedPrimaryTypes: ["train_station"],
    }

    const { places } = await Place.searchNearby(request);

    if(places.length > 0) {
        console.log(places);
    } else {
        console.log("検索結果がありません");
    }
}