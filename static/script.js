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
function sort() {
    sortable('.js-sortable-oneway', {
        forcePlaceholderSize: true,
        acceptFrom: false,
        placeholderClass: 'mb1 bg-navy border border-yellow'
    });
    sortable('.js-sortable-oneway-receive', {
        forcePlaceholderSize: true,
        acceptFrom: '.js-sortable-oneway,.js-sortable-oneway-receive',
        placeholderClass: 'mb1 bg-navy border border-yellow',
        customDragImage: function (draggedElement, elementOffset, event) {
            draggedElement.style.border = "1px solid grey"
            return {
                element: draggedElement,
                posX: event.pageX - elementOffset.left,
                posY: event.pageY - elementOffset.top
            }
        }
    });
}

