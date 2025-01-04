window.onload = function(){
    var i;
    var date = new Date();
    var last_year = date.getFullYear();
    var s = document.getElementsByTagName('select');
    for (i = 1900; i <= last_year; i++) {
        var element = document.createElement("option");
        element.setAttribute("value", i);
        element.textContent = i;
        s[0].appendChild(element);
    }
    for (i=1; i <= 12; i++){
        var element = document.createElement("option");
        element.setAttribute("value", i);
        element.textContent = i;
        s[1].appendChild(element);
    }
    for (i=1; i <= 31; i++){
        var element = document.createElement("option");
        element.setAttribute("value", i);
        element.textContent = i;
        s[2].appendChild(element);
    }
}