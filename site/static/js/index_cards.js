

$(function(){

    
    function isInViewport(card) {
        var elementTop = $(card).offset().top;
        var elementBottom = elementTop + $(card).outerHeight();
        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();
        return elementBottom > viewportTop && elementTop < viewportBottom;
        };


    $(window).scroll(function() {
          $(".card").each(function(){
            if (isInViewport(this)) {
              this.animate({
                "transform":"translateX(0)",
                "opacity":1
                },900)          
              } else {
                this.animate({
                    "transform":"translateX(100%)",
                    "opacity":0
                    },500)    
              };
            });
            this.stop()
        });
    
    });

    