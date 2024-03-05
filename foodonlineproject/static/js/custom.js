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

        //Print the address_components directly;
        //const addressComponents = '<div>';
        //const addressComponents;
        







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

// https://sweetalert2.github.io/#download - I will use this for showing login required

document.addEventListener('DOMContentLoaded', function() {
    function updateCartCounterAndAlert(response, foodId,li_id) {
        console.log(response)

        if (response.chckcart==0){
            document.getElementById("cart_item-"+li_id).remove()

            
            
             

        }




       

      

        if (response.cart_count) {
            document.getElementById('cart_counter').innerHTML = response.cart_count['cart_count'];
            let cart_count=document.getElementById('cart_counter').innerHTML

       
           
            if (cart_count==0){
                     document.getElementById("empty_block").style.display="block";
                     
                            
                    
                     
            }


        }

        if (response && response.chckcart) {
           
            document.querySelector(`#qt-${foodId}`).innerHTML = response.chckcart;

            
           
       
        }



        if (response && response.status === 'login_required') {
             swal({
                title: "Oops!",
                text:response.message,
                type: "error",
                confirmButtonText: "Cool",
                
             
            });




        }
        



    }


    // This is for my cart_deletetion 












    document.querySelectorAll('.cart-decrease-data').forEach(function(element) {
        element.addEventListener('click', function(e) {
            e.preventDefault();
            const foodId = this.getAttribute('id');
            const url = this.getAttribute('data-url');
            const li_id=this.getAttribute('li_id')

            const data = {
                'id': foodId,
                'li_id':li_id
              
            };

            fetch(url + '?' + new URLSearchParams(data), {
                    method: 'GET',
                })
                .then((response) => response.json())
                .then((response) => {
                    updateCartCounterAndAlert(response, foodId,li_id);
                    document.getElementById('subtotal').innerHTML=response.cart_amount['subtotal']
                    document.getElementById('total').innerHTML=response.cart_amount['grandtotal']
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });
















    document.querySelectorAll('.cart-add-data').forEach(function(element) {
        element.addEventListener('click', function(e) {
            e.preventDefault();
            const foodId = this.getAttribute('id');
            const url = this.getAttribute('data-url');
            // const qt=this.getAttribute('data')

            const data = {
                'food': foodId,
                // 'quantity': qt
            };

            fetch(url + '?' + new URLSearchParams(data), {
                    method: 'GET',
                })
                .then(response => response.json())
                .then(response => {
                    console.log(response)

                    updateCartCounterAndAlert(response, foodId);
                    document.getElementById('subtotal').innerHTML=response.cart_amount['subtotal']
                    document.getElementById('total').innerHTML=response.cart_amount['grandtotal']
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });






function remove_cart(response,id){


    if (response.status == 'success') {

        swal({
            title: "Success!",
            text: "Your item has been removed from the cart.",
            icon: "success"
        });

        document.getElementById('subtotal').innerHTML=response.cart_amount['subtotal']
            
        document.getElementById('total').innerHTML=response.cart_amount['grandtotal']


        remove_cart_list(0,id,response)
        iscart_empty()
        
      }







    else{
        swal({
            title: "error!",
            text: "There is no item in your acc.",
            icon: "Error",
            button: "Continue Shopping"

          })


    }



}



function remove_cart_list(cart_item_qty,id,response){

    if (cart_item_qty<=0){
        document.getElementById("cart_item-"+id).remove()
        document.getElementById("cart_counter").innerHTML=response.cart_counter["cart_count"]
        





             
             
           
               


    }


      



    
}




function iscart_empty(){
    let cart_count=document.getElementById('cart_counter').innerHTML
    console.log(cart_count)
    if (cart_count==0){
             document.getElementById("empty_block").style.display="block";
             
                    
            
             
    }

        

}








// here i will add the functionatlity for decrease cart 
        document.querySelectorAll('.delete-item').forEach(function(element){
            

            element.addEventListener('click',function(e){

                e.preventDefault()

                const id=this.getAttribute('id')
                const url=this.getAttribute('data-url')





                const data={
                    'cart_id':id
                }


                fetch(url + '?' + new URLSearchParams(data),{
                    method:'GET'
                })

                .then((response)=>response.json())
                .then((response)=>{  

                   
                    
                    remove_cart(response,id)
                      
                         

                           
                       
                })
                 










            })




        })













// here i will add the functionality of  openinfg and closing hours 
document.querySelectorAll('.add_hour').forEach(function(element) {
    element.addEventListener('click', function(e) {
        e.preventDefault();

        let day = document.getElementById('id_day').value;
        let from_hour = document.getElementById('id_from_hour').value;
        let to_hour = document.getElementById('id_to_hour').value;
        let is_closed = document.getElementById('id_is_closed').checked;
        let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        let url = document.getElementById('add_hour_url').value;
    
        
        if(is_closed){
            is_closed='True';
            condition="day !=''";
        } else {
            is_closed='False';
            condition="day !='' && from_hour !='' && to_hour !=''";
        }

        let data={
            'day': day,
            'from_hour': from_hour,
            'to_hour': to_hour,
            'is_closed': is_closed,
            'csrf': csrf
        }


        if (eval(condition)){
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                //   console.log(data)
                
                  if(data.status=="success"){
                      console.log(data)
                       if(data.is_closed){
                        //    console.log('i am got executyed')
                    
                           var html = "<tr><td><b>" + data.day + "</b></td><td><b>Closed</b></td><td><a href=''>Remove</a></td></tr>";
                           document.getElementById("opening_hours").insertAdjacentHTML('beforeend', html);
                              
                           
                       }
                       else{
                        var html = "<tr><td><b>" + data.day + "</b></td><td><b>" + data.from_hour + " - " + data.to_hour + "</b></td><td><a href=''>Remove</a></td></tr>";
                        document.getElementById("opening_hours").insertAdjacentHTML('beforeend', html);
                       
                       


                       }
                        


                       
                  }
                  else{
                     
                        swal({
                            title: "Oops!",
                            text:'The day is already exit',
                            type: "error",
                            confirmButtonText: "Cool",
                            
                        })
                  }
              

                
            })
            .catch(error => console.error('Error:', error));
        }
    });
});
document.querySelectorAll('.remove-hour').forEach(function(element) {
    element.addEventListener('click', function(e) {
        e.preventDefault();

        // Extract the PK from the URL more reliably
        const urlParts = this.getAttribute('href').split('/');
        const pk = urlParts[urlParts.length - 2];  // Access the second-to-last part of the URL

        // Remove the <tr> element associated with the clicked link
        const trId = 'tableid-' + pk;
        const trElement = document.getElementById(trId);
        let csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        if (trElement) {
            // Make AJAX request to delete data on the backend

            fetch(`/vendor/openinghour_delete/${pk}/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf
                },
            })
            .then(response => {
                 return response
               
            })
            .then(data => {
                const trElement = document.getElementById(trId).remove();

                      
            })
            .catch(error => console.error('Error:', error));
        }
    });
});









    // Place the cart item quantity on load
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



















    








// we will check a another condition wen i will reach to the counter itm to 0
// my cart shoud be deleted


