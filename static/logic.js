function classifier() {
  $.get('/classify', function(data) {
    $('#image').html(data);  // update page with new data
  });
};

$('#capture').on('mousedown', function(){
	$.get('/capture');
	});

$('#vehicle').on('mousedown', function(){
	$.get('/vehicle');
	});

$('#text').on('mousedown', function(){
	$.get('/detect');
	});
	

