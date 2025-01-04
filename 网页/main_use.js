/*window.onload = function ()
{
    date = new Date()
    var year = date.getFullYear();
    var month = date.getMonth();
    var day = date.getDate();
    alert(year + '年' + (month + 1) + '月' + day + '日');
}*/
var flag1 = 0;
window.onload = function(){
    var obutton = document.getElementById("b1");
    obutton.onclick = function() {
        if (flag1 == 0) {
            var frame1 = document.createElement("iframe");
            frame1.src = 'pig_func.html'
            frame1.id = 'f1';
            document.body.appendChild(frame1);
            flag1 = 1;
        }
    }
}

