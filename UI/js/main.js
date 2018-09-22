
// defining a function to select different paths depending on user

function SelectUser(){
	if (document.getElementById('radioadmin').checked){
		window.location.href ="adminhome.html";}
  else if (document.getElementById('radiouser').checked){
								window.location.href ="userhome.html";}
}

// function for adding items to Cart

function addToCart() {
    // clear selection table first
    var selection = document.getElementsByTagName("table")[1].getElementsByTagName("tbody")[0];
    selection.innerHTML = "";

    // loop through items
    var items = document.getElementsByTagName("tr");
    for (var i = 0; i < items.length; i++) {
      var input = items[i].getElementsByTagName("input");
      if (!input.length) continue;
      if (!input[0].checked) continue;
      var item =  items[i].getElementsByTagName("td")[0].innerHTML;
      // append element to selection
      selection.innerHTML = selection.innerHTML + "<p>" + item;
    }
  }

// Alert message for recieved Order

	function makeOrder() {
	    alert("Order has been recieved!");
	}

// clears div for new activity

	function clearDiv() {
    document.getElementById("selecteditems").innerHTML = "";
}

//admin declines Order

function refreshPage(){
	location.reload();
}

// Alert message for marking order as complete

	function markOrder() {
	    alert("The order has been marked as complete!");
	}

	// Alert message for adding items to food list

		function addItem() {
		    alert("Item has been added to food list.");
		}
