// Loops through all Places and displays them on web page
$(document).ready(function () {
  // Gets all users
  let url = 'http://0.0.0.0:5001/api/v1/bikes_search/';
  let users = {};
  $.ajax({
    url: 'http://0.0.0.0:5001/api/v1/users/',
    type: 'GET',
    success: function (data) {
      let i = 0;
      while (i < data.length) {
        users[data[i].id] = data[i].first_name + ' ' + data[i].last_name;
        i++;
      }
    }
  })
  $.ajax({
    url: url,
    type: 'POST',
    data: JSON.stringify({}),
    headers: {'Content-Type': 'application/json'},
    success: function (data) {
      let locations = {}
      for (let i = 0; i < data.length; i++) {
        let html = '<article>\n<div class="description"><h2>' + data[i].name + '</h2>' +
                   '<div class="price_per_day">' + '$' + data[i].price_per_day + '</div>' +
                   '<div class="desc_container">' +
                   '<div class="bike_image"><img src="' + data[i].img_url + '">' + '</div>' +
                   '<div class="bike_desc">' + data[i].description + 
                   '<p><br>Rent it from <span style="font-weight: 600">' + 
                    users[data[i].user_id] + '</span></p>' +
                   '</div></div></div></article>';
        $('section.bikes').append(html);
      }
    }
  });
  $('button').click(function () {
    $('section.bikes').text('');
  });
});

