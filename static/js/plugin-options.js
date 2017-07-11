// default variables as options to the plugins
var datatable_default = {
    'dom': 
        'f' +
        't' +
        '<"row"'+
        '   <"col-sm-6"i>' +
        '   <"col-sm-6"p>' +
        '>',
    'bLengthChange': false,
    'lengthMenu': [10]
};

var bootstrap_fileinput_default = {
    showUpload: false,
    showCaption: false,
    showClose: false,
    fileActionSettings: {
        showZoom: false,
    },
    browseOnZoneClick: true,
    browseLabel: 'Browse',
    browseClass: 'btn btn-primary btn-fill'
};

var selectize_opts = {
    sortField: [
        {
            field: 'text',
            direction: 'asc'
        },
        {
            field: '$score'
        }
    ],
};
