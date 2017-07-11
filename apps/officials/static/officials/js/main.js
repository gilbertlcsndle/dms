$(function(){
    datatable_default.dom = '' +
        '<"row"' +
        '   <"col-sm-6"f>' +
        '   <"col-sm-6 text-right add-btn-container">' +
        '>' +
        't' +
        '<"row"'+
        '   <"col-sm-6"i>' +
        '   <"col-sm-6"p>' +
        '>';
    datatable_default.aoColumnDefs = [
    {
        'bSortable': false,
        'aTargets': [0, 7],
    }
    ];
    datatable_default.order = [[2, 'asc']];
    datatable_default.responsive = true;

    $('#officials').DataTable(datatable_default);

    $('.add-btn-container').html($('.add-btn').html());

    $('#id_position').addClass('list-inline');

    $('[type="submit"]').click(function(e){
        e.preventDefault();
        $('#id_resident').removeAttr('disabled');
        $(this).parents('form').submit();
    });

    $('#id_resident').selectize(selectize_opts);
});