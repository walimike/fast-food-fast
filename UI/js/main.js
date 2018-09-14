
// defining a function to select different paths depending on user

function SelectUser(){
	if (document.getElementById('radioadmin').checked){
		window.location.href ="adminhome.html";}
  else if (document.getElementById('radiouser').checked){
								window.location.href ="userhome.html";}
}
