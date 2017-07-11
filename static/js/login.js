$(function() {
    $('#btn-forgot-pass').click(function() {
        swal({
            title: 'Enter your ID to help us identify you.',
            input: 'text',
            showCancelButton: true,
            confirmButtonText: 'Submit',
            preConfirm: function (text) {
                return new Promise(function (resolve, reject) {
                    $.get(
                        $('#btn-forgot-pass').data('sec-info'),
                        { username: text },
                        function (data) {
                            if (data.is_valid) {
                                resolve();
                            } else {
                                reject(data.error);
                            }
                        }
                    );
                });
            }
        }).then(function (text){
            validate_security_info(text);
        });

        function validate_security_info(username) {
            $.get(
                $('#btn-forgot-pass').data('sec-info'), 
                { 'username': username },
                function(questions) {
                    validate_answers(questions, username);
                },
                'json'
            );
        }

        function validate_answers(questions, username) {
            swal.setDefaults({
                input: 'text',
                confirmButtonText: 'Next &rarr;',
                showCancelButton: true,
                animation: false,
                progressSteps: ['1', '2', '3']
            });

            var steps = [
                {
                    title: 'Question 1',
                    text: questions['question1']
                },
                {
                    title: 'Question 2',
                    text: questions['question2']
                },
                {
                    title: 'Question 3',
                    text: questions['question3']
                },
            ];

            swal.queue(steps).then(function (result) {
                swal.resetDefaults();
                
                $.post(
                    $('#btn-forgot-pass').data('sec-info'),
                    {
                        csrfmiddlewaretoken: 
                            $('[name="csrfmiddlewaretoken"]').val(),
                        username: username,
                        answer1: result[0],
                        answer2: result[1],
                        answer3: result[2]
                    },
                    function (data) {
                        if (data.is_valid) {
                            create_new_pass(username);
                        } else {
                            swal(
                                'Oops...',
                                'You did not pass the test. Please try again.',
                                'error'
                            );
                        }
                    }
                );
            }, function () {
                swal.resetDefaults();
            });    
        }

        function create_new_pass(username) {
             swal({
                title: 'Create your new password',
                html: '<input type="password" ' +
                      ' class="swal2-input" id="id_new_password1"' + 
                      ' placeholder="New password"/>' +
                      '<br>' +
                      '<input type="password" class="swal2-input"' +
                      ' id="id_new_password2"' +
                      ' placeholder="Confirm new password"/>',
                confirmButtonText: 'Submit',
                preConfirm: function () {
                    return new Promise(function (resolve, reject) {
                        new_password1 = $.trim($('#id_new_password1').val());
                        new_password2 = $.trim($('#id_new_password2').val());

                        if (!(new_password1 && new_password2)) {
                            reject('Please enter your new password.');
                        } else {
                            $.post(
                                $('#btn-forgot-pass').data('forgot-pass'), 
                                {
                                    csrfmiddlewaretoken: 
                                        $('[name="csrfmiddlewaretoken"]').val(),
                                    username: username,  
                                    new_password1: new_password1,
                                    new_password2: new_password2
                                },
                                function (data) {
                                    if (data.is_valid) {
                                        $('#id_username').val(username);
                                        resolve();
                                    } else {
                                        $.each(data['errors'], function (i, v) {
                                            reject(v);
                                        });
                                    }
                                },
                                'json'
                            );
                        }
                    });

                }
            }).then(function () {
                swal(
                    'Success!',
                    'You have successfully changed your password.',
                    'success'
                );
            });
        }
    });
});