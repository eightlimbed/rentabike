/*
 * Listens on each Category <input> field.
 * If the checkbox is checked, the category is added to an object called 'selected'
 * If the category is unchecked, it is removed from 'selected'
 * The <H4> Category tag is updated dynamically when boxes are checked/unchecked
 */
$(document).ready(function () {
  let categoryIds = [];
  let categoryNames = [];
  $('input#cats').on('click', function () {
    if ($(this).prop('checked')) {
      categoryNames.push($(this).attr('data-name'));
      categoryIds.push($(this).attr('data-id'));
      let txt = categoryNames.join(', ');
      if (txt.length > 25) {
        $('.categories h4').text(txt.substr(0, 25) + '...');
      } else {
        $('.categories h4').text(txt);
      }
    } else {
      let nameIndex = categoryNames.indexOf($(this).attr('data-name'));
      let idIndex = categoryIds.indexOf($(this).attr('data-id').replace(',', ''));
      categoryNames.splice(nameIndex, 1);
      categoryIds.splice(idIndex, 1);
      let txt = categoryNames.join(', ');
      if (txt.length > 25) {
        $('.categories h4').text(txt.substr(0, 25) + '....');
      } else {
        $('.categories h4').text(txt);
      }
    }
  });
  $('button').click(function () {
    let cIds = [];
    for (let i = 0; i < categoryIds.length; i++) {
      categoryIds[i] = categoryIds[i].replace(',', '');
      cIds.push(categoryIds[i]);
    }
    let url = 'http://0.0.0.0:5001/api/v1/bikes_by_categories/' + cIds.join(',');
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
