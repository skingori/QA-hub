$(function () {
    // Submit post on submit
    $('#submit_cancel_form').on('submit', function (event) {
        event.preventDefault();
        submit_cancel_form();
    });

    // AJAX for posting
    function submit_cancel_form() {
        console.log("Initiating Cancel!"); // sanity check
        let html = document.getElementById('cancel').innerText;
        let container_data = html.replace(/\\/g, "");
        $.ajax({
            url: "/initiate_cancel/", // the endpoint
            type: "POST", // http method
            data: {
                cancel: container_data
            }, // data sent with the post request
            success: function (response) {
                document.getElementById('cancel_response').innerHTML = PR.prettyPrintOne(JSON.stringify(response));
            },
            error: function (json) {
                alert(json.responseText)
            }
        });
    }
});