$(document).ready(function(){
  $('value').hide()
  $('key').on('click', function(){
    $('value').toggle().css('color','black').css('border-top-color','#4CAF50')
  })
  $('.ph-button').on('click', function(){
    location.reload(true)
  })
})
