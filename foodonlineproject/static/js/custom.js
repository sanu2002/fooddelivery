let autocomplete;

function initAutoComplete() {
    const input = document.getElementById('id_addressline_1');
    autocomplete = new google.maps.places.Autocomplete(input, {
        types: ['geocode'],
        componentRestrictions: { country: ['in'] },
    });

    autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged() {
    const place = autocomplete.getPlace();

    if (place.geometry) {
        // Print the address_components directly

        let geocoder = new google.maps.Geocoder();
        geocoder.geocode({ 'address': place.formatted_address }, function (results, status) {
            if (status === 'OK') {
                const location = results[0].geometry.location;
                const latitude = location.lat();
                const longitude = location.lng();

                const latitudeInput = document.getElementById('id_latitude');
                const longitudeInput = document.getElementById('id_longtitude');

                if (latitudeInput && longitudeInput) {
                    latitudeInput.value = latitude  | "";
                    longitudeInput.value = longitude | "";
                } else {
                    console.error('Latitude or longitude input not found.');
                }

                document.getElementById('id_addressline_1').placeholder = 'Start typing...';
            } else {
                console.error('Geocoding failed. Status:', status);
            }

            let data = place.address_components;

            let city, state;

            for (let index = 0; index < data.length; index++) {
                const element = data[index];
                const types = element.types;

                if (types.includes('locality')) {
                    city = element.long_name;
                } else if (types.includes('administrative_area_level_1')) {
                    state = element.long_name;
                }
            }

            const cityInput = document.getElementById('id_city');
            const stateInput = document.getElementById('id_state');

            if (cityInput && stateInput) {
                cityInput.value = city || '';
                stateInput.value = state || '';
            } else {
                console.error('City or state input not found.');
            }
        });
    }
}

// Initialize the autocomplete when the Google Maps API is loaded
window.onload = initAutoComplete;
