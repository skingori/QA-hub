$( "#sel" )
  .change(function () {
    $( "select option:selected" ).each(function() {
      $("#form").submit();
    });

  });