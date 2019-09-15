$(function () {
    // Submit post on submit
    $('#simulate_json_form').on('submit', function (event) {
        event.preventDefault();
        simulate_json();
    });

    // AJAX for posting
    function simulate_json() {
        console.log("Making payment!"); // sanity check
        let container = document.getElementById('json_data').innerText;
        let container_data = container.replace(/\\/g, '');
        $.ajax({
            url: "/simulate_json/", // the endpoint
            type: "POST", // http method
            data: {
                json_data: JSON.parse(container_data)
            }, // data sent with the post request
            success: function (response) {
                window.location.href = response["redirect_url"];
            },
            error: function (json) {
                alert(json.responseText)
            }
        });
        $('#json_modal').modal('hide')
    }
});