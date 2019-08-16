// Dragging
function dragover_handler(ev) {
    console.log("dragOver");
    // ev.currentTarget.style.background = "lightblue";
    ev.preventDefault();
}

function dragstart_handler(ev) {
    console.log("dragStart");
    ev.dataTransfer.setData("text", ev.target.id);
    ev.effectAllowed = "copyMove";
}

function drop_handler(ev) {
    console.log("Drop");
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}

function dragend_handler(ev) {
    console.log("dragEnd");
    // ev.target.style.border = "solid black";
    ev.dataTransfer.clearData();
}

