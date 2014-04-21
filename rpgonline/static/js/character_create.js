var user_id = "";
var name = "";
var combat_notes = "";
var ability_list = new Array();
var weaknesses_list = new Array();
var attack_list = new Array();

var perks_list = new Array();
var flaws_list = new Array();

var defense = "";
var health = "";
var endurance = "";
var tv = "";
var background = "";
var appearance = "";
var personality = "";
var other_notes = "";
var portrait_url = "";
var icon_url = "";

$(document).ready(function() {
    $.getJSON( '/all_abilities_json', { name: "{{ session['username'] }}" }, function( data ) {
        $('#abilitiesname_select').find('option').remove();
        $.each(data, function(index, field) {
            $('#abilitiesname_select').append($("<option></option>").attr('value', field.id).text(field.name));
        });
        //console.log(JSON.stringify(data));
    });
    
    $.getJSON( '/all_weaknesses_json', { name: "{{ session['username'] }}" }, function( data ) {
        $('#weaknessesname_select').find('option').remove();
        $.each(data, function(index, field) {
            $('#weaknessesname_select').append($("<option></option>").attr('value', field.id).text(field.name));
        });
        //console.log(JSON.stringify(data));
    });
    
    $.getJSON( '/all_perks_json', { name: "{{ session['username'] }}" }, function( data ) {
        $('#perkname_select').find('option').remove();
        $.each(data, function(index, field) {
            $('#perkname_select').append($("<option></option>").attr('value', field.id).text(field.name));
        });
        //console.log(JSON.stringify(data));
    });

    $.getJSON( '/all_flaws_json', { name: "{{ session['username'] }}" }, function( data ) {
        $('#flawname_select').find('option').remove();
        $.each(data, function(index, field) {
            $('#flawname_select').append($("<option></option>").attr('value', field.id).text(field.name));
        });
        //console.log(JSON.stringify(data));
    });

    $("#abilities_btn").on("click", add_to_ability_table);
    $("#weaknesses_btn").on("click", add_to_weakness_table);
    $("#perkadd_btn").on("click", add_to_perk_table(perks_list, flaws_list));
    $("#flawadd_btn").on("click", add_to_flaw_table);
    $("#attackadd_btn").on("click", add_to_attack_table);
});

function add_to_ability_table() {
    var s_ability_id = $('#abilitiesname_select').children(':selected').attr('value');
    var s_ability_name = $('#abilitiesname_select').children(':selected').text();
    var s_ability_value = $('#abilitiesvalue_select').children(':selected').text();
    var s_ability_note = $('#abilitiesnote_text').val();
    
    var ability = [s_ability_id, s_ability_name, s_ability_value, s_ability_note];
    
    ability_list.push(ability);
    
    update_ability_table();
    
    //for (var i=0;i<ability.length;i++) {
    //    console.log(ability[i])
    //}
    
    //console.log(s_ability_id);
    //console.log(s_ability_name);
    //console.log(s_ability_value);
    //console.log(s_ability_note);
}

function update_ability_table() {
    $("#abilities_table tr").remove();
    
    var table_obj = $('#abilities_table tbody');
    
    var table_row = $('<tr>', {id: "a_header"});
    var table_c_name = $('<th>', {html: 'Name'});
    var table_c_value = $('<th>', {html: 'Value'});
    var table_c_note = $('<th>', {html: 'Note'});
    
    table_row.append(table_c_name);
    table_row.append(table_c_value);
    table_row.append(table_c_note);
    
    table_obj.append(table_row);
    
    for (var i=0;i<ability_list.length;i++) {
        var table_row = $('<tr>', {id: ability_list[i][0]});
        var table_c_name = $('<td>', {html: ability_list[i][1]});
        var table_c_value = $('<td>', {html: ability_list[i][2]});
        var table_c_note = $('<td>', {html: ability_list[i][3]});
        
        table_row.append(table_c_name);
        table_row.append(table_c_value);
        table_row.append(table_c_note);
        
        table_obj.append(table_row);
    }
}

function add_to_weakness_table() {
    var s_weaknesses_id = $('#weaknessesname_select').children(':selected').attr('value');
    var s_weaknesses_name = $('#weaknessesname_select').children(':selected').text();
    var s_weaknesses_value = $('#weaknessesvalue_select').children(':selected').text();
    var s_weaknesses_note = $('#weaknessesnote_text').val();
    
    var weakness = [s_weaknesses_id, s_weaknesses_name, s_weaknesses_value, s_weaknesses_note];
    
    weaknesses_list.push(weakness);
    
    update_weakness_table();
}

function update_weakness_table() {
    $("#weaknesses_table tr").remove();
    
    var table_obj = $('#weaknesses_table tbody');
    
    var table_row = $('<tr>', {id: "w_header"});
    var table_c_name = $('<th>', {html: 'Name'});
    var table_c_value = $('<th>', {html: 'Value'});
    var table_c_note = $('<th>', {html: 'Note'});
    
    table_row.append(table_c_name);
    table_row.append(table_c_value);
    table_row.append(table_c_note);
    
    table_obj.append(table_row);
    
    for (var i=0;i<weaknesses_list.length;i++) {
        var table_row = $('<tr>', {id: weaknesses_list[i][0]});
        var table_c_name = $('<td>', {html: weaknesses_list[i][1]});
        var table_c_value = $('<td>', {html: weaknesses_list[i][2]});
        var table_c_note = $('<td>', {html: weaknesses_list[i][3]});
        
        table_row.append(table_c_name);
        table_row.append(table_c_value);
        table_row.append(table_c_note);
        
        table_obj.append(table_row);
    }
}

function add_to_perk_table() {
    var s_perk_id = $('#perkname_select').children(':selected').attr('value');
    var s_perk_name = $('#perkname_select').children(':selected').text();
    var s_perk_value = $('#perkmultiplier_select').children(':selected').text();
    var s_perk_note = $('#perknote_text').val();
    
    var perk = [s_perk_id, s_perk_name, s_perk_value, s_perk_note];
    
    perks_list.push(perk);
    
    update_perk_table();
}

function update_perk_table() {
    $("#perkselect_table tr").remove();
    
    var table_obj = $('#perkselect_table tbody');
    
    var table_row = $('<tr>', {id: "w_header"});
    var table_c_name = $('<th>', {html: 'Perk Name'});
    var table_c_value = $('<th>', {html: 'Mult'});
    var table_c_note = $('<th>', {html: 'Note'});
    
    table_row.append(table_c_name);
    table_row.append(table_c_value);
    table_row.append(table_c_note);
    
    table_obj.append(table_row);
    
    for (var i=0;i<perks_list.length;i++) {
        var table_row = $('<tr>', {id: perks_list[i][0]});
        var table_c_name = $('<td>', {html: perks_list[i][1]});
        var table_c_value = $('<td>', {html: perks_list[i][2]});
        var table_c_note = $('<td>', {html: perks_list[i][3]});
        
        table_row.append(table_c_name);
        table_row.append(table_c_value);
        table_row.append(table_c_note);
        
        table_obj.append(table_row);
    }
}

function add_to_flaw_table() {
    var s_flaw_id = $('#flawname_select').children(':selected').attr('value');
    var s_flaw_name = $('#flawname_select').children(':selected').text();
    var s_flaw_value = $('#flawmultiplier_select').children(':selected').text();
    var s_flaw_note = $('#flawnote_text').val();
    
    var flaw = [s_flaw_id, s_flaw_name, s_flaw_value, s_flaw_note];
    
    flaws_list.push(flaw);
    
    update_flaw_table();
}

function update_flaw_table() {
    $("#flawselect_table tr").remove();
    
    var table_obj = $('#flawselect_table tbody');
    
    var table_row = $('<tr>', {id: "w_header"});
    var table_c_name = $('<th>', {html: 'Flaw Name'});
    var table_c_value = $('<th>', {html: 'Mult'});
    var table_c_note = $('<th>', {html: 'Note'});
    
    table_row.append(table_c_name);
    table_row.append(table_c_value);
    table_row.append(table_c_note);
    
    table_obj.append(table_row);
    
    for (var i=0;i<flaws_list.length;i++) {
        var table_row = $('<tr>', {id: flaws_list[i][0]});
        var table_c_name = $('<td>', {html: flaws_list[i][1]});
        var table_c_value = $('<td>', {html: flaws_list[i][2]});
        var table_c_note = $('<td>', {html: flaws_list[i][3]});
        
        table_row.append(table_c_name);
        table_row.append(table_c_value);
        table_row.append(table_c_note);
        
        table_obj.append(table_row);
    }
}

function add_to_attack_table(ol, fl) {
    var s_attack_name = $('#attackname_text').val();
    var s_attack_roll = $('#attackroll_text').val();
    var s_attack_dx = $('#attackdx_text').val();
    var s_attack_cost = $('#attackcost_text').val();
    var s_attack_note = $('#attacknote_text').val();
    
    var attack = [s_attack_name, ol, fl, s_attack_roll, s_attack_dx, s_attack_cost, s_attack_note];
    
    attack_list.push(attack);
    
    update_attack_table();
    flaws_list.length = new Array();
    perks_list.length = new Array();
    update_flaw_table();
    update_perk_table();
}

function update_attack_table() {
    $("#combatstats_table tr").remove();
    
    // Header
    var table_obj = $('#combatstats_table tbody');
    
    var table_row = $('<tr>', {id: "w_header"});
    var table_c_name = $('<th>', {html: 'Name'});
    var table_c_perks = $('<th>', {html: 'Perks'});
    var table_c_flaws = $('<th>', {html: 'Flaws'});
    var table_c_roll = $('<th>', {html: 'Roll'});
    var table_c_dx = $('<th>', {html: 'DX'});
    var table_c_cost = $('<th>', {html: 'Cost'});
    var table_c_note = $('<th>', {html: 'Note'});
    
    table_row.append(table_c_name);
    table_row.append(table_c_perks);
    table_row.append(table_c_flaws);
    table_row.append(table_c_roll);
    table_row.append(table_c_dx);
    table_row.append(table_c_cost);
    table_row.append(table_c_note);
    
    table_obj.append(table_row);
    
    for (var i=0;i<attack_list.length;i++) {
        var table_row = $('<tr>', {id: attack_list[i][0]});
        var table_c_name = $('<td>', {html: attack_list[i][0]});
        console.log(i);
        var temp_perks = "";
        for (var p=0;p<attack_list[i][1].length;p++) {
            console.log(attack_list[i][1][p][1]);
            temp_perks += attack_list[i][1][p][1] + " ";
        }
        
        var temp_flaws = "";
        for (var f=0;f<attack_list[i][2].length;f++) {
            temp_flaws += attack_list[i][2][f][1] + " " + attack_list[i][2][f][2];
            if (f+1<attack_list[i][2].length) {
                temp_flaws += ", "
            }
        }
        
        var table_c_perks = $('<td>', {html: temp_perks});
        var table_c_flaws = $('<td>', {html: temp_flaws});
        var table_c_roll = $('<td>', {html: attack_list[i][3]});
        var table_c_dx = $('<td>', {html: attack_list[i][4]});
        var table_c_cost = $('<td>', {html: attack_list[i][5]});
        var table_c_note = $('<td>', {html: attack_list[i][6]});
        
        table_row.append(table_c_name);
        table_row.append(table_c_perks);
        table_row.append(table_c_flaws);
        table_row.append(table_c_roll);
        table_row.append(table_c_dx);
        table_row.append(table_c_cost);
        table_row.append(table_c_note);
        
        table_obj.append(table_row);
    }
}

function add__new_character() {
    
}