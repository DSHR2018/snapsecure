function login() {
	document.getElementById("login").style.display = "none";
	document.getElementById('input').style.display = "block";
}

var video = document.querySelector("#videoElement");
var mediaStream = HTMLMediaElement.srcObject;

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;

if (navigator.getUserMedia) {       
 navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
 video.src = window.URL.createObjectURL(stream);
 video.play();
 });
}

function videoError() {
	// do something
}