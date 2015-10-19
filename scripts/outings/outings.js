/*
Sets the width of the given element to half the width of the reference
object.

referenceObject: the id of the object whose width to use to set the element widths
elementIds: a list of ids of the elements whose widths to set
*/
function setElementWidthToHalf(referenceObjectId, elementIdsToSet) {
    // Get the reference object and compute the new width
    var refObj = document.getElementById(referenceObjectId);

    // Get the padding
    var computedStyle = window.getComputedStyle(refObj, null);
    var totalHorizontalPadding = parseInt(computedStyle.getPropertyValue('padding-left'));
    totalHorizontalPadding += parseInt(computedStyle.getPropertyValue('padding-right'));

    console.log(refObj.clientWidth * 0.50);
    console.log(totalHorizontalPadding);

    // Get the new width, but subtract the half the horizontal padding + 1 so that two
    // will display side by side
    var newWidth = refObj.clientWidth * 0.50 - (totalHorizontalPadding / 2.0) - 3;
    newWidth += "px";

    // Other variables
    var element;

    for (var ii = 0; ii < elementIdsToSet.length; ii++) {
        element = document.getElementById(elementIdsToSet[ii]);
        element.style.width = newWidth;
    }
}

/*
This method adds delegates to the window.onload and window.onresize
events to modfiy the width of the given element

currentWindow: the current window
referenceObject: the id of the object whose width to use to set the element widths
outingId: the id of the outing whose half rows to modify
*/
function addSetElementWidthToHalfEventsForOuting(outingId) {
    // Get the reference object id
    var referenceObjectId = outingId + "_container";

    // Get the element ids
    var elementIdsToSet = [];
    var numberOfHalfRows = 4;
    for (var ii = 0; ii < numberOfHalfRows; ii++) {
        elementIdsToSet.push(outingId + "_row_half_" + ii);
    }

    var newDelegate = function () {
        setElementWidthToHalf(referenceObjectId, elementIdsToSet);
    }

    window.onload = buildNewEvent(
        window.onload,
        newDelegate);

    window.onresize = buildNewEvent(
        window.onresize,
        newDelegate);
}