$(function () {
    // Submit post on submit
    $('#submit_ack_form').on('submit', function (event) {
        event.preventDefault();
        submit_cancel_form();
    });

    // AJAX for posting
    function submit_cancel_form() {
        console.log("Initiating Ack!"); // sanity check
        let html = document.getElementById('ack').innerText;
        let container_data = html.replace(/\\/g, "");
        $.ajax({
            url: "/post_ack/", // the endpoint
            type: "POST", // http method
            data: {
                acknowledge: container_data
            }, // data sent with the post request
            success: function (response) {
                const editor = ace.edit('ack_response');
                editor.setTheme("ace/theme/dracula");
                editor.session.setMode("ace/mode/javascript");
                editor.getSession().setTabSize(2);
                editor.getSession().setUseWrapMode(true);
                editor.setValue(JSON.stringify(response, null, '\t'));
            },
            error: function (json) {
                alert(json.responseText)
            }
        });
    }
});