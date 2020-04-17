$(document).ready(function ()
{
    var quantity;
    $('.addButton').click(function () {

        quantity =  parseInt( $(this).closest('td').prev('td').text() );
        quantity += 1;
        $(this).closest('td').prev('td').text(quantity);
        

    });
    
});