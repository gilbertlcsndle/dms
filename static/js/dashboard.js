$(function() {
    var event_url = $('#calendar').data('url');

    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'listYear, month,agendaWeek,agendaDay'
        },
        events: event_url,
        eventRender: function(event, element) {
            $(element).tooltip({
                title: event.description,
                container: 'body',
            });
        },
        buttonText : {
            list:     'year'
        }
    });

    
    bootstrap_fileinput_default.uploadUrl = $('#files-url').data('add');
    bootstrap_fileinput_default.uploadExtraData = {
        'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
    };
    bootstrap_fileinput_default.fileActionSettings.showUpload = false;
    bootstrap_fileinput_default.dropZoneTitle = 
      '<span class="glyphicon glyphicon-download-alt"></span> <br \>' +
      'Drop files here or click to upload.';
    bootstrap_fileinput_default.dropZoneClickTitle = '';
    bootstrap_fileinput_default.showBrowse = false;
    bootstrap_fileinput_default.showUpload = true;
    bootstrap_fileinput_default.allowedPreviewTypes = ['image', 'text', 'video', 'audio'];
    bootstrap_fileinput_default.previewSettings = {
        image : {width: "auto", height: "80px"},
    };
    
    $('#id_file').fileinput(bootstrap_fileinput_default);

    $('#id_file')
        .on('filebatchuploadcomplete', function(event, files, extra) {
        
        window.location = $('#files-url').data('success');
    });

    datatable_default.lengthMenu = [5];
    datatable_default.responsive = true;
    datatable_default.aoColumnDefs = [
        {
            'bSortable': false,
            'aTargets': 3,
        }
    ];
    $('#files').DataTable(datatable_default);
});