/**
 * Created by akash on 3/30/2015.
 */

$(document).ready(function() {
    $('#gang').tooltip({
        title: "Awesome titleeeee!"
    });
    $("#field1").tooltip({
        position: {my: "left+45 center", at: "right"}
    });
    $("#field2").tooltip({
        content: function () {
            return this.getAttribute("title");
        },
        animation: 'fade',

    });

    $("#field3").tooltip({
        content: function () {
            return this.getAttribute("title");
        },
        animation: 'fade',

    });
});

   });