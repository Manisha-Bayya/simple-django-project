var $DOM = $(document);

$DOM.on('click', '#send_otp', function() {

	console.log("send otp clicked");
    data = {}
    data["email"] = $(".email").val();

	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: '/login/send_otp',
		success: function(result) {
            console.log(result);
		}
	});
});

$DOM.on('click', '#login_submit', function() {

	console.log("login clicked");
    data = {}
    data["email"] = $(".email").val();
    data["otp"] = $(".otp").val()

	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: '/login/validate',
		success: function(result) {
            if (result.success) {
                window.location.href = "/";
            }
            else {
                alertify.set('notifier', 'position', 'top-right');
                alertify.error(result.message);
            }
		}
	});
});
