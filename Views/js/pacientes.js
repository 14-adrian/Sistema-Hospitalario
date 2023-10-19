$(document).ready(function(){
    eel.fetch_pacientes()
    eel.get_user_online()
    $("#btn_addnew").on("click", function() {
        $("#Addnewmodal").show();
    });
    $(".close").on("click", function() {
        $("#Addnewmodal").hide();
        location.href = "crudPacientes.html";
    });
    $(".closeEdit").on("click", function() {
        $("#Editmodal").hide();
        location.href = "crudPacientes.html";
    });
    $(".closedelete").on("click", function() {
        $("#Delete_modal_pac").hide();
        
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
function action_edit_m(editPaciente){ 
   //alert(editemployees);
   editPaciente.forEach(get_paciente_values)
}

async function btn_edit(id){ 
    eel.get_paciente(id)
    $("#Editmodal").show();
}

function get_paciente_values(item, index){
    if (index == 0) {
        document.getElementById("m_id").value = item;
    }  else if (index == 1) {
        document.getElementById("edit_Mnombre").value = item;
    } else if (index == 2) {
        document.getElementById("edit_MTel").value = item;
    }else if (index == 3) {
        document.getElementById("edit_Mcorreo").value = item;
    }else if (index == 4) {
        document.getElementById("edit_Mfnac").value = item;
    }else if (index == 5) {
        document.getElementById("edit_Msexo").value = item;
    }else if (index == 6) {
        document.getElementById("edit_MAlt").value = item;
    }else if (index == 7) {
        document.getElementById("edit_MWH").value = item;
    }
    else {}
 
}
//----------------------CARGAR TABLA-------------------------------        
function showdata(item, index){
    var get_table = document.getElementById("pacienteTable");
    var tr = document.createElement("tr");
    var td = document.createElement("td");
    var td2 = document.createElement("td");
    var td3 = document.createElement("td");
    var td4 = document.createElement("td");
    var td5 = document.createElement("td");
    var td6 = document.createElement("td");
    var td7 = document.createElement("td");
    var td8 = document.createElement("td");
    var td9 = document.createElement("td");

    var id = item[0]
    td.innerText = item[0]
    td2.innerText = item[1]
    td3.innerText = item[2]
    td4.innerText = item[3]
    td5.innerText = item[4]
    td6.innerText = item[5]
    td7.innerText = item[6]
    td8.innerText = item[7]
                
    td9.innerHTML = '<button type="button" class="btn-warning" onclick="btn_edit('+id+')">Editar</button> <button type="button" class="btn-danger" onclick="buttondelete('+id+')">Eliminar</button>'
    //td5.className = "acoes"
    //td5.setAttribute("onclick","actions(this, 'documents');")
                
    get_table.appendChild(tr)
    tr.appendChild(td)
    tr.appendChild(td2)
    tr.appendChild(td3)
    tr.appendChild(td4)
    tr.appendChild(td5)
    tr.appendChild(td6)
    tr.appendChild(td7)
    tr.appendChild(td8)
    tr.appendChild(td9)
}

//--------------------AGREGAR-----------------------
async function agregar_paciente(){
    $( "#myform" ).validate({
            messages: {
                txtID: {
                    required: "Porfavor Ingrese el DUI"
                },
                txtNombre: {
                    required: "Porfavor Ingrese el Nombre"
                },
                txtTel: {
                    required: "Porfavor Ingrese el Telefono"
                },
                txtCorreo: {
                    required: "Porfavor Ingrese el Correo"
                },
                txtFNac: {
                    required: "Porfavor Ingrese la Fecha de Nacimiento"
                },
                txtSexo: {
                    required: "Porfavor Ingrese el Sexo"
                },
                txtAlt: {
                    required: "Porfavor Ingrese la Altura"
                },
                txtWH: {
                    required: "Porfavor Ingrese el Peso"
                }
            },
            submitHandler: function(form) {
                eel.save_paciente($('#txtID').val(),$('#txtNombre').val(),$('#txtTel').val(),$('#txtCorreo').val(),$('#txtFNac').val(),$('#txtSexo').val(),$('#txtAlt').val(),$('#txtWH').val())
            }
    });
};
     
eel.expose(save_return); 
function save_return(status){
    if (status == "success"){
        $('#return_register').text('Nuevo Paciente Agregado!');
        $('#txtID').val('');
        
        $('#txtNombre').val('');
        $('#txtTel').val('');
        $('#txtCorreo').val('');
        $('#txtFNac').val('');
        $('#txtSexo').val('');
        $('#txtAlt').val('');
        $('#txtWH').val('');
    }
    if (status == "failure"){
        $('#return_register').text('Error al agregar, asegurese de no haber dejado espacios en blanco.');
    }
};

// Editar Medico
async function actualizar_paciente(){
    $( "#myformEditMed" ).validate({
            messages: {
                edit_Mnombre: {
                    required: "Porfavor Ingrese el Nombre"
                },
                edit_MTel: {
                    required: "Porfavor Ingrese el Telefono"
                },
                edit_Mcorreo: {
                    required: "Porfavor Ingrese el Correo"
                },
                
                edit_Mfnac: {
                    required: "Porfavor Ingrese la Fecha de Nacimiento"
                },
                edit_Msexo: {
                    required: "Porfavor Ingrese el Sexo"
                },
                edit_MAlt: {
                    required: "Porfavor Ingrese la Altura"
                },
                edit_MWH: {
                    required: "Porfavor Ingrese el Peso"
                },
            },
            submitHandler: function(form) {
                eel.update_paciente($('#m_id').val(),$('#edit_Mnombre').val(),$('#edit_MTel').val(),$('#edit_Mcorreo').val(),$('#edit_Mfnac').val(),$('#edit_Msexo').val(),$('#edit_MAlt').val(),$('#edit_MWH').val())
            }
    });
};
eel.expose(update_return); 
function update_return(status){
    if (status == "success"){
        $('#return_update').text('El paciente se actualizo correctamente!');
    }
    if (status == "failure"){
        $('#return_register').text('Error al actualizar, asegurese de no haber dejado espacios en blanco.');
    }
};

//-------------------------------ELIMINAR--------------------

function buttondelete(id)
{
    document.getElementById("idvalue").value = id;
    $("#Delete_modal_pac").show();
}

async function btn_submitdelete(id){ 
    eel.get_delete_paciente(id)
}

eel.expose(delete_return)
function delete_return(status){ 
    if (status == "success"){
        location.href = "crudPacientes.html";
    }
    if (status == "failure"){
        $('#return_delete').text('Ocurrio un error al eliminar el paciente');
    }
}