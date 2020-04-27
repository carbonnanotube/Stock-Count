$(document).ready(function ()
{
    // JS only search of table to search for products 

    $('#result_message').hide();
   


    $("#searchId").on("keyup", function () {
        var value = $(this).val().toLowerCase();


        if (value === "") {
            $('table').show();
        }

        

            $("#product_table tr").each(function () {
                $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
        
        if ($("#product_table tr:visible").length == 0) {
            $('#result_message').show();
            $('table').hide();
        }
        else if ($("#product_table tr:visible").length > 0) {
            $('#result_message').hide();
            $('table').show();
        }
       

    });

     

   
    
    
});


/*class Transactions(models.Model):
    foodName = models.CharField(max_length = 200)
    quantity = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)


    def __str__(self):
        return self.foodName
 * 
 * 
 */