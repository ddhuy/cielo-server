var SERVER_ID = get_param_by_name('ServerId');

function add_dev_row ( container, type, serial, capaciy, speed, slot, vendor, revision ) {
    var tr = container.find('tbody tr:last');
    var cloned_tr = tr.clone();
    cloned_tr.find('input.field-type').val(type);
    cloned_tr.find('input.field-serial').val(serial);
    cloned_tr.find('input.field-capacity').val(capacity);
    cloned_tr.find('input.field-speed').val(speed);
    cloned_tr.find('input.field-slot').val(slot);
    cloned_tr.find('input.field-vendor').val(vendor);
    cloned_tr.find('input.field-revision').val(revision);
    cloned_tr.addClass('data-field-row');
    cloned_tr.removeAttr('style');
    tr.before(cloned_tr);
    return cloned_tr;
}

function add_row ( container, key, val ) {
    var tr = container.find('tbody tr:last');
    var cloned_tr = tr.clone();
    cloned_tr.find('input.field-key').val(key);
    cloned_tr.find('input.field-val').val(val);
    cloned_tr.addClass('data-field-row');
    cloned_tr.removeAttr('style');
    tr.before(cloned_tr);
    return cloned_tr;
}

function display_board_data ( board_data ) {
    $('#id_Serial').val(board_data['Serial']);
    $('#id_Status').val(board_data['Status']);
    $('.id_Owner').val(board_data['User']);
    $('#id_IPMI').val(board_data['IpmiPort']);
    // public
    var public_info = board_data['Public'] || board_data['Info'];
    if (public_info) {
        var hw_data = public_info['Hardware'];
        for (var k in hw_data) {
            add_row($('#id_TabHardware'), k, hw_data[k]);
        }
        var sw_data = public_info['Software'];
        for (var k in sw_data) {
            add_row($('#id_TabSoftware'), k, sw_data[k]);
        }
    }
    // private
    var private_info = board_data['Private'];
    if (private_info) {
        var bmc_data = private_info['BMC'];
        for (var k in bmc_data) {
            add_row($('#id_TabBMC'), k, bmc_data[k]);
        }
        var power_data = private_info['Power'];
        for (var k in power_data) {
            add_row($('#id_TabPower'), k, power_data[k]);
        }
    }
    // devices
    var dev_info = board_data['Devices'];
    if (dev_info) {
        for (var dev in dev_info) {
            add_dev_row($('#id_TabDevices'),
                        dev['Type'], dev['Serial'], dev['Capacity'], dev['Speed'],
                        dev['Slot'], dev['Vendor'], dev['Revision']);
        }
    }
    // note
    var note_info = board_data['Note'];
    if (note_info) {
        for (var k in note_info) {
            add_row($('#id_TabNote'), k, note_info[k]);
        }
    }
}

function parse_board_data ( ) {
    var bmc_data = {};
    $('#id_TabBMC tbody tr.data-field-row').map(function() {
        var key = $(this).find('input.field-key').val();
        var val = $(this).find('input.field-val').val();
        bmc_data[key] = val;
        return bmc_data;
    });

    var power_data = {};
    $('#id_TabPower tbody tr.data-field-row').map(function() {
        var key = $(this).find('input.field-key').val();
        var val = $(this).find('input.field-val').val();
        power_data[key] = val;
        return power_data;
    });

    var hardware_data = {};
    $('#id_TabHardware tbody tr.data-field-row').map(function() {
        var key = $(this).find('input.field-key').val();
        var val = $(this).find('input.field-val').val();
        hardware_data[key] = val;
        return hardware_data;
    });

    var software_data = {};
    $('#id_TabSoftware tbody tr.data-field-row').map(function() {
        var key = $(this).find('input.field-key').val();
        var val = $(this).find('input.field-val').val();
        software_data[key] = val;
        return software_data;
    });

    var dev_info = [];
    $('#id_TabDevices tbody tr.data-field-row').map(function() {
        var type = $(this).find('input.field-type').val();
        var serial = $(this).find('input.field-serial').val();
        var capacity = $(this).find('input.field-capacity').val();
        var speed = $(this).find('input.field-speed').val();
        var slot = $(this).find('input.field-slot').val();
        var vendor = $(this).find('input.field-vendor').val();
        var revision = $(this).find('input.field-revision').val();
        dev_info.push({
            'Type' : type,
            'Serial' : serial,
            'Capacity' : capacity,
            'Speed' : speed,
            'Slot' : slot,
            'Vendor' : vendor,
            'Revision' : revision
        });
        return dev_info[dev_info.length - 1];
    });

    var note_info = {};
    $('#id_TabNote tbody tr.data-field-row').map(function() {
        var key = $(this).find('input.field-key').val();
        var val = $(this).find('input.field-val').val();
        note_info[key] = val;
        return note_info;
    });

    var board_data = {};
    board_data['Serial'] = $('#id_Serial').val();
    board_data['Status'] = $('#id_Status').val();
    board_data['User'] = $('.id_Owner').first().val();
    board_data['Private'] = {'BMC': bmc_data, 'Power': power_data};
    board_data['Info'] = {'Hardware': hardware_data, 'Software': software_data};
    board_data['Note'] = note_info;
    board_data['Devices'] = dev_info;
    return board_data;
}

function clean_display ( ) {
    $('#id_TabHardware tbody').find('tr.data-field-row').remove();
    $('#id_TabSoftware tbody').find('tr.data-field-row').remove();
    $('#id_TabBMC tbody').find('tr.data-field-row').remove();
    $('#id_TabPower tbody').find('tr.data-field-row').remove();
    $('#id_TabNote tbody').find('tr.data-field-row').remove();
    $('#id_TabDevices tbody').find('tr.data-field-row').remove();
}

$(document).ready(function() {
    enable_all_qtips();
});

function show_board_dialog ( title, action, serial, board_data ) {
    $('#id_BoardTabs').tabs({});
    // setTheme('bootstrap2', 'fontawesome4');
    var board_dialog = $('#id_BoardDialog').dialog({
        width: '750',
        height: '700',
        title: title,
        resizable: false,
        closeOnEscape: false,
        buttons: {
            'OK': function() {
                if (!$('#id_Serial').val()) {
                    cielo_dialog('Board Serial is not valid');
                    return;
                }
                var board_data = parse_board_data();
                commit_json_data(
                    URL = '/dashboard/',
                    Data = {
                        Action: action,
                        ServerId: SERVER_ID,
                        Serial: serial,
                        Data: JSON.stringify(board_data)
                    },
                    Param = {},
                    OnSuccessCallback = function ( json_resp, Param ) {
                        location.reload(true);
                    },
                    OnErrorCallback = function ( json_resp, Param ) {
                        cielo_dialog(json_resp.Data);
                    }
                );
                $(this).dialog('close');
            },
            'Cancel': function() {
                $(this).dialog('close');
            }
        },
        open: function() {
            // if (board_data) {
            //     display_board_data(board_data);
            // }
            if (serial) {
                $(this).data('BOARD_SERIAL', serial);
            }
        },
        close: function() {
            // clean_display();
        }
    });
    board_dialog.dialog('open');
}

$(document).on('click', '.new-board', function() {
    var board_row = $(this).parents('.board-row');
    $.ajax({
        type     : 'GET',
        url      : '/board/insert',
        cache    : false,
        success: function ( response ) {
            var div_board = document.getElementById('id_BoardDialog');
            div_board.innerHTML = response;
            show_board_dialog('Install New Board', 'InsertBoard', null, null);
        },
        error: function ( response ) {
            cielo_dialog(response);
        }
    });
});

$(document).on('click', '.edit-board', function() {
    var serial = $(this).parents('.board-row').attr('data-board-serial');
    $.ajax({
        type     : 'GET',
        url      : '/board/update/?ServerId=' + SERVER_ID + '&Serial=' + serial,
        cache    : false,
        success: function ( response ) {
            var div_board = document.getElementById('id_BoardDialog');
            div_board.innerHTML = response;
            show_board_dialog('Update board', 'UpdateBoard', serial, null);
        },
        error: function ( response ) {
            cielo_dialog(response);
        }
    });
});

$(document).on('click', '.deactivate-board', function() {
    var board_row = $(this).parents('.board-row');
    var Serial = board_row.attr('data-board-serial');
    cielo_confirm_dialog(
        Title = 'Delete Board',
        Message = 'Are you sure want to de-activate this board?',
        YesFn = function() {
            commit_json_data(
                URL = '/dashboard/',
                Data = {
                    Action: 'DeactivateBoard',
                    ServerId: SERVER_ID,
                    Serial: Serial
                },
                Param = {},
                OnSuccessCallback = function ( json_resp, Param ) {
                    location.reload(true);
                },
                OnErrorCallback = function ( json_resp, Param ) {
                    cielo_dialog(json_resp.Data);
                }
            );
        },
        NoFn = function() {
        }
    );
});

$(document).on('click', '.activate-board', function() {
    var board_row = $(this).parents('.board-row');
    var Serial = board_row.attr('data-board-serial');
    cielo_confirm_dialog(
        Title = 'Delete Board',
        Message = 'Are you sure want to activate this board?',
        YesFn = function() {
            commit_json_data(
                URL = '/dashboard/',
                Data = {
                    Action: 'ActivateBoard',
                    ServerId: SERVER_ID,
                    Serial: Serial
                },
                Param = {},
                OnSuccessCallback = function ( json_resp, Param ) {
                    location.reload(true);
                },
                OnErrorCallback = function ( json_resp, Param ) {
                    cielo_dialog(json_resp.Data);
                }
            );
        },
        NoFn = function() {
        }
    );
});

$(document).on('click', '.new-field', function() {
    add_row($(this).closest('table'));
    // var $tr = $(this).closest('table').find('tbody tr:last');
    // var $clone = $tr.clone();
    // $clone.find(':text').val('');
    // $clone.removeAttr('style');
    // $tr.after($clone);
});

$(document).on('click', '.delete-field', function() {
    $(this).closest('tr').remove();
});

$(document).on('click', '.btn-release', function() {
    var serial = $('#id_BoardDialog').data('BOARD_SERIAL');
    commit_json_data(
        URL = '/dashboard/',
        Data = {
            Action: 'ReleaseBoard',
            ServerId: SERVER_ID,
            Serial: serial
        },
        Param = {},
        OnSuccessCallback = function ( json_resp, Param ) {
            var board_data = json_resp;
            $("#id_IPMI").val("");
            $(".id_Owner").val("");
        },
        OnErrorCallback = function ( json_resp, Param ) {
            cielo_dialog(json_resp.Data);
        }
    );
});

$(document).on('click', '.btn-request', function() {
    var serial = $('#id_BoardDialog').data('BOARD_SERIAL');
    commit_json_data(
        URL = '/dashboard/',
        Data = {
            Action: 'RequestBoard',
            ServerId: SERVER_ID,
            Serial: serial
        },
        Param = {},
        OnSuccessCallback = function ( json_resp, Param ) {
            var board_data = json_resp.Data[0];
            $("#id_IPMI").val(board_data.Port);
            $(".id_Owner").val(board_data.Username);
        },
        OnErrorCallback = function ( json_resp, Param ) {
            cielo_dialog(json_resp.Data);
        }
    );
});
