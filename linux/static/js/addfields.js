const addfields = () => {
    let telnum = parseInt($('#add_field_area').find('div.add').length)+1;
	$('div#add_field_area').append(`<div id="add" class="form-group col-md-9 mb-0 add"><label> Name №${telnum}</label><input type="text"  id="val" class="form-control" name="name${telnum}">`);
}