var datos = [];


function add(id, name, cost){
    var idProd = id;
    var product = name;
    var price = cost;
    var cantidad = document.getElementById(id);

    datos.push(idProd);
    datos.push(product);
    datos.push(price);
    datos.push(cantidad.value);

    localStorage.setItem("Compra", JSON.stringify(datos));

    //alert("Copate: " + cantidad.value );

    //alert("id: " + datos[0] + "  Producto: " + datos[1] + " Precio: " + datos[2] + "arrayLEngh:");

    //localStorage.clear();
}