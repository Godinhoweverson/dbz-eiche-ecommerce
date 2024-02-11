
//  Cart 

function updateCart(productId, action) {
   console.log(productId, action)
   fetch(`update_cart/${productId}/${action}/`, {
       method: 'GET',
       headers: {
           'X-Requested-With': 'XMLHttpRequest',
       },
   })
   .then(response => response.text())
   .then(data => {
       const cartItem = document.getElementById(`cart-item-${productId}`);
       cartItem.innerHTML = data;
       const event = new Event('hx-trigger');
       document.body.dispatchEvent(event);
       location.reload();
   })
   .catch(error => console.error('Error updating cart:', error));
}


function removeFromCart(productId) {
fetch(`remove_from_cart/${productId}/`, {
   method: 'GET',
   headers: {
       'X-Requested-With': 'XMLHttpRequest',
   },
})
.then(response => response.json())
.then(data => {
   console.log(data.message);
   location.reload();
})
.catch(error => console.error('Error removing item from cart:', error));
}


