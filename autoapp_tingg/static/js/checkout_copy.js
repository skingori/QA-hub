function GetAccessKey() {
    /* Get the text field */
    const copyText = document.getElementById("access_key");

    /* Select the text field */
    copyText.select();

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    // alert("Copied the text: " + copyText.value);
}


function GetServiceCode() {
    // $(document).ready(function () {
    //     $("#service_code").change(function () {
    //         var str = "";
    //         $("select option:selected").each(function () {
    //             str += $(this).text() + "";
    //             var input = document.createElement('input');
    //             input.setAttribute('value', str);
    //             document.body.appendChild(input);
    //             input.select();
    //             document.execCommand('copy');
    //             document.body.removeChild(input)
    //         });
    //     }).change();
    // });
    //

    /* Get the text field */
    const copyText = document.getElementById("service_code");

    /* Select the text field */
    copyText.select();

    /* Copy the text inside the text field */
    document.execCommand("copy");
    //
    // /* Alert the copied text */
    // /* alert("Copied the text: " + copyText.value); */
}

function GetIvKey() {
    /* Get the text field */
    const copyText = document.getElementById("iv_key");

    /* Select the text field */
    copyText.select();

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    /* alert("Copied the text: " + copyText.value); */
}

function GetSecretKey() {
    /* Get the text field */
    const copyText = document.getElementById("secret_key");

    /* Select the text field */
    copyText.select();

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    /* alert("Copied the text: " + copyText.value); */
}

function ClientId() {
    /* Get the text field */
    const copyText = document.getElementById("client_id");

    /* Select the text field */
    copyText.select();

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    /* alert("Copied the text: " + copyText.value); */
}

function ClientSecret() {
    /* Get the text field */
    const copyText = document.getElementById("client_secret");

    /* Select the text field */
    copyText.select();

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    /* alert("Copied the text: " + copyText.value); */
}

function ClientCode() {
    /* Get the text field */
    const copyText = document.getElementById("client_code");

    /* Select the text field */
    copyText.select();

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    /* alert("Copied the text: " + copyText.value); */
}