async function run() {
    let n = await eel.getDataJson()();
    document.getElementById('edit_Host').value = n[0];
    document.getElementById('edit_Usuario').value = n[1];
    document.getElementById('edit_Pas').value = n[2];
    document.getElementById('edit_Db').value = n[3];
}
run();