$(document).ready(function(){

    if (document.getElementById('check').value=="yes"){
        check();
    }


    $('#firstname').keyup(function(){
        $.ajax({
            url: '/firstname',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('#firstname_err').html(serverResponse)
            }
        })
    })

    $('#lastname').keyup(function(){
        $.ajax({
            url: '/lastname',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('#lastname_err').html(serverResponse)
            }
        })
    })

    $('#username').keyup(function(){
        $.ajax({
            url: '/username',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('#username_err').html(serverResponse)
            }
        })
    })

    $("#email").keyup(function(){
        $.ajax({
            url: '/email',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('#email_err').html(serverResponse)
            }
        })
    })

    $('#password').keyup(function(){
        $.ajax({
            url: '/password',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('#password_err').html(serverResponse)
            }
        })
    })

    $('#confirm').keyup(function(){
        $.ajax({
            url: '/confirm',
            method: 'post',
            data: $('#reg_form').serialize(),
            success: function(serverResponse){
                $('#confirm_err').html(serverResponse)
            }
        })
    })
    

})

function check(){
    $.ajax({
        url: '/register',
        method: 'post',
        data: $('#reg_form').serialize(),
        success: function(serverResponse){
            $('#reg_err').html(serverResponse)
        }
    })
    $.ajax({
        url: '/firstname',
        method: 'post',
        data: $('#reg_form').serialize(),
        success: function(serverResponse){
            $('#firstname_err').html(serverResponse)
        }
    })
    $.ajax({
        url: '/email',
        method: 'post',
        data: $('#reg_form').serialize(),
        success: function(serverResponse){
            $('#email_err').html(serverResponse)
        }
    })
    $.ajax({
        url: '/lastname',
        method: 'post',
        data: $('#reg_form').serialize(),
        success: function(serverResponse){
            $('#lastname_err').html(serverResponse)
        }
    })
    $.ajax({
        url: '/username',
        method: 'post',
        data: $('#reg_form').serialize(),
        success: function(serverResponse){
            $('#username_err').html(serverResponse)
        }
    })
    $.ajax({
        url: '/password',
        method: 'post',
        data: $('#reg_form').serialize(),
        success: function(serverResponse){
            $('#password_err').html(serverResponse)
        }
    })
    $.ajax({
        url: '/confirm',
        method: 'post',
        data: $('#reg_form').serialize(),
        success: function(serverResponse){
            $('#confirm_err').html(serverResponse)
        }
    })
}