//invalid syntax! follow the session please
var computer = prompt("type in a lab ip address");

var matchIpPortHost = function(computer);
   if (computer === "173.12.76.129") {
      console.log("Okay " +computer+ "has a hostname of blueberry.head.org, and can be accsessed on port 20022");
   }
   else {
      console.log("sorry mate your address is not listed would you like us to add you?");
       confirm("you have the choice");
   }
};
matchIpPortHost(computer);
