/*
 * Listens on each Category and City field.
 * If the checkbox is checked, the selection is added to a list that will be
 * used to make an API call, and the name of the selection is rendered in the
 * <H4> tag.
 */
let catId = '';
let catName = '';
let cityId = '';
let cityName = '';
$(document).ready(function () {
  $('input#cities').on('click', function () {
    if ($(this).prop('checked')) {
      cityName = $(this).attr('data-name');
      cityId = $(this).attr('data-id');
      $('.locations h4').text(cityName);
    } else {
      $('.locations h4').text('');
    }
  });
  $('input#cats').on('click', function () {
    if ($(this).prop('checked')) {
      catName = $(this).attr('data-name');
      catId = $(this).attr('data-id');
      $('.categories h4').text(catName);
    } else {
      $('.categories h4').text('');
    }
  });
  $('button').click(function () {
    let cityCat = []
    if (cityId) {
      cityCat.push(cityId);
    }
    if (catId) {
      cityCat.push(catId);
    }
    let url = 'http://0.0.0.0:5001/api/v1/bikes_by_categories/' + cityCat.join(',');
    $.ajax({
      url: url,
      type: 'POST',
      success: function (data) {
        for (let i = 0; i < data.length; i++) {
          let html = '<article>\n<div class="description"><h2>' + data[i].name + '</h2>' +
                     '<div class="price_per_day">' + '$' + data[i].price_per_day + '</div>' +
                     '<div class="desc_container">' +
                     '<div class="bike_image"><img src="' + data[i].img_url + '">' + '</div>' +
                     '<div class="bike_desc">' + data[i].description + 
                     '</div></div></div></article>';
          $('section.bikes').append(html);
        }
      }
    });
  });
});
