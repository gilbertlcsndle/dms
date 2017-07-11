$(function(){
    datatable_default.dom = 
        '<"row"' +
        '   <"col-sm-4"f>'+
        '   <"#custom-filter.col-sm-4">'+
        '   <"#btn-print.col-sm-4 text-right">'+
        '>' +
        't' +
        '<"row"'+
        '   <"col-sm-6"i>' +
        '   <"col-sm-6"p>' +
        '>';

    $('#events').DataTable(datatable_default);

    $('#type').appendTo('#custom-filter');

    $("#btn-print").append(
        '<button type="button" id="print"'+
        '   class="btn btn-primary btn-fill">' +
        '   <span class="glyphicon glyphicon-print"></span>'  +
        '   Print' +
        '</button>'
    );

    $('#id_resident, #id_event').selectize(selectize_opts);

    $('.content').on('change', '#type', function() {
        if ($(this).val()) { 
            window.location = 
                $('#sidebar').data('current') + 
                '?type=' +
                $(this).val();
        } else {
            window.location = $('#sidebar').data('current');
        }
    });

    $('#print').click(function() {
        $('#events').print();
    });
});