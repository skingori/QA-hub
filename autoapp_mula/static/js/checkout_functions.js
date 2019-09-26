$("#proBanner").fadeTo(10000, 500).slideUp(500, function () {
    $("#proBanner").slideUp(500);
});

$(document).ready(function () {
    $('body').on('click', '#simulate_pay', function () {
        document.getElementById("account_number").value = $(this).attr('data-id');
    });
});

$(function () {
    // Submit post on submit
    $('#simulate_pay_form').on('submit', function (event) {
        event.preventDefault();
        create_pay();
    });

    // AJAX for posting
    function create_pay() {
        console.log("Making payment!"); // sanity check
        $.ajax({
            url: "/simulatePay/", // the endpoint
            type: "POST", // http method
            data: {
                amount: $('#amount').val(),
                account_number: $('#account_number').val(),
                msisdn: $('#msisdn').val(),
                payerClient: $('#payerClient').val(),
                currency: $('#currency').val()
            }, // data sent with the post request
            // handle a successful response
            success: function (json) {
                let data = JSON.stringify(json);
                $(document).ready(function () {
                    alert(json["REASON"]);
                    // $('.toast').toast('show');
                    // $('.toast-body').html(data);
                });
            },
            // handle a non-successful response
            error: function (json) {
                let data = JSON.stringify(json);
                alert(json["REASON"]);
                // $('#pay_message_modal').modal({show:true});
                //  $('#pay_modal_content').html(data, "Error making payment!!!");
                // $('#pay_modal_content').html("<div class='alert-box alert radius' data-alert>" + errmsg +
                //     "</div>"); // add the error to the dom
                console.log(json.status + ": " + json.statusText); // provide a bit more info about the error to the console
            }
        });
        $('#payment').modal('hide')
    }

    // This function gets cookie with a given name
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    let csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        let host = document.location.host; // host + port
        let protocol = document.location.protocol;
        let sr_origin = '//' + host;
        let origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url === origin || url.slice(0, origin.length + 1) === origin + '/') ||
            (url === sr_origin || url.slice(0, sr_origin.length + 1) === sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});