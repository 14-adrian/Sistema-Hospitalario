async function run() {
    let n = await eel.getDataJson()();
    document.getElementById('edit_Host').value = n[0];
    document.getElementById('edit_Usuario').value = n[1];
    document.getElementById('edit_Pas').value = n[2];
    document.getElementById('edit_Db').value = n[3];
}
run();

async function actualizar_db(){

    $( "#myformEditMed" ).validate({
        messages: {
            edit_Host: {
                required: "Porfavor Ingrese el Host"
            },
        },
        submitHandler: function(form) {
            eel.update_conf($('#edit_Host').val(),$('#edit_Usuario').val(),$('#edit_Pas').val(),$('#edit_Db').val())
            location.reload(true)
            window.close()
        }
    });
}

eel.expose(update_return); 
function update_return(status){
    if (status == "success"){
        $('#return_update').text('La configuracion se actualizo correctamente!');
    }
    if (status == "failure"){
    }
};