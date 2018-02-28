document.addEventListener("DOMContentLoaded",function() {
  var amzBtn = document.getElementById("amazon-btn");
  var appBtn = document.getElementById("apple-btn");
  var nfxBtn = document.getElementById("netflix-btn");
  var tslBtn = document.getElementById("tesla-btn");
  amzBtn.addEventListener("click",function(){displayP('amazon-ml')});
  appBtn.addEventListener("click",function(){displayP("apple-ml")});
  nfxBtn.addEventListener("click",function(){displayP("netflix-ml")});  
  tslBtn.addEventListener("click",function(){displayP("tesla-ml")});

});

function displayP(ml) {
  var container = document.getElementById("madlib-div");
  var elem = document.getElementById(ml);
  for( var i = 0; i < container.children.length; i++)  {
    container.children[i].style.display = 'none';
  }
  elem.style.display = 'block';
}
