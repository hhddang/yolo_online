$(document).ready(function(){
    
    $("#upload-image").change(function(event){
        var url = URL.createObjectURL(event.target.files[0]);
        $(".image-input .image-display").attr("src",url)
    });
    
    $(".button").click(function(){
        $("#form1").submit()
        console.log("submitted")
    });
});