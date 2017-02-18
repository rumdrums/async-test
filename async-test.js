// this blocks main loop:

var j=0;
function doStuff() {
  j++;
  console.log('getting: ', j);
	var client = new XMLHttpRequest();
	client.open("GET", "/", false);	
	client.send(null);
	client.responseText
};

var i=0;
while (1) {
  i++;
  console.log('barf');
  doStuff()
}

// this will never actually call the stuff in setTimeout()

var j=0;
function doStuff() {
 console.log('doing stuff, maybe')
  setTimeout(function() {
	  j++;
	  console.log('getting: ', j);
		var client = new XMLHttpRequest();
		client.open("GET", "/", false);	
		client.send(null);
		client.responseText
	}, 0);
};

var i=0;
while (1) {
  i++;
  console.log('barf');
  doStuff()
}



