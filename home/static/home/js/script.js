$(document).ready(function(){
    

function typeWriter(text, i) {
 if (i < (text.length)) {
    $('.landingText').html(text.substring(0, i+1));
    i++;
    setTimeout(function(){
        typeWriter(text, i);
    }, 150);
}
}

typeWriter("Hi, my name is Nichola. I'm a full stack developer", 0);

  
$('#myForm').on('submit', function(e){
  $('#myModal').modal('show');
  e.preventDefault();

 });
  
$('a').mouseenter(function() {
 	$(this).css("color", "#C3AEAF");
 });

$('a').mouseleave(function(){
    $(this).css("color", "#4a4a4f");
});

$(".card").mouseenter(function(){
    $(this).animate({opacity: '1.0'}, "slow");
});

$(".card").mouseleave(function(){
    $(this).animate({opacity: '0.6'}, "slow");
});

$(".resumeButton").mouseenter(function(){
    $(this).css("background-color", "#4a4a4f");
});

$(".resumeButton").mouseleave(function(){
    $(this).css("background-color", "#C3AEAF");
});

$(".imageContainer").hover(function (){
    $('.portfolioImage').attr("src", "./images/scottWebb2.jpeg");
}, function () {
    $('.portfolioImage').attr("src", "./images/ScottWebb.jpeg");
});

$(".imageContainer").onmousestart(function (){
    $('.portfolioImage').attr("src", "./images/scottWebb2.jpeg");
}, function () {
    $('.portfolioImage').attr("src", "./images/ScottWebb.jpeg");
});



});




