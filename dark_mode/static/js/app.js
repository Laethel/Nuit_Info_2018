$(document).foundation();

$(document).ready(function() {
    
    // MAGNIFIER
    var visible = true;

    $('#magnifier').on('click', function() {
        let $middleHead = $('#middle-head');

        if(visible) {
            $middleHead.addClass('hidden');
            visible = false;
        } else {
            $middleHead.removeClass('hidden');
            visible = true;            
        }
    });


    // SEARCH BAR
    $('#searchbar-icon').click(function(){
        $('#searchbar-input').animate({width: 'toggle'});
        $("#searchbar-icon").toggle();
        $("#searchbar-cross").toggle(500);
      });
      
      $('#searchbar-cross').click(function(){
        $('#searchbar-input').animate({width: 'toggle'});
        $("#searchbar-cross").toggle();
        $("#searchbar-icon").toggle(500);
      });
      
    

});