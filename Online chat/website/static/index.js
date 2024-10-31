$(function() {

    $('#sendBtn'.bind('click', function() {
        var value = document.getElementById("msg").value
        console.log(value)
        $.getJSON('/send_message', 
            {val:value},
            function(data) {
                
            });
            return false;
    }));
});

function validate(name) {
    if(name.length >= 2) {
        return true;
    }
    return false;
}