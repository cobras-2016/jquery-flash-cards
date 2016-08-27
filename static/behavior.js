$(document).ready(function(){
  $('.collapsible-header').on('click', function(){
    $('.collapsible-body').css('color','black').css('border-top-color','#4CAF50')
  })
  $('.ph-button').on('click', function(){
    location.reload(true)
  })
  $(".dropdown-button").dropdown();
})
