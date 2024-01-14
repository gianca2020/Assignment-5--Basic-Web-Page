function Nav() {
  var info = "appName: " + navigator.appName +
    "\nproduct: " + navigator.product +
    "\nappVersion: " + navigator.appVersion +
    "\nuserAgent: " + navigator.userAgent +
    "\nplatform: " + navigator.platform +
    "\nlanguage: " + navigator.language;
  document.getElementById("infoText").innerText = info;
}


function Window() {
  var info = "innerHeight: " + window.innerHeight +
    "\ninnerWidth: " + window.innerWidth;
  document.getElementById("infoText").innerText = info;
}


function Screen() {
  var info = "width: " + screen.width +
    "\nheight: " + screen.height +
    "\navailWidth: " + screen.availWidth +
    "\navailHeight: " + screen.availHeight +
    "\ncolorDepth: " + screen.colorDepth +
    "\npixelDepth: " + screen.pixelDepth;
  document.getElementById("infoText").innerText = info;
}


function Location() {
  var info = "href: " + location.href +
    "\nhostname: " + location.hostname +
    "\npathname: " + location.pathname +
    "\nprotocol: " + location.protocol;
  document.getElementById("infoText").innerText = info;
}


function GeoLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var info = "Latitude: " + position.coords.latitude +
        "\nLongitude: " + position.coords.longitude;
      document.getElementById("infoText").innerText = info;
    });
  } else {
    document.getElementById("infoText").innerText = "Geolocation is not supported by this browser.";
  }
}
