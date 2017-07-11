$(function(){
    // $.get("", {cert_name: "cert-5.html"}, function(data) {
    //     $('#certificate').html(data);
    // });
    
    $('#select-cert').change(function(){
        if ($(this).val()) {
            $.get("", {cert_name: $(this).val()}, function(data) {
                $('#certificate').html(data);
            });
            $('#no-cert').hide();
        } else {
            $('#certificate').empty();
            $('#no-cert').show();
        }

    });

    /* shrink if theres a character on this element
    else back to default width */
    $("#certificate")
        .on('keyup', "[contenteditable='true']", function(){

        var chars = $.trim($(this).text());

        if (chars) {
            $(this).width('auto');
            $('#print, #clear-text').removeAttr('disabled');
        } else {
            $(this).width('100px');
            $('#print, #clear-text').attr('disabled', 'disabled');
        }
    });

    $("#print").click(function(){
        $('#certificate').print();
    });

    $("#clear-text").click(function(){
        $("[contenteditable='true']").empty().width('100px');
        $('#print, #clear-text').attr('disabled', 'disabled');
    });

    $('#select-cert').selectize(selectize_opts);
});