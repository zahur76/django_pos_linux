$(document).ready(function(){    

  let total = parseFloat($(".total").html().split('$')[1])
  
  $('.pay-button').click(function(event){
    event.preventDefault()
    let receivedAmount = $('#amount').val();
    if(receivedAmount >= total){      
      $('#pay-form').submit();
    }    
  })    
});