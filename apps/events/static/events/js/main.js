$(function(){
    $('#id_start').val(moment($('#id_start').val()).format('MMMM D, YYYY hh:mm A'));
    $('#id_end').val(moment($('#id_end').val()).format('MMMM D, YYYY hh:mm A'));

    $('#id_start, #id_end').datetimepicker({ format: 'MMMM D, YYYY hh:mm A' });

    var submit_event = $('#event-form [type="submit"]').click(function(e){
        e.preventDefault();
        var start = $(this).parent('form').find('#id_start');
        var end = $(this).parent('form').find('#id_end');


        // checks if the end date is after the start date
        if (start.val() && end.val()) {
            start_date = new Date(start.val());
            end_date = new Date(end.val());
            
            var is_valid = false;

            
            var end_form_group = end.parent('.form-group');

            // create new errorlist if not existed
            if (!end_form_group.find('.errorlist').length) {
                end_form_group.append('<ul class="errorlist"></ul>');
            }

            if (
                end_date > start_date && 
                start_date.getTime() !== end_date.getTime()
            ) {
                is_valid = true;

                // remove existing error if exist
                if (end_form_group.find('.errorlist').length) {
                    end_form_group
                        .find('.errorlist li:contains('+ errormsg +')')
                        .remove();
                }
            } else {
                var errormsg = 'End date must be after the start date.';

                // add new errormsg if not existed
                if (
                    !end_form_group.find(
                        '.errorlist li:contains('+ errormsg +')'
                    ).length
                ) {
                    end_form_group
                        .find('.errorlist')
                        .append('<li>'+ errormsg +'</li>');
                }
            }

            if (is_valid) {
                // checks if the event conflicts on the other event
                $.get($('#event-data').data('url'), function (data) {
                    var conflict_events = '';

                    for (i in data) {
                        var start_date_data = new Date(data[i].start);
                        var end_date_data = new Date(data[i].end);

                        
                        if ($('#event-data').data('id') !== data[i].pk) {
                            if(
                                !(
                                    start_date_data >= end_date || 
                                    end_date_data <= start_date
                                )
                            ){
                                is_valid = false;
                                conflict_events += data[i].title + ', ';

                                break;
                            } else {
                                is_valid = true;
                            }
                        }

                    }

                    if (is_valid) {
                        start.val(moment(start_date).format('MMMM D, YYYY hh:mm A'));
                        end.val(moment(end_date).format('MMMM D, YYYY hh:mm A'));

                        submit_event.parent('form').submit();
                    } else {
                        var errormsg = 'Conflict with ' + 
                            conflict_events.substr(0, conflict_events.length - 2) +
                            '.';

                        // add new errormsg if not existed
                        if (
                            !end_form_group.find(
                                '.errorlist li:contains('+ errormsg +')'
                            ).length
                        ) {
                            end_form_group
                                .find('.errorlist')
                                .append('<li>'+ errormsg +'</li>');
                        }
                    }
                });
            }
        }   
    });

    datatable_default.aoColumnDefs = [
        {
            'bSortable': false,
            'aTargets': [3]
        }
    ];
    datatable_default.responsive = true;
    datatable_default.order = [[1, 'desc']];

    $('#events').DataTable(datatable_default);

    $('.event-datetime').each(function() {
        $(this).text(moment($(this).text()).format('MMMM D, YYYY hh:mm A'));
    });

    $('.view-description').click(function(){
        $.get(
            $(this).data('url'), 
            { pk: $(this).data('pk') },
            function(data) {
                var start = moment(data.start).format('MMMM D, YYYY hh:mm A');
                var end = moment(data.end).format('MMMM D, YYYY hh:mm A');

                swal(
                    data.title, 
                    data.description +
                    "<br /><br />" +
                    start + 
                    "<br />" + 
                    "to " + end
                );
            }
        );

    });

});