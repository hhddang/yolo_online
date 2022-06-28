$(document).ready(function(){
    
    $("#upload-image").change(function(event){
        var url = URL.createObjectURL(event.target.files[0]);
        $("#input").attr("src",url)
    });

});