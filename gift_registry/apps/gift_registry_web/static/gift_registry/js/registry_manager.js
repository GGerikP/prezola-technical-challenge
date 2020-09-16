/*
$(document).ready(function() {
    populate_registry()
});
*/

function populate_registry(registry_id, purchase_status, display_type) {

    // TODO: get the registry of the logged in user and use it to query the registry data
    registry_id = (registry_id != undefined ? registry_id : 1);
    purchase_status = (purchase_status != undefined ? purchase_status : "available");
    display_type = (display_type != undefined ? display_type : "purchase");

    console.log("registry_id=" + registry_id + ", purchase_status=" + purchase_status + ", display_type=" + display_type)
    $.ajax({
          url: GIFT_REGISTRY.giftRegistryApiURL + "/registry/" + registry_id + "/?purchase_status=" + purchase_status
    }).done(function(registry) {
        console.log(registry);
        gifts = registry.gifts;
        let gift_container = $(".gift_container." + purchase_status);

        gift_container.empty();

        let row = $("<tr></tr>").attr("class", "gift_header_row");
        row.append($("<td class='gift_field'></td>").text("ID"))
        row.append($("<td class='gift_field'></td>").text("Name"))
        row.append($("<td class='gift_field'></td>").text("Brand"))
        row.append($("<td class='gift_field'></td>").text("Price"))

        if (display_type == "purchase") {
            row.append($("<td class='gift_field'></td>"))
        } else {
            row.append($("<td class='gift_field'></td>").text("In Stock Quantity"))
        }

        gift_container.append(row);

        for (let i = 0; i < gifts.length; i++) {
            let gift = gifts[i];
            let product = gift.product;
            console.log("product[" + i + "] = " + JSON.stringify(product));
            if (product == undefined) {
                continue
            }
            let row = $("<tr></tr>")
            row.append($("<td class='gift_field'></td>").text(product.id))
            row.append($("<td class='gift_field'></td>").text(product.name))
            row.append($("<td class='gift_field'></td>").text(product.brand))
            row.append($("<td class='gift_field'></td>").text(product.price + product.currency))

            if (display_type == "purchase") {
                let purchase_button=$("<button>Purchase</button>").attr("onclick", "purchase_gift(" + registry.id + ", " + gift.id + ")");
                if (product.in_stock_quantity <= 0) {
                    purchase_button.attr("disabled", true);
                    purchase_button.attr("title","Sold out");
                }
                row.append($("<td class='gift_field'></td>").append(purchase_button));
            } else {
                row.append($("<td class='gift_field'></td>").append(product.in_stock_quantity))
            }

            gift_container.append(row);
        }
    });
}

function purchase_gift(registry_id, gift_id) {
    $.ajax({
          url: GIFT_REGISTRY.giftRegistryApiURL + "/registry/" + registry_id
    }).done(function(registry) {
        var gift = undefined;
        for (var i = 0; i < registry.gifts.length; i++) {
            if (registry.gifts[i].id == gift_id) {
                gift = registry.gifts[i];
                registry["purchased_gift"] = registry.gifts[i];
                registry.gifts.splice(i, 1);
            }
        }
        if (gift == undefined || gift.in_stock_quantity <= 0) {
            alert("We're sorry this gift is no longer available.");
            populate_registry(registry.id);
        }
    }).done(function(registry) {
        console.log("Updating the registry with: " + JSON.stringify(registry));
        $.ajax({
              url: GIFT_REGISTRY.giftRegistryApiURL + "/registry/" + registry.id + "/"
            , data: JSON.stringify(registry)
            , dataType: 'json'
            , type: 'PATCH'
            , success: function(registry) {
                populate_registry(registry.id);
            }
            , error: function(resp) {
                console.log(resp);
                alert("There was an error making this purchase");
            }
        })
    })

}

