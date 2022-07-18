$(document).ready(function() {
    $("#scan-btn").click(function() {
        $.ajax({
            url: "http://127.0.0.1:8080/",
            type: "GET",
            success: function(result){
                console.log(result)
                $("#card_id").val(result)
            },
            error: function(error){
                console.log(`Error ${error}`)
            }
        })
    })

    $('#datatable').DataTable();
    
})