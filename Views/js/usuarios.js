$(document).ready(function(){
    eel.fetch_users()
    eel.get_user_online()

    document.addEventListener('contextmenu', event => {
        event.preventDefault();
    });

    $("#btn_addnew").on("click", function() {
        $("#Addnewmodal").show();
    });
    $(".close").on("click", function() {
        $("#Addnewmodal").hide();
        location.href = "crudUsuarios.html";
    });
    $(".closeEdit").on("click", function() {
        $("#Editmodal").hide();
        location.href = "crudUsuarios.html";
    });
    $(".closedelete").on("click", function() {
        $("#Delete_modal_medico").hide();
        
      });
})

function link(target) {
    window.location.href=target;
}

eel.expose(action_out)
function action_out(registers){ 
    registers.forEach(showdata)
}

//-------------EDITAR----------------
eel.expose(action_edit_m)
function action_edit_m(editMedicos){ 
   editMedicos.forEach(get_user_values)
}

async function btn_edit(id){ 
    eel.get_user(id)
    $("#Editmodal").show();
}

function get_user_values(item, index){
    if (index == 0) {
        document.getElementById("m_id").value = item;
    } else if (index == 1) {
        document.getElementById("edit_Nombre").value = item;
    } else if (index == 2) {
        document.getElementById("edit_Correo").value = item;
    } else if (index == 3) {
        document.getElementById("edit_DUI").value = item;
    }else if (index == 4) {
        document.getElementById("edit_Cargo").value = item;
    }else if (index == 5) {
        document.getElementById("edit_Pass").value = item;
    }else if (index == 6) {
        document.getElementById("edit_User").value = item;
    }
    else {}
 
}
//----------------------CARGAR TABLA-------------------------------        
function showdata(item, index){
    var get_table = document.getElementById("medicoTable");
    var tr = document.createElement("tr");
    var td = document.createElement("td");
    var td2 = document.createElement("td");
    var td3 = document.createElement("td");
    var td4 = document.createElement("td");
    var td5 = document.createElement("td");
    var td6 = document.createElement("td");
    var td7 = document.createElement("td");
    var td8 = document.createElement("td");

    var id = item[0]
    td.innerText = item[0]
    td2.innerText = item[1]
    td3.innerText = item[2]
    td4.innerText = item[3]
    td5.innerText = item[4]
    td6.innerText = "******"
    td7.innerText = item[6]
                
    td8.innerHTML = '<button type="button" class="btn-warning" onclick="btn_edit('+id+')">Editar</button> <button type="button" class="btn-danger" onclick="buttondelete('+id+')">Eliminar</button>'
                
    get_table.appendChild(tr)
    tr.appendChild(td)
    tr.appendChild(td2)
    tr.appendChild(td3)
    tr.appendChild(td4)
    tr.appendChild(td5)
    tr.appendChild(td6)
    tr.appendChild(td7)
    tr.appendChild(td8)
}

//--------------------AGREGAR-----------------------
async function agregar_medico(){
    $( "#myform" ).validate({
            messages: {
                txtID: {
                    required: "Porfavor Ingrese el ID"
                },
                txtNombre: {
                    required: "Porfavor Ingrese el Nombre"
                },
                txtCorreo: {
                    required: "Porfavor Ingrese el Correo"
                },
                txtDUI: {
                    required: "Porfavor Ingrese el DUI"
                },
                txtCargo: {
                    required: "Porfavor Ingrese el Cargo"
                },
                
                txtPass: {
                    required: "Porfavor Ingrese la Contraseña"
                },
                txtUser: {
                    required: "Porfavor Ingrese el nombre de Usuario"
                },
            },
            submitHandler: function(form) {
                eel.save_users($('#txtID').val(),$('#txtNombre').val(),$('#txtCorreo').val(),$('#txtDUI').val(),$('#txtCargo').val(),$('#txtPass').val(),$('#txtUser').val())
            }
    });
};
     
eel.expose(save_return); 
function save_return(status){
    if (status == "success"){
        $('#return_register').text('Nuevo Usuario Agregado!');
        $('#txtID').val('');
        $('#txtNombre').val('');
        $('#txtCorreo').val('');
        $('#txtDUI').val('');
        $('#txtCargo').val('');
        $('#txtPass').val('');
        $('#txtUser').val('');
    }
    if (status == "failure"){
        $('#return_register').text('Error al agregar, asegurese de no haber dejado espacios en blanco.');
    }
};

// Editar Medico
async function actualizar_medico(){
    $( "#myformEditMed" ).validate({
            messages: {
                edit_Nombre: {
                    required: "Porfavor Ingrese el Nombre"
                },
                edit_Correo: {
                    required: "Porfavor Ingrese el Correo"
                },
                edit_DUI: {
                    required: "Porfavor Ingrese el DUI"
                },
                edit_Cargo: {
                    required: "Porfavor Ingrese el Cargo"
                },
                
                edit_Pass: {
                    required: "Porfavor Ingrese la contraseña"
                },
                edit_User: {
                    required: "Porfavor Ingrese el Nombre de Usuario"
                },
            },
            submitHandler: function(form) {
                eel.update_user($('#m_id').val(),$('#edit_Nombre').val(),$('#edit_Correo').val(),$('#edit_DUI').val(),$('#edit_Cargo').val(),$('#edit_Pass').val(),$('#edit_User').val())
            }
    });
};
eel.expose(update_return); 
function update_return(status){
    if (status == "success"){
        $('#return_update').text('El Usuario se actualizo correctamente!');
    }
    if (status == "failure"){
        $('#return_register').text('Error al actualizar, asegurese de no haber dejado espacios en blanco.');
    }
};

//-------------------------------ELIMINAR--------------------

function buttondelete(id)
{
    document.getElementById("idvalue").value = id;
    $("#Delete_modal_medico").show();
}

async function btn_submitdelete(id){ 
    eel.get_delete_user(id)
}

eel.expose(delete_return)
function delete_return(status){ 
    if (status == "success"){
        location.href = "crudUsuarios.html";
    }
    if (status == "failure"){
        $('#return_delete').text('Ocurrio un error al eliminar el usuario');
    }
}