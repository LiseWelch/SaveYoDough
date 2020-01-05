var check = "";

function reset() {
    $('#payment_to').val("-- select --")
    $('#payment_from').val("-- select --")
    $('#type').val("-- select --")
    $('#on').val("-- select --")
    $('#to').val("-- select --")
    $('#card_name').val("");
    $('#card_balance').val("");
    $('#account_name').val("");
    $('#account_balance').val("");
};

$(document).ready(function(){

    $('#add_transactions').hide()
    $('#add_accounts').hide()
    $('#add_cards').hide()
    $('#edit_cards').hide()
    $('#edit_accounts').hide()

    $('#purchase_options').hide()
    $('#payment_options').hide()
    $('#deposit_options').hide()

    $('#add_t').click(function(){
        reset();
        if ($('#add_cards').is(":visible")) {
            $('#add_cards').slideUp(function() {
                $('#cards').slideDown();
            })
            $('#transactions').slideUp(function(){
                $('#add_transactions').slideDown();
        })
        } else if ($('#add_accounts').is(":visible")) {
            $('#add_accounts').slideUp(function() {
                $('#accounts').slideDown();
            })
            $('#transactions').slideUp(function(){
                $('#add_transactions').slideDown();
        })
        } else if ($('#edit_cards').is(":visible")) {
            $('#edit_cards').slideUp(function() {
                $('#cards').slideDown();
            })
            $('#transactions').slideUp(function(){
                $('#add_transactions').slideDown();
            })
        } else if ($('#edit_accounts').is(":visible")) {
            $('#edit_accounts').slideUp(function() {
                $('#accounts').slideDown();
            })
            $('#transactions').slideUp(function(){
                $('#add_transactions').slideDown();
            })
        } else {
            $('#transactions').slideUp(function(){
                $('#add_transactions').slideDown();
        })
        }
    })

    $('#add_a').click(function(){
        reset();
        if ($('#add_cards').is(":visible")) {
            $('#add_cards').slideUp(function() {
                $('#cards').slideDown();
            })
            $('#accounts').slideUp(function(){
                $('#add_accounts').slideDown();
        })
        } else if ($('#add_transactions').is(":visible")) {
            $('#add_transactions').slideUp(function() {
                $('#transactions').slideDown();
                $('#payment_options').hide()
                $('#purchase_options').hide()
                $('#deposit_options').hide()
            })
            $('#accounts').slideUp(function(){
                $('#add_accounts').slideDown();
        })
        } else if ($('#edit_cards').is(":visible")) {
            $('#edit_cards').slideUp(function() {
                $('#cards').slideDown();
            })
            $('#accounts').slideUp(function(){
                $('#add_accounts').slideDown();
            })
        } else {
            $('#accounts').slideUp(function(){
                $('#add_accounts').slideDown();
        })
        }
    })

    $('#add_c').click(function(){
        reset();
        if ($('#add_accounts').is(":visible")) {
            $('#add_accounts').slideUp(function() {
                $('#accounts').slideDown();
            })
            $('#cards').slideUp(function(){
                $('#add_cards').slideDown();
        })
        } else if ($('#add_transactions').is(":visible")) {
            $('#add_transactions').slideUp(function() {
                $('#transactions').slideDown();
                $('#payment_options').hide()
                $('#purchase_options').hide()
                $('#deposit_options').hide()
            })
            $('#cards').slideUp(function(){
                $('#add_cards').slideDown();
        })
        } else if ($('#edit_accounts').is(":visible")) {
            $('#edit_accounts').slideUp(function() {
                $('#accounts').slideDown();
            })
            $('#cards').slideUp(function(){
                $('#add_cards').slideDown();
            })
        } else {
            $('#cards').slideUp(function(){
                $('#add_cards').slideDown();
        })
        }
    })

    $('#type').on("change", function(){
        check = $('#type option:selected').val().toLowerCase();
        if ($('#type option:selected').val()=="Purchase") {
            $.ajax({
                url: './purchase',
                method: 'post',
                data: $(this).serialize(),
                success: function(serverResponse){
                    $('#purchase_options').html(serverResponse);
                    if ($('#payment_options').is(":visible")) {
                        $('#payment_options').slideUp(function(){
                            $('#purchase_options').slideDown() 
                        })
                    } else if ($('#deposit_options').is(":visible")) {
                            $('#deposit_options').slideUp(function(){
                                $('#purchase_options').slideDown() 
                            })
                    } else if ($('#withdraw_options').is(":visible")) {
                        $('#withdraw_options').slideUp(function(){
                            $('#purchase_options').slideDown() 
                        })
                    } else {
                        $('#purchase_options').slideDown()
                    }
                }
            })
        } else if ($('#type option:selected').val()=="Withdraw") {
            $.ajax({
                url: './withdraw',
                method: 'post',
                data: $(this).serialize(),
                success: function(serverResponse){
                    $('#withdraw_options').html(serverResponse);
                    if ($('#payment_options').is(":visible")) {
                        $('#payment_options').slideUp(function(){
                            $('#withdraw_options').slideDown() 
                        })
                    } else if ($('#deposit_options').is(":visible")) {
                            $('#deposit_options').slideUp(function(){
                                $('#withdraw_options').slideDown() 
                            })
                    } else if ($('#purchase_options').is(":visible")) {
                        $('#purchase_options').slideUp(function(){
                            $('#withdraw_options').slideDown() 
                        })
                    }  else {
                        $('#withdraw_options').slideDown()
                    }
                }
            })
        }else if ($('#type option:selected').val()=="Payment") {
            $.ajax({
                url: './payment',
                method: 'post',
                data: $(this).serialize(),
                success: function(serverResponse){
                    $('#payment_options').html(serverResponse);
                    if ($('#purchase_options').is(":visible")) {
                        $('#purchase_options').slideUp(function(){
                            $('#payment_options').slideDown() 
                        })
                    } else if ($('#deposit_options').is(":visible")) {
                            $('#deposit_options').slideUp(function(){
                                $('#payment_options').slideDown() 
                            })
                    } else if ($('#withdraw_options').is(":visible")) {
                        $('#withdraw_options').slideUp(function(){
                            $('#payment_options').slideDown() 
                        })
                    } else {
                        $('#payment_options').slideDown()
                    }
                }
            })
        } else if ($('#type option:selected').val()=="Deposit") {
            $.ajax({
                url: './deposit',
                method: 'post',
                data: $(this).serialize(),
                success: function(serverResponse){
                    $('#deposit_options').html(serverResponse);
                    if ($('#payment_options').is(":visible")) {
                        $('#payment_options').slideUp(function(){
                            $('#deposit_options').slideDown() 
                        })
                    } else if ($('#purchase_options').is(":visible")) {
                            $('#purchase_options').slideUp(function(){
                                $('#deposit_options').slideDown() 
                            })
                    }  else if ($('#withdraw_options').is(":visible")) {
                        $('#withdraw_options').slideUp(function(){
                            $('#deposit_options').slideDown() 
                        })
                    } else {
                        $('#deposit_options').slideDown()
                    }
                }
            })
        } else {
            if ($('#payment_options').is(":visible")){
                $('#payment_options').slideUp()
            }
            if ($('#purchase_options').is(":visible")){
                $('#purchase_options').slideUp()
            }
            if ($('#deposit_options').is(":visible")){
                $('#deposit_options').slideUp()
            }

        }
    })

    $('#account_name').keyup(function(){
        $.ajax({
            url: './accountname',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('#account_name_err').html(serverResponse)
            }
        })
    })

    $('#card_name').keyup(function(){
        $.ajax({
            url: './cardname',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('#card_name_err').html(serverResponse)
            }
        })
    })
    
    $('#edit_card_name').keyup(function(){
        $.ajax({
            url: './edit/cardname',
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('#edit_card_name_err').html(serverResponse)
            }
        })
    })

    $('#a_form').submit(function(e){
        e.preventDefault()
        if (document.getElementById('a_valid').value=="yes") {
            $.ajax({
                url: './create/account',
                method: 'post',
                data: $('#a_form').serialize(),
                success: function(serverResponse){
                    $('#account_table').hide();
                    $('#a_err').hide();
                    $('#deleted_accounts').hide()
                    $('#added_accounts').show()
                    $('#account_name').val("");
                    $('#account_balance').val("");
                    $('#added_accounts').html(serverResponse);
                    $('#add_accounts').slideUp(function() {
                        $('#accounts').slideDown();
                    });
                }
            })
        } else if (document.getElementById('a_valid').value=="no") {
            $.ajax({
                url: './create/account',
                method: 'post',
                data: $('#a_form').serialize(),
                success: function(serverResponse){
                    $('#a_err').show();
                    $('#a_err').html(serverResponse);
                }
            })
            return false
        }
        })

        $('#t_form').submit(function(e){
            e.preventDefault()
            $.ajax({
                url: ('./add/'+check),
                method: 'post',
                data: $('#t_form').serialize(),
                success: function(serverResponse){
                    $('#payment_options').hide()
                    $('#purchase_options').hide()
                    $('#deposit_options').hide()
                    $('#withdraw_options').hide()
                    $('#tran_table').hide();
                    $('#t_err').hide();
                    $('#deleted_tran').hide()
                    $('#added_tran').show()
                    $('#desc').val("");
                    $('#amount').val("");
                    $('#type').val("-- select --");
                    $('#added_tran').html(serverResponse)
                    $('#add_transactions').slideUp(function() {
                        $('#transactions').slideDown();
                      });
                }
            })

            $.ajax({
                url: './update/cards',
                method: 'get',
                success: function(serverResponse){
                    $('#card_table').hide();
                    $('#deleted_cards').hide();
                    $('#added_cards').show();
                    $('#added_cards').html(serverResponse);
                }
            })

            $.ajax({
                url: './update/accounts',
                method: 'get',
                success: function(serverResponse){
                    $('#account_table').hide();
                    $('#deleted_accounts').hide();
                    $('#added_accounts').show();
                    $('#added_accounts').html(serverResponse);
                }
            })
            return false;
        })
    
        $('#c_form').submit(function(e){
        e.preventDefault()
        if (document.getElementById('c_valid').value=="yes") {
            $.ajax({
                url: './create/card',
                method: 'post',
                data: $('#c_form').serialize(),
                success: function(serverResponse){
                    $('#card_table').hide();
                    $('#c_err').hide();
                    $('#deleted_cards').hide()
                    $('#added_cards').show()
                    $('#card_name').val("");
                    $('#card_balance').val("");
                    $('#added_cards').html(serverResponse);
                    $('#add_cards').slideUp(function() {
                        $('#cards').slideDown();
                    });
                }
            })
        } else if (document.getElementById('c_valid').value=="no") {
            $.ajax({
                url: './create/card',
                method: 'post',
                data: $('#c_form').serialize(),
                success: function(serverResponse){
                    $('#c_err').show();
                    $('#c_err').html(serverResponse);
                }
            })
            return false
        }
        })
        
        $('#card_save').click(function(e){
            e.preventDefault()
            if (document.getElementById('edit_c_valid').value=="no") {
                $.ajax({
                    url: './update/card',
                    method: 'post',
                    data: $('#c_edit').serialize(),
                    success: function(serverResponse){
                        $('#edit_c_err').show();
                        $('#edit_c_err').html(serverResponse);
                    }
                })
            } else {
                $.ajax({
                    url: ('./update/card'),
                    method: 'post',
                    data: $('#c_edit').serialize(),
                    success: function(serverResponse){
                        $('#added_cards').hide()
                        $('#card_table').hide()
                        $('#cards').show(function(){
                            $('#edit_cards').hide()
                        })
                        $('#deleted_cards').show()
                        $('#deleted_cards').html(serverResponse);
                }
                })
            }
            return false
        })
        
        $('#a_edit').submit(function(e){
            e.preventDefault()
            if (document.getElementById('edit_a_valid').value=="no") {
                $.ajax({
                    url: './update/account',
                    method: 'post',
                    data: $('#a_edit').serialize(),
                    success: function(serverResponse){
                        $('#edit_a_err').show();
                        $('#edit_a_err').html(serverResponse);
                    }
                })
            } else {
                $.ajax({
                    url: ('./update/account'),
                    method: 'post',
                    data: $('#a_edit').serialize(),
                    success: function(serverResponse){
                        $('#account_table').hide();
                        $('#a_err').hide();
                        $('#deleted_accounts').hide()
                        $('#added_accounts').show()
                        $('#account_name').val("");
                        $('#account_balance').val("");
                        $('#added_accounts').html(serverResponse);
                        $('#edit_accounts').slideUp(function() {
                            $('#accounts').slideDown();
                    });
                }
                })
            }
            return false
        })

        $('#cancel_a').click(function(){
            $('#add_accounts').slideUp(function(){
                $('#accounts').slideDown()
        })
        })

        $('#cancel_c').click(function(){
            $('#add_cards').slideUp(function(){
                $('#cards').slideDown()
        })
        })
        $('#cancel_t').click(function(){
            $('#add_transactions').slideUp(function(){
                $('#transactions').slideDown()
                $('#payment_options').hide()
                $('#purchase_options').hide()
                $('#deposit_options').hide()
        })
        })

})

function card_del(id) {
    $.ajax({
        url: ('./delete/card/'+id),
        method: 'post',
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#added_cards').hide()
            $('#card_table').hide()
            $('#deleted_cards').show()
            $('#deleted_cards').html(serverResponse);
        }
    })
    $.ajax({
        url: './update/transactions',
        method: 'post',
        success: function(serverResponse){
            $('#tran_table').hide();
            $('#deleted_tran').hide();
            $('#added_tran').show();
            $('#added_tran').html(serverResponse);
        }
    })

    $.ajax({
        url: './update/accounts',
        method: 'post',
        success: function(serverResponse){
            $('#account_table').hide();
            $('#deleted_accounts').hide();
            $('#added_accounts').show();
            $('#added_accounts').html(serverResponse);
        }
    })
}

function card_edit(id) {
    $.ajax({
        url: ('./edit/card/'+id),
        method: 'post',
        data: $(this).serialize(),
        success: function(serverResponse){
            reset();
            $('#edit_cards').html(serverResponse);
            if ($('#add_accounts').is(":visible")) {
                $('#add_accounts').slideUp(500,function() {
                    $('#accounts').slideDown(500);
                })
                $('#cards').hide(function(){
                    $('#edit_cards').show();
            })
            } else if ($('#add_transactions').is(":visible")) {
                $('#add_transactions').slideUp(500, function() {
                    $('#transactions').slideDown(500);
                    $('#payment_options').hide()
                    $('#purchase_options').hide()
                    $('#deposit_options').hide()
                    $('#cards').hide(function(){
                        $('#edit_cards').show();
                })
                })
            } else if ($('#edit_accounts').is(":visible")) {
                $('#edit_accounts').slideUp(500, function() {
                    $('#accounts').slideDown(500);
                })
                $('#cards').hide(function(){
                    $('#edit_cards').show();
            })
            } else {
                $('#cards').hide(function(){
                    $('#edit_cards').show(); 
            })
            }
        }
    })
}

function account_edit(id) {
    $.ajax({
        url: ('./edit/account/'+id),
        method: 'post',
        data: $(this).serialize(),
        success: function(serverResponse){
            reset();
            $('#edit_accounts').html(serverResponse);
            if ($('#add_cards').is(":visible")) {
                $('#add_cards').slideUp(500, function() {
                    $('#cards').slideDown(500);
                })
                $('#accounts').slideUp(500, function(){
                    $('#edit_accounts').slideDown(500);
            })
            } else if ($('#add_transactions').is(":visible")) {
                $('#add_transactions').slideUp(500, function() {
                    $('#transactions').slideDown(500);
                    $('#payment_options').hide()
                    $('#purchase_options').hide()
                    $('#deposit_options').hide()
                })
                $('#accounts').slideUp(500, function(){
                    $('#edit_accounts').slideDown(500);
            })
            } else if ($('#edit_cards').is(":visible")) {
                $('#edit_cards').slideUp(500, function() {
                    $('#cards').slideDown(500);
                    // $('#accounts').slideUp(500, function(){
                    //     $('#edit_accounts').slideDown(500);
                    // })
                })
            } else {
                $('#accounts').slideUp(500, function(){
                    $('#edit_accounts').slideDown(500); 
            })
            }
        }
    })
}
function account_del(id) {
    $.ajax({
        url: ('./delete/account/'+id),
        method: 'post',
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#added_accounts').hide()
            $('#account_table').hide()
            $('#deleted_accounts').show()
            $('#deleted_accounts').html(serverResponse);
        }
    })
    $.ajax({
        url: './update/transactions',
        method: 'post',
        success: function(serverResponse){
            $('#tran_table').hide();
            $('#deleted_tran').hide();
            $('#added_tran').show();
            $('#added_tran').html(serverResponse);
        }
    })

    $.ajax({
        url: './update/cards',
        method: 'post',
        success: function(serverResponse){
            $('#card_table').hide();
            $('#deleted_cards').hide();
            $('#added_cards').show();
            $('#added_cards').html(serverResponse);
        }
    })
}

function tran_del(id) {
    $.ajax({
        url: ('./delete/transaction/'+id),
        method: 'post',
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#added_tran').hide()
            $('#tran_table').hide()
            $('#deleted_tran').show()
            $('#deleted_tran').html(serverResponse);
        }
    })
    $.ajax({
        url: './update/cards',
        method: 'post',
        success: function(serverResponse){
            $('#card_table').hide();
            $('#deleted_cards').hide();
            $('#added_cards').show();
            $('#added_cards').html(serverResponse);
        }
    })
    $.ajax({
        url: './update/accounts',
        method: 'post',
        success: function(serverResponse){
            $('#account_table').hide();
            $('#deleted_accounts').hide();
            $('#added_accounts').show();
            $('#added_accounts').html(serverResponse);
        }
    })
}
