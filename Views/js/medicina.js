$(document).ready(function(){
    eel.fetch_medicina()
    eel.get_user_online()

    document.addEventListener('contextmenu', event => {
        event.preventDefault();
    });

    $("#btn_addnew").on("click", function() {
        $("#Addnewmodal").show();
    });
    $(".close").on("click", function() {
        $("#Addnewmodal").hide();
        location.href = "crudMedicina.html";
    });
    $(".closeEdit").on("click", function() {
        $("#Editmodal").hide();
        location.href = "crudMedicina.html";
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
function action_edit_m(editMedicina){ 
   editMedicina.forEach(get_medicina_values)
}

async function btn_edit(id){ 
    eel.get_medicina(id)
    $("#Editmodal").show();
}

function get_medicina_values(item, index){
    if (index == 0) {
        document.getElementById("m_id").value = item;
    } else if (index == 1) {
        document.getElementById("edit_Desc").value = item;
    } 
    else {}
 
}
//----------------------CARGAR TABLA-------------------------------        
function showdata(item, index){
    var get_table = document.getElementById("medicoTable");
    var tr = document.createElement("tr");
    var td = document.createElement("td");
    var td2 = document.createElement("td");
    var td8 = document.createElement("td");

    var id = item[0]
    td.innerText = item[0]
    td2.innerText = item[1]
                
    td8.innerHTML = '<button type="button" class="btn-warning" onclick="btn_edit('+id+')">Editar</button> <button type="button" class="btn-danger" onclick="buttondelete('+id+')">Eliminar</button>'
                
    get_table.appendChild(tr)
    tr.appendChild(td)
    tr.appendChild(td2)
    tr.appendChild(td8)
}

//--------------------AGREGAR-----------------------
async function agregar_medico(){
    $( "#myform" ).validate({
            messages: {
                txtID: {
                    required: "Porfavor Ingrese el ID"
                },
                txtDesc: {
                    required: "Porfavor Ingrese la Descripcion"
                },
            },
            submitHandler: function(form) {
                eel.save_medicina($('#txtID').val(),$('#txtDesc').val())
            }
    });
};
     
eel.expose(save_return); 
function save_return(status){
    if (status == "success"){
        $('#return_register').text('Nueva Medicina Agregado!');
        $('#txtID').val('');
        $('#txtDesc').val('');
    }
    if (status == "failure"){
        $('#return_register').text('Error al agregar, asegurese de no haber dejado espacios en blanco.');
    }
};

// Editar Medico
async function actualizar_medico(){
    $( "#myformEditMed" ).validate({
            messages: {
                edit_Desc: {
                    required: "Porfavor Ingrese la Descripcion"
                },
            },
            submitHandler: function(form) {
                eel.update_medicina($('#m_id').val(),$('#edit_Desc').val())
            }
    });
};
eel.expose(update_return); 
function update_return(status){
    if (status == "success"){
        $('#return_update').text('La Medicina se actualizo correctamente!');
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
    eel.get_delete_medicina(id)
}

eel.expose(delete_return)
function delete_return(status){ 
    if (status == "success"){
        location.href = "crudMedicina.html";
    }
    if (status == "failure"){
        $('#return_delete').text('Ocurrio un error al eliminar la medicina');
    }
}