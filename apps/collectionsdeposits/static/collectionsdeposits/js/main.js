$(function(){
    // datatable
    datatable_default.aoColumnDefs = [
        {
            'bSortable': false,
            'aTargets': [4]
        }
    ];
    datatable_default.dom = 
      '<"row"' +
      ' <"col-sm-4"f>' +
      ' <"#total.col-sm-4 text-center">' +
      ' <"#btn-print.col-sm-4 text-right">' +
      '>' + 
      't' +
      '<"row"' +
      ' <"col-sm-6"i>' +
      ' <"col-sm-6"p>' +
      '>';
    datatable_default.order = [0, 'desc'];
    datatable_default.responsive = true;

    $('#collections').DataTable(datatable_default);

    $("#btn-print").append(
        '<button type="button" id="print"'+
        '   class="btn btn-primary btn-fill">' +
        '   <span class="glyphicon glyphicon-print"></span>'  +
        '   Print' +
        '</button>'
    );

    $('#id_payor').selectize(selectize_opts);    

    selectize_opts.onChange = function (value) {
        $.get($('#id_particular').parent('div').data('url'), { pk: value }, function (data){
            $('#id_collection').val(data);
        });
    };

    $('#total').append('Total: ' + $('#td-collection').data('total'));

    $('#id_particular').selectize(selectize_opts);    

    $('#print').click(function() {
        $('#collections').print();
    });

});