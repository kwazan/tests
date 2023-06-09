$(document).ready(function() {
    $("#otp-form").submit(function(event) {
      event.preventDefault();
      var formData = $(this).serialize();
      $.ajax({
        type: "POST",
        url: "hello/hello3",  
        data: formData,
        beforeSend: function() {
          //  loading overlay 
        },
        success: function(data) {
          // Handle the response from the server, for example:
          
        },
        error: function(error) {
          
          // Show error message to the user
        }
      });
    });
  });
  