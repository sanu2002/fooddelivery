let autocomplete;

function initAutoComplete(params) {
    const input = document.getElementById('autocomplete');

    autocomplete = new google.maps.places.Autocomplete(input, {
        types: ['geocode', 'establishment'],
        componentRestrictions: {
            country: ['in']
        }
    });

    autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged() {
    const place = autocomplete.getPlace();

    if (place.geometry) {
        document.getElementById('autocomplete').placeholder = 'Start typing...';
    } else {
        console.log('Place name: ', place.name);
    }
}


