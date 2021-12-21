$(document).ready(function(){

    $(".login").click(function(){       
        $("#loginModal").show();                          
    });
    
    $(".close").click(function(){        
        $("#loginModal").hide();        
    });

    /* Function to clear flash messages after 3's*/  
    setTimeout(function(){
        $(".flash-message").hide("slow");
    }, 3000 ); // 5 secs

    /* Allow password to become visible*/ 
    $("body").on('click', '.eye-icon', function() {
        $(this).toggleClass("fa-eye fa-eye-slash");
        input = $("#password");
        if (input.attr("type") === "password") {
          input.attr("type", "text");
        } else {
          input.attr("type", "password");
        }
    });

    // language dropdown
    $('#dropdownMenuButton').click(function(){
        console.log('zahur')
        $('.language-menu').toggleClass("style");
        let myClass = $('#language').attr("class");
        if(myClass==="language-menu style"){
            $("#language").attr('style', "visibility:visible")
        }else{
            $("#language").attr('style', "visibility:hidden")
        }
    })
          
});