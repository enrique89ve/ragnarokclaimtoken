$("#send_custom").click(function () {
  console.log("Claim");
  let keychain = window.hive_keychain


  let custom = '{"claim":true}'
  keychain.requestCustomJson(
  null,
  "duat_drop_claim",
  "Posting",
  custom,
  null,
  function (response) {

    console.log("main js response - custom JSON");
    console.log(response);


    if (response.success == true) {

      alert("Successfully!")
    }




    if (response.error == "user_cancel") {

      alert(response.error)
    }



    },
    null





  );
});
