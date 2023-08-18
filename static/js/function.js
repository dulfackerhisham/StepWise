$(document).ready(function(){
    $('.increment-btn').on("click" ,function (e){
        e.preventDefault();
        
        let maxStock = parseInt($(this).closest('.product_data').find('.max-stock').val(), 10);
        let currentQty = parseInt($(this).closest('.product_data').find('.qty').val(), 10);

        if (currentQty < maxStock) {
            currentQty++;
            $(this).closest('.product_data').find('.qty').val(currentQty);
        }
    });
    
    $('.decrement-btn').on("click" ,function (e){
        e.preventDefault();
        console.log("its working")
    
        var dec_value = $(this).closest('.product_data').find('.qty').val();
        var value = parseInt(dec_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1){  // Decrement only if value is greater than 1
            value--;
            $(this).closest('.product_data').find('.qty').val(value);  // Corrected selectors
        }
    });
    
    // Add to cart functionality
    // now we are taking the quantity input field value when we click on 'add to cart' button
    $("#add-to-cart-btn").on("click", function(e){
        e.preventDefault();

        console.log("function is called");
        let quantity = $("#sst").val()
        // let product_title = $(".product-title").val()
        let product_id = $(".product-id").val()
        // let product_price = $(".product-price").text()
        // let this_val = $(this)
        var token = $('input[name=csrfmiddlewaretoken]').val();

        console.log("quantity:", quantity);
        // console.log("product title:", product_title);
        console.log("product id:", product_id);
        // console.log("product price:", product_price);
        // console.log("Current Element:", this_val);

        $.ajax({
            type: "POST",
            url: "/cart/add_to_cart/",
            data: {
                'id': product_id,
                'qty': quantity,
                // 'title': product_title,
                // 'price': product_price,
                csrfmiddlewaretoken: token,
            },
            dataType: "json",
            beforeSend: function() {
                console.log("Adding product to Cart");
            },
            success: function(response){
                console.log(response)
                alertify.success(response.status)
                // window.alert(response.status)
                console.log("Added product to Cart");
            }
        })
})

    $('.changeQuantity').click(function (e){
        e.preventDefault();
        // let product_id = $(".product-id").val()

        var product_id = $(this).closest('.product_data').find('.product-id').val();
        var product_qty = $(this).closest('.product_data').find('.qty').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        console.log("called func");
        console.log(product_id, "product id");
        console.log(product_qty, "quantity");

        $.ajax({
            type: 'POST',
            url : '/cart/update-cart/',
            data: {
                'id': product_id,
                'qty': product_qty,
                csrfmiddlewaretoken: token,
            },
            dataType: 'json',
            success: function (response) {
                console.log("product updated")

                alertify.success(response.status)
            }
        })
    })


    $('.delete-cart').click(function (e){
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.product-id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            url : '/cart/delete-cart/',
            data: {
                'id': product_id,
                csrfmiddlewaretoken: token,
            },
            success: function(response) {
                console.log("product deleted")
                alertify.success(response.status)
            }
        })

    })

    

})