$(function () {
    // Submit post on submit
    $('#submit_refunds_form').on('submit', function (event) {
        event.preventDefault();
        submit_refunds_form();
    });

    // AJAX for posting
    function submit_refunds_form() {
        console.log("Submitting Refunds!"); // sanity check
        let html = document.getElementById('refund').innerText;
        let container_data = html.replace(/\\/g, "");
        $.ajax({
            url: "/post_refunds/", // the endpoint
            type: "POST", // http method
            data: {
                refund: container_data
            }, // data sent with the post request
            success: function (response) {
                const editor = ace.edit('refund_response');
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