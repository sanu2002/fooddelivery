function changeImage(element)
{
  var x = element.getElementsByTagName("img").item(0);
  var v = x.getAttribute("src");
  if(v == ".png")
    v = "feed-orange.png";
  else{
    v = "feed-blue.png";


  }
  x.setAttribute("src", v);
}

<img id="image0" src="feed-blue.png" onclick="changeImage(this);" />