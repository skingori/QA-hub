(function($) {
  'use strict';
  $(function() {

    $('#recent-purchases-listing').DataTable({
      "aLengthMenu": [
        [5, 10, 15, -1],
        [5, 10, 15, "All"]
      ],
      "iDisplayLength": 5,
      "language": {
        search: ""
      },
      searching: true, paging: false, info: false
    });

  });
})(jQuery);

