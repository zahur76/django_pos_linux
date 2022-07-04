$(document).ready(function(){

    $(".open-category-modal").click(function(){
        let modalNumber = $(this).attr('value')
        $(`#addCategory-${modalNumber}`).show(); 
    })

    $(".close").click(function(){
        let modalNumber = $(this).attr('value')
        $(`#addCategory-${modalNumber}`).hide(); 
    })

});