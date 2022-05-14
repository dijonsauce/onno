//"Close" button and append it to each item on list.
var myodelist = document.getElementsby TagName("LI");
var i;
for (i = 0; i <myNodelist.length; i++) {
    var span = document,createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    myNodelist[i].appendChild(span)
}