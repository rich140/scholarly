const fill = document.querySelector('.fill');
const empties = document.querySelectorAll('.empty');

// Fill listeners
fill.addEventListener('dragstart', dragStart);
fill.addEventListener('dragend', dragEnd);

// Loop through empty boxes and add listeners
for (const empty of empties) {
    empty.addEventListener('dragover', dragOver);
    empty.addEventListener('dragenter', dragEnter);
    empty.addEventListener('dragleave', dragLeave);
    empty.addEventListener('drop', dragDrop);
}

// Drag Functions

function dragStart() {
    this.className += ' hold';
    setTimeout(() => (this.className = 'invisible'), 0);
    console.log("start");
}

function dragEnd() {
    this.className = 'fill';
    console.log("end");
}

function dragOver(e) {
    e.preventDefault();
    console.log("Over");

}

function dragEnter(e) {
    e.preventDefault();
    this.className += ' hovered';
    console.log("Enter");
}

function dragLeave() {
    this.className = 'empty';
    console.log("Leave");
}

function dragDrop() {
    this.className = 'empty';
    this.append(fill);
    console.log("Drop");
}



// Dragging
function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
}