countInterests = 0;
function interests(num){

	if(document.getElementById(num).style.border == ""){
		if (countInterests<2){
			document.getElementById(num).style.border = "2px solid black";
			document.getElementById(num).style.background = "lightgrey";
			countInterests++;
		}
		else{
			document.getElementById("errorMsn").innerHTML="You can only select two images";
			document.getElementById("errorMsn").style.color="red"
		}
	}
	else{
		document.getElementById(num).style.border = ""
		document.getElementById(num).style.background = "white";
		countInterests--;
		if(document.getElementById("errorMsn").innerHTML!=""){
			document.getElementById("errorMsn").innerHTML=""
		}
	}
}
function link(link){
	if (countInterests < 2){
		document.getElementById("errorMsn").innerHTML="You have to select two images";
		document.getElementById("errorMsn").style.color="red"
		return false;
	}
	document.location.href = link
}
