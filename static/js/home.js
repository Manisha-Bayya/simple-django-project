var $DOM = $(document);
$DOM.on('click', '#search_submit', function() {

	console.log("search clicked");

    query = $(".search").val();
    $('.search_results').empty()
	$.ajax({
		type: 'get',
		url: '/search?query=' + query,
		success: function(result) {
            console.log(result);
            $('.search_results').append(result)
		}
	});
});

