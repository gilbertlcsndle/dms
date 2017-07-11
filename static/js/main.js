$(function(){
    $("[type='text'], \
       [type='number'], \
       [type='password'], \
       [type='date'], \
       select, \
       textarea")
        .addClass('form-control');
    
    if (!$('.navbar-brand').text()) {
        $('.navbar-brand').text($('title').text());
    }
   
     $(".content").on('click', '.confirm-delete', function(e){
        e.preventDefault();
        
        var confirm_delete = $(this);
        swal({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!',
            cancelButtonText: 'No, cancel!',
        }).then(function () {
            confirm_delete.parent('form').submit();
        });
    });

    $('.go-back').click(function(e){
        e.preventDefault();
        history.back(1);
    });

    $("[type='number']").attr('min', '0');

    $('#id_bdate').datetimepicker({ format: 'YYYY-MM-DD' }).attr('type', 'text');
});