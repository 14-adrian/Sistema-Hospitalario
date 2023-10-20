$(document).ready(function(){
    eel.fetch_diag()
    eel.get_user_online()
    eel.get_DMedico()
    eel.get_DPaciente()
    eel.get_DMedicina()
    $("#btn_addnew").on("click", function() {
        $("#Addnewmodal").show();
    });
    $(".close").on("click", function() {
        $("#Addnewmodal").hide();
        location.href = "crudDiagnosticos.html";
    });
    $(".closeEdit").on("click", function() {
        $("#Editmodal").hide();
        location.href = "crudDiagnosticos.html";
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

eel.expose(action_NM)
function action_NM(registers){ 
    registers.forEach(showNM)
    registers.forEach(showNME)
}

eel.expose(action_NP)
function action_NP(registers){ 
    registers.forEach(showNP)
    registers.forEach(showNPE)
}

eel.expose(action_MD)
function action_MD(registers){ 
    registers.forEach(showMD)
    registers.forEach(showMDE)
}

//-------------EDITAR----------------
eel.expose(action_edit_m)
function action_edit_m(editMedicos){ 
   editMedicos.forEach(get_diag_values)
}

async function btn_edit(id){ 
    eel.get_cita(id)
    $("#Editmodal").show();
}

function get_diag_values(item, index){
    if (index == 0) {
        document.getElementById("m_id").value = item;
    } else if (index == 1) {
        document.getElementById("edit_NP").value = item;
    } else if (index == 2) {
        document.getElementById("edit_NM").value = item;
    } else if (index == 3) {
        document.getElementById("edit_IDC").value = item;
    }else if (index == 4) {
        document.getElementById("edit_Desc").value = item;
    }else if (index == 5) {
        document.getElementById("edit_Medicina").value = item;
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
    var td8 = document.createElement("td");

    var id = item[0]
    td.innerText = item[0]
    td2.innerText = item[1]
    td3.innerText = item[2]
    td4.innerText = item[3]
    td5.innerText = item[4]
    td6.innerText = item[5]
                
    td8.innerHTML = '<button type="button" class="btn-warning" onclick="btn_edit('+id+')">Editar</button> <button type="button" class="btn-danger" onclick="buttondelete('+id+')">Eliminar</button>'
                
    get_table.appendChild(tr)
    tr.appendChild(td)
    tr.appendChild(td2)
    tr.appendChild(td3)
    tr.appendChild(td4)
    tr.appendChild(td5)
    tr.appendChild(td6)
    tr.appendChild(td8)
}

//--------------------AGREGAR-----------------------
function showNM(item, index){
    var get_table = document.getElementById("txtNM");
    var op = document.createElement("option");

    var id = item[0]
    op.innerText = item[0]
                
    get_table.appendChild(op)
}

function showNME(item, index){
    var get_table = document.getElementById("edit_NM");
    var op = document.createElement("option");

    var id = item[0]
    op.innerText = item[0]
                
    get_table.appendChild(op)
}

function showNP(item, index){
    var get_table = document.getElementById("txtNP");
    var op = document.createElement("option");

    var id = item[0]
    op.innerText = item[0]
                
    get_table.appendChild(op)
}
function showNPE(item, index){
    var get_table = document.getElementById("edit_NP");
    var op = document.createElement("option");

    var id = item[0]
    op.innerText = item[0]
                
    get_table.appendChild(op)
}

function showMD(item, index){
    var get_table = document.getElementById("txtMedicina");
    var op = document.createElement("option");

    var id = item[0]
    op.innerText = item[0]
                
    get_table.appendChild(op)
}
function showMDE(item, index){
    var get_table = document.getElementById("edit_Medicina");
    var op = document.createElement("option");

    var id = item[0]
    op.innerText = item[0]
                
    get_table.appendChild(op)
}

async function agregar_medico(){
    $( "#myform" ).validate({
            messages: {
                txtID: {
                    required: "Porfavor Ingrese el ID"
                },
                txtIDC: {
                    required: "Porfavor Ingrese el ID de la cita"
                },
                txtDESC: {
                    required: "Porfavor Ingrese la Descripcion"
                },
            },
            submitHandler: function(form) {
                eel.save_diag($('#txtID').val(),$('#txtNP').val(),$('#txtNM').val(),$('#txtIDC').val(),$('#txtDESC').val(),$('#txtMedicina').val())
            }
    });
};
     
eel.expose(save_return); 
function save_return(status){
    if (status == "success"){
        $('#return_register').text('Nuevo Diagnostico Agregado!');
        $('#txtID').val('');
        $('#txtIDC').val('');
        $('#txtDESC').val('');
    }
    if (status == "failure"){
        $('#return_register').text('Error al agregar, asegurese de no haber dejado espacios en blanco.');
    }
};

// Editar Medico
async function actualizar_medico(){
    $( "#myformEditMed" ).validate({
            messages: {
                edit_IDC: {
                    required: "Porfavor Ingrese el Tipo"
                },
                edit_DESC: {
                    required: "Porfavor Ingrese la Fecha "
                },
            },
            submitHandler: function(form) {
                eel.update_diag($('#m_id').val(),$('#edit_NP').val(),$('#edit_NM').val(),$('#edit_IDC').val(),$('#edit_DESC').val(),$('#edit_Medicina').val())
            }
    });
};
eel.expose(update_return); 
function update_return(status){
    if (status == "success"){
        $('#return_update').text('El Diagnostico se actualizo correctamente!');
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
    eel.get_delete_diag(id)
}

eel.expose(delete_return)
function delete_return(status){ 
    if (status == "success"){
        location.href = "crudDiagnosticos.html";
    }
    if (status == "failure"){
        $('#return_delete').text('Ocurrio un error al eliminar el diagnostico');
    }
}