$(document).ready(function(){
    // Add to cart functionality
    // now we are taking the quantity input field value when we click on 'add to cart' button
    $("#add-to-cart-btn").on("click", function(){
        console.log("function is called");
        let quantity = $("#sst").val()
        let product_title = $(".product-title").val()
        let product_id = $(".product-id").val()
        let product_price = $(".product-price").text()
        let this_val = $(this)

        console.log("quantity:", quantity);
        console.log("product title:", product_title);
        console.log("product id:", product_id);
        console.log("product price:", product_price);
        console.log("Current Element:", this_val);

        $.ajax({
            url: '/add-to-cart',
            data: {
                'id': product_id,
                'qty': quantity,
                'title': product_title,
                'price': product_price,
            },
            dataType: 'json',
            beforeSend: function() {
                console.log("Adding product to Cart");
            },
            success: function(reponse){
                this_val.html("Item Added to Cart");
                console.log("Added product to Cart");
            }
        })
})
})