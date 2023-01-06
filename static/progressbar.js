function ajaxClick() {

  var timerId, percent;

  // reset progress bar
  percent = 0;
  $('#upload').attr('disabled', true);
  $('#load').css('width', '0px');
  $('#load').addClass('progress-bar-striped active');

  timerId = setInterval(function() {

    // increment progress bar
    percent += 5;
    $('#load').css('width', percent + '%');
    $('#load').html(percent + '%');


    if (percent >= 100) {
      clearInterval(timerId);
      $('#upload').attr('disabled', false);
      $('#load').removeClass('progress-bar-striped active');
      $('#load').html('Загрузка завершена');
    }
  }, 400)
}

