$(document).ready(function(){
  $('value').hide()
  $('key').on('click', function(){
    // $('key').toggle()
    $('value').fadeIn('slow').toggle()
  })
  $('right').on('click', function(){
    location.reload(true)
  })
})
