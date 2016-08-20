$(document).ready(function(){
  $('value').hide()
  $('key').on('click', function(){
    $('value').toggle()
    $('value').css('color','black')
  })
  $('.ph-button').on('click', function(){
    location.reload(true)
  })
})
