$('#category-add-toggle').click( function() {
	$(this).parents('div:first').toggleClass( 'wp-hidden-children' );
	$('#category-tabs a[href="#categories-all"]').click();
	$('#newcategory').focus();
	return false;
} );     