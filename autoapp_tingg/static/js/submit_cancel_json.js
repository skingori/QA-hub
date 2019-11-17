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
                const editor = ace.edit('cancel_response');
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