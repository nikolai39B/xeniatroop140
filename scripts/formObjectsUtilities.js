/*
Sets the width of the given labels with respect to the given reference
object. Also, because it generally looks better, this method uses 2.25
instead of exactly one half.

referenceObject: the id of the object whose width to use to set the label widths
labelsToSet: a list of ids of labels whose widths to change
*/
function setLabelWidths(referenceObjectId, labelIdsToSet) {
    // Get the reference object and compute the new width
    var refObj = document.getElementById(referenceObjectId);
    var newWidth = refObj.clientWidth / 2.25 + "px";

    // Other variables
    var label;
    
    for (var ii = 0; ii < labelIdsToSet.length; ii++) {
        label = document.getElementById(labelIdsToSet[ii]);
        label.style.width = newWidth;
    }
}

/*
This method adds delegates to the window.onload and window.onresize
events to center the given labels in the page.

currentWindow: the current window
labelIdsToSet: a list of ids of labels to center
*/
function addSetLabelWidthsEvents(currentWindow, labelIdsToSet) {
    var mainContainerId = "d_page_content_container";
    var newDelegate = function() { 
        setLabelWidths(mainContainerId, labelIdsToSet);
    }

    currentWindow.onload = buildNewEvent(
        currentWindow.onload,
        newDelegate);

    currentWindow.onresize = buildNewEvent(
        currentWindow.onresize,
        newDelegate);
}