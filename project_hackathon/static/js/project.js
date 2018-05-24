if (typeof DH == 'undefined') { // T = django ataac
  DH = {};
}

DH = function () {

    function editProfileInfo() {
    	$('#profile_form_id').hide();
        $('#edit_profile_btn').on('click', function() {
        	$('#profile_info_id').hide();
        	$('#profile_form_id').show();
        });
    }

    function cancelEditProfile() {
    	$('#cancel_edit_btn_id').on('click', function() {
        	$('#profile_info_id').show();
        	$('#profile_form_id').hide();
        });
    }


    return {
    	editProfileInfo: editProfileInfo,
    	cancelEditProfile: cancelEditProfile
    }
}()

$( function() {
	$( "#id_date_of_birth" ).datepicker({ dateFormat: 'yy-mm-dd' });
	$( "#id_datetime" ).datetimepicker();
} );

