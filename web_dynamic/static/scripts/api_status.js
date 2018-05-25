// Toggles the API status circle in upper-right hand part of webpage
// Red is API status is OK, grey if not.
$(document).ready(function () {
  let url = 'http://0.0.0.0:5001/api/v1/status/';
  $.ajax({
    url: url,
    type: 'GET',
    success: function (data) {
      if (data.status === 'OK') { $('div#api_status').css('background', '#FF545F'); }
    }
  });
});

