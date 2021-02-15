$(document).ready(function(){
  console.log("script running")
    $(".row-1").mouseenter(function(){
      $(".box-1").css({
        "transform":"scale(1.1)",
        "transition":"transform .4s",
        "z-index":"1"
      });
    });

    $(".row-1").mouseleave(function(){
        $(".box-1").css({
            "transform":"scale(1)",
            "transition":"transform .4s"
          });
      });


      $(".row-2").mouseenter(function(){
        $(".box-2").css({
          "transform":"scale(1.1)",
          "transition":"transform .4s",
          "z-index":"1"
        });
      });
  
      $(".row-2").mouseleave(function(){
          $(".box-2").css({
              "transform":"scale(1)",
              "transition":"transform .4s"
            });
        });

        
        $(".row-3").mouseenter(function(){
            $(".box-3").css({
              "transform":"scale(1.1)",
              "transition":"transform .4s",
              "z-index":"1"
            });
          });
      
          $(".row-3").mouseleave(function(){
              $(".box-3").css({
                  "transform":"scale(1)",
                  "transition":"transform .4s"
                });
            });
      
      


      
  });





$(document).ready(function(){
  $("#showHide").click(function(){
    $(".timeline-area").toggle();
  });
});


$(document).ready(function(){
  $("#scan").click(function(){
    var bla = $("#url").val();
    console.log(bla)
    $("#scan").append("<img class='rotating' src='https://img.icons8.com/carbon-copy/2x/loading.png' width='20'>")
    $("#scanText").hide();
  });
});

