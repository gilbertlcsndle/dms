$(function(){
    datatable_default.dom = '' +
        '<"row"' +
        '   <"col-sm-6"f>' +
        '   <"col-sm-6 text-right add-btn-container">' +
        '>' +
        't' +
        '<"row"'+
        '   <"col-sm-6"i>' +
        '   <"col-sm-6"p>' +
        '>';
    datatable_default.aoColumnDefs = [
        {
            'bSortable': false,
            'aTargets': [0, 5]
        }
    ];
    datatable_default.order = [[1, 'asc']];

    $('#residents').DataTable(datatable_default);

    $('.add-btn-container').html($('.add-btn').html());

    var id_occupation = $("#id_occupation").easyAutocomplete({
        data: [
            'Government',
            'Private',
            'Farming',
            'Fishing',
            'Self-employed',
            'Business',
            'OCW', 
            'Professional',
            'Practice'
        ],
        list: {
            onSelectItemEvent: function() {
                var selectedItemValue = id_occupation.getSelectedItemData();
                
                id_occupation.val(selectedItemValue);
            },
            sort: {
                enabled: true
            }
        }
    });
    
    var id_common_garbage_disposal = $("#id_common_garbage_disposal").easyAutocomplete({
        data: [
            'Dumping/Tambak',
            'Open Pit',
            'Composting',
            'Burning/Burying',
            'Collected'
        ],
        list: {
            onSelectItemEvent: function() {
                var selectedItemValue = id_common_garbage_disposal.getSelectedItemData();
                
                id_common_garbage_disposal.val(selectedItemValue);
            },
            sort: {
                enabled: true
            }
        }
    });

    var id_source_of_water_supply = $("#id_source_of_water_supply").easyAutocomplete({
        data: [
            'Open Dug Well',
            'Springs/Pipe',
            'Artesian wells/Jetmatic pumps',
            'Water works'
        ],
        list: {
            onSelectItemEvent: function() {
                var selectedItemValue = id_source_of_water_supply.getSelectedItemData();
                
                id_source_of_water_supply.val(selectedItemValue);
            },
            sort: {
                enabled: true
            }
        }
    });

    var id_toilet_type = $("#id_toilet_type").easyAutocomplete({
        data: [
            'Flush/Water Sealed',
            'Antipolo',
            'Open pit'
        ],
        list: {
            onSelectItemEvent: function() {
                var selectedItemValue = id_toilet_type.getSelectedItemData();
                
                id_toilet_type.val(selectedItemValue);
            },
            sort: {
                enabled: true
            }
        }
    });

    var id_common_agri_products = $("#id_common_agri_products").easyAutocomplete({
        data: [
            'Rice',
            'Corn',
            'Rootcrops',
            'Vegetable',
            'Fruit',
            'Bearing',
            'Trees'
        ],
        list: {
            onSelectItemEvent: function() {
                var selectedItemValue = id_common_agri_products.getSelectedItemData();
                
                id_common_agri_products.val(selectedItemValue);
            },
            sort: {
                enabled: true
            }
        }
    });

    var id_kinds_of_animals = $("#id_kinds_of_animals").easyAutocomplete({
        data: [
            'Swine',
            'Goat',
            'Chicken',
            'Duck'
        ],
        list: {
            onSelectItemEvent: function() {
                var selectedItemValue = id_kinds_of_animals.getSelectedItemData();
                
                id_kinds_of_animals.val(selectedItemValue);
            },
            sort: {
                enabled: true
            }
        }
    });

    var id_type_of_dwelling_unit = $("#id_type_of_dwelling_unit").easyAutocomplete({
        data: [
            'Concrete',
            'Semi-concrete',
            'Nipa/Bamboo',
            'Wooden',
            'Barong-barong',
            'Galvanize'
        ],
        list: {
            onSelectItemEvent: function() {
                var selectedItemValue = id_type_of_dwelling_unit.getSelectedItemData();
                
                id_type_of_dwelling_unit.val(selectedItemValue);
            },
            sort: {
                enabled: true
            }
        }
    });

    $(
        '#id_gender,' + 
        '#id_educational_attainment,' +
        '#id_status'
    ).addClass('list-inline');

    $('#id_photo').fileinput(bootstrap_fileinput_default);

    $('#id_spouse, #id_civil_status').selectize(selectize_opts);
});