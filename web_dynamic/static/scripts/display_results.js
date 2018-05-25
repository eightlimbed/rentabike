// Loops through all Places and displays them on web page
$(document).ready(function () {
  let url = 'http://0.0.0.0:5001/api/v1/bikes_search/';
  $.ajax({
    url: url,
    type: 'POST',
    data: JSON.stringify({}),
    headers: {'Content-Type': 'application/json'},
    success: function (data) {
      for (let i = 0; i < data.length; i++) {
        let html = '<article>\n<div class="title">\n<h2>' + data[i].name + '</h2>' +
                       '<div class="price_per_day">' + data[i].price_per_day + '</div></div>' +
                       '<div class="information">' + 'Yo!' + '</div>' +
                       '<div class="description">' + data[i].description + '</div></article>';
        $('section.bikes').append(html);
      }
    }
  });
  $('button').click(function () {
    $('section.bikes').text('');
  });
});

