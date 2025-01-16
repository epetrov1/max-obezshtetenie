/*
Author       : Theme-Family
Template Name: Mutakabbir - Law Firm & Lawyer Service Website Template
Version      : 1.0
*/
(function($) {
    "use strict";
	
	
		/*PRELOADER JS*/			
		$(window).on('load', function() { 
			$('#atf-loader').delay(2500).fadeOut(700);
		}); 
		/*END PRELOADER JS*/	
		
		// Header Sticky
		$(window).on('scroll',function() {
            if ($(this).scrollTop() > 30){  
                $('.navbar-area').addClass("atf-sticky-header");
            }
            else{
                $('.navbar-area').removeClass("atf-sticky-header");
            }
        });
		
		 // Mean Menu
		jQuery('.mean-menu').meanmenu({
			meanScreenWidth: "991"
        });

        
		//**================= Sticky =====================**//
  
		  $(window).on('scroll', function() {
			if ($(window).scrollTop() > 50) {
				$('.atf-sticky-header').addClass('atf-nav');
				$('.atf-back-to-top').addClass('open');
			} else {
				$('.atf-sticky-header').removeClass('atf-nav');
				$('.atf-back-to-top').removeClass('open');
			}
		  });
		 
		  
		/*--------------------------------------------------------------
								Scroll UP
		--------------------------------------------------------------*/
			
			$(window).on('scroll', function () { 
				var scrolled = $(window).scrollTop();
				if (scrolled > 400) $('.back-to-top').addClass('active');
				if (scrolled < 400) $('.back-to-top').removeClass('active');
			});
		
			$('.back-to-top').on('click', function () {
				$("html, body").animate({
					scrollTop: "0"
				}, 50);
			});
			
			/*--------------------------------------------------------------
								 // header search js
			--------------------------------------------------------------*/
			 
			  $('.atf-searching-btn').on('click', function(){
				$('.atf-searching-area').addClass('active');
			  });

			  $('.atf-searching-close-btn').on('click', function(){
				$('.atf-searching-area').removeClass('active');
			  });
			/* --------------------------------------------------------
				 Initialize Swiper
			--------------------------------------------------------- */

				var swiper = new Swiper(".mySwiper", {
				  pagination: {
					el: ".swiper-pagination",
					clickable: true,
					renderBullet: function (index, className) {
					  return '<span class="' + className + '">' + (index + 1) + "</span>";
					},
				  },
				  navigation: {
					nextEl: ".swiper-button-next",
					prevEl: ".swiper-button-prev",
				  },
				});
				
			
			
			/* --------------------------------------------------------
				  Odometer JS 
			--------------------------------------------------------- */
			$('.odometer').appear(function() {
				var odo = $(".odometer");
				odo.each(function() {
					var countNumber = $(this).attr("data-count");
					$(this).html(countNumber);
				});
			});
			
			/* --------------------------------------------------------
				    Porfolio isotope
			--------------------------------------------------------- */

				var portfolioIsotope = $('.atf-main-portfolio').isotope({
					itemSelector: '.atf-grid'
				});

				$('#atf-portfolio-flters li').on('click', function() {
					$("#atf-portfolio-flters li").removeClass('filter-active');
					$(this).addClass('filter-active');

					portfolioIsotope.isotope({
						filter: $(this).data('filter')
					});
				});

			/* END Portfolio JS */
			
			
			/* --------------------------------------------------------
				   Testimonial-slider js
			--------------------------------------------------------- */
			  
			  $('.atf_testimonial_slider').slick({
				dots: false,
				infinite: true,
				speed: 300,
				slidesToShow: 1,
				slidesToScroll: 1,
				autoplay: false,
				autoplaySpeed: 5000,
				arrows: true,
				prevArrow: '<button type="button" class="prev"><i class="fa-solid fa-arrow-left"></i></button>',
				nextArrow: '<button type="button" class="next"><i class="fa-solid fa-arrow-right"></i></button>'
			  });
			  
			  
			  /* --------------------------------------------------------
			  Start Service Design Two
			--------------------------------------------------------- */
			$('.atf__service-slider-active').slick({
				arrows: true,
				dots: false,
				infinite: true,
				speed: 300,
				slidesToShow: 4,
				slidesToScroll: 1,
				prevArrow: '<a class="slick-prev"><i class="fas fa-arrow-left" alt="Arrow Icon"></i></a>',
				nextArrow: '<a class="slick-next"><i class="fas fa-arrow-right" alt="Arrow Icon"></i></a>',
				responsive: [
					{
						breakpoint: 1200,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1
						}
					},
					{
						breakpoint: 992,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1
						}
					},
					{
						breakpoint: 768,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1,
							arrows: false,
							dots: true,
						}
					},
					{
						breakpoint: 580,
						settings: {
							arrows: false,
							dots: true,
							slidesToShow: 1,
							slidesToScroll: 1
						}
					}
				]
			});
			
			/* --------------------------------------------------------
			  Start Porfolio Two Design
			--------------------------------------------------------- */
			$('.atf__porfolio-slider-active').slick({
				arrows: true,
				dots: false,
				infinite: true,
				speed: 300,
				slidesToShow: 3,
				slidesToScroll: 1,
				prevArrow: '<a class="slick-prev"><i class="fas fa-arrow-left" alt="Arrow Icon"></i></a>',
				nextArrow: '<a class="slick-next"><i class="fas fa-arrow-right" alt="Arrow Icon"></i></a>',
				responsive: [
					{
						breakpoint: 1200,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1
						}
					},
					{
						breakpoint: 992,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1
						}
					},
					{
						breakpoint: 768,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1,
							arrows: false,
							dots: true,
						}
					},
					{
						breakpoint: 580,
						settings: {
							arrows: false,
							dots: true,
							slidesToShow: 1,
							slidesToScroll: 1
						}
					}
				]
			});
			
			/* --------------------------------------------------------
			  Start Team Design
			--------------------------------------------------------- */
			$('.atf__team-slider-active').slick({
				arrows: true,
				dots: false,
				infinite: true,
				speed: 300,
				slidesToShow: 4,
				slidesToScroll: 1,
				prevArrow: '<a class="slick-prev"><i class="fas fa-arrow-left" alt="Arrow Icon"></i></a>',
				nextArrow: '<a class="slick-next"><i class="fas fa-arrow-right" alt="Arrow Icon"></i></a>',
				responsive: [
					{
						breakpoint: 1200,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1
						}
					},
					{
						breakpoint: 992,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1
						}
					},
					{
						breakpoint: 768,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1,
							arrows: false,
							dots: true,
						}
					},
					{
						breakpoint: 580,
						settings: {
							arrows: false,
							dots: true,
							slidesToShow: 1,
							slidesToScroll: 1
						}
					}
				]
			});

			/*END Team Design*/
			
			/* --------------------------------------------------------
			  Start blog Two Design
			--------------------------------------------------------- */
			$('.atf__blog-slider-active').slick({
				arrows: true,
				dots: false,
				infinite: true,
				speed: 300,
				slidesToShow: 3,
				slidesToScroll: 1,
				prevArrow: '<a class="slick-prev"><i class="fas fa-arrow-left" alt="Arrow Icon"></i></a>',
				nextArrow: '<a class="slick-next"><i class="fas fa-arrow-right" alt="Arrow Icon"></i></a>',
				responsive: [
					{
						breakpoint: 1200,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1
						}
					},
					{
						breakpoint: 992,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1
						}
					},
					{
						breakpoint: 768,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1,
							arrows: false,
							dots: true,
						}
					},
					{
						breakpoint: 580,
						settings: {
							arrows: false,
							dots: true,
							slidesToShow: 1,
							slidesToScroll: 1
						}
					}
				]
			});
			
			
			
			/* --------------------------------------------------------
				   LightCase jQuery Active
			--------------------------------------------------------- */
				$('a[data-rel^=lightcase]').lightcase({
					transition: 'elastic', /* none, fade, fadeInline, elastic, scrollTop, scrollRight, scrollBottom, scrollLeft, scrollHorizontal and scrollVertical */
					swipe: true,
					maxWidth: 1170,
					maxHeight: 600,
				});	  

			/* --------------------------------------------------------
							Mailchamp jQuery Active
			--------------------------------------------------------- */
			$('#mc-form').ajaxChimp({
				url: 'https://themesfamily.us22.list-manage.com/subscribe/post?u=e056d9c3aeb53b20aff997467&amp;id=e307d7e1b8&amp;f_id=0012cee1f0'
				/* Replace Your AjaxChimp Subscription Link */
			}); 
		
		
			/*--------------------------------------------------------------
							WOW SCROLL SPY
		  --------------------------------------------------------------*/	
			 var wow = new WOW({
				  //disabled for mobile
					mobile: false
				});

			wow.init();
		

    
})(jQuery);


