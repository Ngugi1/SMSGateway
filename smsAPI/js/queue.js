(function() { 
	root = window || this;
	
	$('#addtoqueue').click(function (e) {
		var o = new Option($('#destination_number').val(), $('#destination_number').val());
		$("#destination_numbers").append(o);
      });
}).call(this);