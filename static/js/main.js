
// Send Handshake event
$("#sw-handshake").click(function () {
  hive_keychain.requestHandshake(function () {
    console.log("Handshake received!");
  });
});
  

  $("#send_custom").click(function () {
    console.log("Claim");
    hive_keychain.requestCustomJson(
      $("#custom_username").val(),
      $("#custom_id").val(),
      $("#custom_method").val(),
      $("#custom_json").val(),
      $("#custom_message").val(),
      function (response) {
        console.log("main js response - custom JSON");
        alert(response['message']);
        console.log(response['message']);
        
      },
      $("#custom_rpc").val()

      




      
    );
  });


