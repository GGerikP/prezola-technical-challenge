
$(document).ready(function() {
    $.ajax({
          url: GIFT_REGISTRY.giftRegistryApiURL + "/registry/1"
        , context: document.body
    }).done(function(registry) {
        populate_registry(registry);
    });
});


function populate_registry(registry) {
    console.log(registry);
    products = registry.products;
    $(".product_container").empty();
    for (let i = 0; i < products.length; i++) {
        console.log("products[" + i + "] = " + JSON.stringify(products[i]));
        if (products[i] == undefined || products[i].in_stock_quantity <= 0) {
            continue
        }
        row = $("<tr></tr>")
        row.append($("<td class='product_field'></td>").text(products[i].id))
        row.append($("<td class='product_field'></td>").text(products[i].name))
        row.append($("<td class='product_field'></td>").text(products[i].brand))
        row.append($("<td class='product_field'></td>").text(products[i].price + products[i].currency))

        purchase_button=$("<button>Purchase</button>").attr("onclick", "purchase_product(" + registry.id + ", " + products[i].id + ")");
        row.append($("<td class='product_field'></td>").append(purchase_button));
        $(".product_container").append(row);
    }
}

function purchase_product(registry_id, product_id) {
    $.ajax({
          url: GIFT_REGISTRY.giftRegistryApiURL + "/registry/" + registry_id
    }).done(function(registry) {
        product = undefined;
        for (var i = 0; i < registry.products.length; i++) {
            if (registry.products[i].id == product_id) {
                product = registry.products[i];
                registry["purchased_product"] = registry.products[i];
                registry.products.splice(i, 1);
            }
        }
        if (product == undefined || product.in_stock_quantity <= 0) {
            alert("We're sorry this product is no longer available.");
            populate_registry(registry);
        }
    }).done(function(registry) {
        console.log("Updating the registry with: " + JSON.stringify(registry));
        $.ajax({
              url: GIFT_REGISTRY.giftRegistryApiURL + "/registry/" + registry.id + "/"
            , data: JSON.stringify(registry)
            , dataType: 'json'
            , type: 'PATCH'
            , success: function(resp) {
                populate_registry(registry);
            }
            , error: function(resp) {
                console.log(resp);
                alert("There was an error making this purchase");
            }
        })
    })

}

