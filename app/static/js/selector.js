$( window ).load( function () {
	var $table = $( '.table' ).isotope( {
		itemSelector: '.table-item',
	} );

	$( '.filter-button-group' ).on( 'click', 'a', function () {

		$( '.filter-button-group a' ).removeClass( "current" );
		$( this ).addClass( "current" );

		var filterValue = $( this ).attr( 'data-filter' );
		$table.isotope( {
			filter: filterValue
		} );
		setTimeout( function () {

		}, 0 );

		return false;

	} );

  // delete main-preloader
	var mainPreloader = document.querySelector('.main-preloader');
	if( mainPreloader ) {
		mainPreloader.classList.add('window-is-loaded');
		setTimeout(function(){
				mainPreloader.parentNode.removeChild( mainPreloader );
		},650);
	}
	// /delete main-preloader

} );