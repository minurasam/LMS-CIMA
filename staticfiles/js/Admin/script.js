
function addRow() {
          
    var fName = document.getElementById("fname");
    var lName = document.getElementById("lname");
    var cimaID = document.getElementById("ID");
    var level = document.getElementById("level");
    var username = document.getElementById("user-name");
    var password = document.getElementById("pw");

    var table = document.getElementById("myTableData");
 
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    
    row.insertCell(0).innerHTML= rowCount;
    row.insertCell(1).innerHTML= fName.value;
    row.insertCell(2).innerHTML= lName.value;
    row.insertCell(3).innerHTML= cimaID.value;
    row.insertCell(4).innerHTML= level.value;
    row.insertCell(5).innerHTML= username.value;
    row.insertCell(6).innerHTML= password.value;
    row.insertCell(7).innerHTML= '<input type="button" value = "Delete" onClick="Javacsript:deleteRow(this)">';
    x=x+1

}
 
function deleteRow(obj) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("myTableData");
    table.deleteRow(index);
    
}