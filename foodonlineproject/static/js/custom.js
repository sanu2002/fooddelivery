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


// $(document).ready(function(e){
    
//     $('.cart-add-data').on('click', function(e) {
//         e.preventDefault();
        
//         const foodId = $(this).attr('id');
//         const url = $(this).attr('data-url');
//         const csrfToken = $('input[name=csrfmiddlewaretoken]').val();  // Get CSRF token from the page

//         const data = {
//             'food': foodId,
//         };

//         $.ajax({
//             type: 'GET',
//             url: url,
//             data: data,
//             success: function(response) {
//                 $('#cart_counter').html(response.cart_count['cart_count']) 

//             },
//             error: function(error) {
//                 console.error('Error:', error);
//             }
//         });
//     });
// });


// here i will use the fetch or ajax request for making the cart functionality working 




// https://sweetalert2.github.io/#download - i will uses this for shwoing login required

document.addEventListener('DOMContentLoaded', function() {





    document.querySelectorAll('.cart-decrease-data').forEach(function(element){

          element.addEventListener('click',function(e){
            e.preventDefault()
            const foodId = this.getAttribute('id');
            const url = this.getAttribute('data-url');

            const data={
                'id':foodId
            }

            fetch(url + '?' + new URLSearchParams(data), {
                method: 'GET',
            })
            .then((response)=>response.json())
            .then((response)=>{

                document.getElementById('cart_counter').innerHTML=response.cart_count['cart_count']
                document.querySelector(`#qt-${foodId}`).innerHTML = response.chckcart;


                   
                     
                 
                

            })

            .catch(error => {
                console.error('Error:', error);
            });








                

          })





    })
    














    document.querySelectorAll('.cart-add-data').forEach(function(element) {
        element.addEventListener('click', function(e) {
            e.preventDefault();
            const foodId = this.getAttribute('id');

            const url = this.getAttribute('data-url');


            const data = {
                'food': foodId,
            };
            

            fetch(url + '?' + new URLSearchParams(data), {
                method: 'GET',
            })
            .then(response => response.json())
            .then(response => {

                    console.log(response.cart_count['cart_count'])
                    document.getElementById('cart_counter').innerHTML=response.cart_count['cart_count']
                    document.querySelector(`#qt-${foodId}`).innerHTML = response.chckcart;

                    // $('#qt-'+foodId).html(response.chckcart) js-query
                   


             
                     
                   
                    
                     

                
            })
            .catch(error => {
                    console.error('Error:', error);
            });





        });
    });



    // place the cart item quantity on load

    let item_qt = document.getElementsByClassName('item_qt');
    let itemArray = Array.from(item_qt);

    itemArray.forEach(element => {
        let the_id = element.getAttribute('id');
        let qty = element.getAttribute('data_qt');

        // Assuming you want to set the HTML content of an element with ID 'the_id'
        let targetElement = document.getElementById(the_id);

        if (targetElement) {
            // Set the HTML content using .innerHTML
            targetElement.innerHTML = qty;
        }
    });







    




});
