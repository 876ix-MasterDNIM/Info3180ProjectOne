var imgs;
$(document).ready(function() {
    
    $('#url').focusout(function() {
        var regex = /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/
        // if (regex.exec($('#url').val())) {
            $.ajax(
               {
                   url: '/crawl',
                   method: 'POST',
                   data: JSON.stringify({'url' : $('#url').val()}),
                   contentType: 'application/json'
               })
               .done(function(response) {
                   imgs = response['imgs'];
                   $('.imgs').empty();
                   if (response['imgs'] == 'no images') {
                       $('.imgheading').text('No images could be found. Try another url or a default image will be used');
                   } else {
                       console.log(response['imgs']);
                       $('.imgheading').text('Select Image To Use For Item Below');
                       var numOfRows = Math.ceil(imgs.length / 3);
                       for(var i = 1; i <= numOfRows; i++) {
                           $('.imgs').append(
                               '<label>' +
                            '<input type="radio" name="img" checked />' + 
                            '<img style="width: 180px; height: 180px;" class="img" src="' + imgs[1*i] + '"class="col s4"></img>' +
                  '</label>' +
                  '<label>' +
                    '<input type="radio" name="img" />' +
                    '<img style="width: 180px; height: 180px;" class="img" src="' + imgs[2*i] + '"class="col s4"></img>' +
                  '</label>' +
                  '<label>' +
                    '<input type="radio" name="img" />' +
                    '<img style="width: 180px; height: 180px;" class="img" src="' + imgs[3*i] + '"class="col s4"></img>' +
                  '</label>');
                       }
                   }
               })
               .fail(function(jqXHR, txt) {
                   
               });
        // } else {
        //     $('#url').addClass('red lighten-2');
        //     $('#url').val('Enter a valid url');
        // }
        
    });
    // $('#url').focus(function() {
    //     if ($('#url').hasClass('red')) {
    //         $('#url').removeClass('red lighten-2');
    //         $('#url').val('');
    //     }
    // });
    

});