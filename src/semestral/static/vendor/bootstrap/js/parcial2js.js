function StoreData() {
    var table = document.getElementById("conSto");
    var row = table.insertRow(0);
    var nombre = row.insertCell(0);
    var email = row.insertCell(1);
    nombre.innerHTML = "NEW CELL1";
    email.innerHTML = "NEW CELL2";
}

function myDeleteFunction() {
    document.getElementById("myTable").deleteRow(0);
}