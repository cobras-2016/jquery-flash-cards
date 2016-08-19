$(document).ready(function(){
  $('value').hide()
  $('key').on('click', function(){
    // $('key').toggle()
    $('value').toggle()
  })
  $('right').on('click', function(){
    location.reload(true)
  })
})
