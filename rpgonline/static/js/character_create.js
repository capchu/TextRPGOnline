var ability_list = [];
var weaknesses_list = [];
var attack_list = [];

var perks_list = [];
var flaws_list = [];

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
    });
    
    $.getJSON( '/all_perks_json', { name: "{{ session['username'] }}" }, function( data ) {
        $('#perkname_select').find('option').remove();
        $.each(data, function(index, field) {
            $('#perkname_select').append($("<option></option>").attr('value', field.id).text(field.name));
        });
    });

    $.getJSON( '/all_flaws_json', { name: "{{ session['username'] }}" }, function( data ) {
        $('#flawname_select').find('option').remove();
        $.each(data, function(index, field) {
            $('#flawname_select').append($("<option></option>").attr('value', field.id).text(field.name));
        });
    });

    $("#abilities_btn").on("click", add_to_ability_table);
    $("#weaknesses_btn").on("click", add_to_weakness_table);
    $("#perkadd_btn").on("click", add_to_perk_table);
    $("#flawadd_btn").on("click", add_to_flaw_table);
    $("#attackadd_btn").on("click", add_to_attack_table);   
    $("#submit_btn").on("click", add__new_character);
});

function add_to_ability_table() {
    var s_ability_id = $('#abilitiesname_select').children(':selected').attr('value');
    var s_ability_name = $('#abilitiesname_select').children(':selected').text();
    var s_ability_value = $('#abilitiesvalue_select').children(':selected').text();
    var s_ability_note = $('#abilitiesnote_text').val();
    
    var ability = [s_ability_id, s_ability_name, s_ability_value, s_ability_note];
    
    ability_list.push(ability);
    
    update_ability_table();
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

function add_to_attack_table() {
    var s_attack_name = $('#attackname_text').val();
    var s_attack_roll = $('#attackroll_text').val();
    var s_attack_dx = $('#attackdx_text').val();
    var s_attack_cost = $('#attackcost_text').val();
    var s_attack_note = $('#attacknote_text').val();
    
    var pl = perks_list.slice();
    var fl = flaws_list.slice();
    
    var attack = [s_attack_name, pl, fl, s_attack_roll, s_attack_dx, s_attack_cost, s_attack_note];
    
    attack_list.push(attack);
    
    update_attack_table();
    flaws_list.length = 0;
    perks_list.length = 0;
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
            temp_perks += attack_list[i][1][p][1] + " " + attack_list[i][1][p][2];
            if (p+1<attack_list[i][1].length) {
                temp_perks += ", "
            }
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
    var character_obj = {
        user_id: "",
        name: "",
        combat_notes: "",
        ability_list: [],
        weakness_list: [],
        attack_list: [],
        defense: "",
        health: "",
        endurance: "",
        tv: "",
        background: "",
        appearance: "",
        personality: "",
        other_notes: "",
        portrait_url: "",
        icon_url: ""
    };
    
    for (var i=0;i<ability_list.length;i++) {
        var ability_obj = {
            id: "",
            name: "",
            value: "",
            note: "",
        };
        ability_obj.id = ability_list[i][0];
        ability_obj.name = ability_list[i][1];
        ability_obj.value = ability_list[i][2];
        ability_obj.note = ability_list[i][3];
        character_obj['ability_list'].push(ability_obj);
    }
    
    for (var i=0;i<weaknesses_list.length;i++) {
        var weakness_obj = {
            id: "",
            name: "",
            value: "",
            note: "",
        };
        weakness_obj.id = weaknesses_list[i][0];
        weakness_obj.name = weaknesses_list[i][1];
        weakness_obj.value = weaknesses_list[i][2];
        weakness_obj.note = weaknesses_list[i][3];
        character_obj['weakness_list'].push(weakness_obj);
    }
    
    for (var i=0;i<attack_list.length;i++) {
        var attack_obj = {
            name: "",
            perks: [],
            flaws: [],
            roll: "",
            dx: "",
            end: "",
            note: "",
        };
        
        for (var p=0;p<attack_list[i][1].length;p++) {
            var perk_obj = {
                perk_id: "",
                name: "",
                multiplier: "",
                note: ""
            }
            perk_obj.perk_id = attack_list[i][1][p][0];
            perk_obj.name = attack_list[i][1][p][1];
            perk_obj.multiplier = attack_list[i][1][p][2];
            perk_obj.note = attack_list[i][1][p][3];
            attack_obj['perks'].push(perk_obj);
        }
        
        for (var f=0;f<attack_list[i][2].length;f++) {
            var flaw_obj = {
                flaw_id: "",
                name: "",
                multiplier: "",
                note: ""
            }
            flaw_obj.flaw_id = attack_list[i][2][f][0];
            flaw_obj.name = attack_list[i][2][f][1];
            flaw_obj.multiplier = attack_list[i][2][f][2];
            flaw_obj.note = attack_list[i][2][f][3];
            attack_obj['flaws'].push(flaw_obj);
        }
        
        attack_obj['name'] = attack_list[i][0];
        attack_obj['roll'] = attack_list[i][3];
        attack_obj['dx'] = attack_list[i][4];
        attack_obj['end'] = attack_list[i][5];
        attack_obj['note'] = attack_list[i][6];
        character_obj['attack_list'].push(attack_obj);
    }
    
    character_obj["user_id"] = $('#username').text();
    character_obj["name"] = $('#name_text').val();
    character_obj["combat_notes"] = $('#combatnotes_text').val();
    character_obj["defense"] = $('#statsdefense_text').val();
    character_obj["health"] = $('#statshealth_text').val();
    character_obj["endurance"] = $('#statsedurance_text').val();
    character_obj["tv"] = $('#statstv_text').val();
    character_obj["background"] = $('#background_text').val();
    character_obj["appearance"] = $('#appearance_text').val();
    character_obj["personality"] = $('#personality_text').val();
    character_obj["other_notes"] = $('#othernotes_text').val();
    character_obj["portrait_url"] = $('#portraiturl_text').val();
    character_obj["icon_url"] = $('#portraiturl_text').val();
    console.log(JSON.stringify(character_obj, null, 2));
    //var json = JSON.parse(character_obj);

    $.ajax({
        type: "POST",
        contentType: "application/json",
        url: "/character_submit",
        data: JSON.parse(JSON.stringify(character_obj)),
        sucess: function(data, status) {
            alert("Data: " + data + "\nStatus: " + status);
            },
        dataType: "json"
    });
}