/*
Sets the width of the given labels with respect to the given reference
object.

percentAcrossRefObj suggested values:
    for normal label/textbox setup: 0.43

referenceObject: the id of the object whose width to use to set the label widths
labelsToSet: a list of ids of labels whose widths to change
percentAcrossRefObj: how far across the reference object to set the label widths.
    should be 0 < x < 1.
*/
function setLabelWidths(referenceObjectId, labelIdsToSet, percentAcrossRefObj) {
    // Get the reference object and compute the new width
    var refObj = document.getElementById(referenceObjectId);
    var newWidth = refObj.clientWidth * percentAcrossRefObj + "px";

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
percentAcrossRefObj: how far across the reference object to set the label widths.
    should be 0 < x < 1.
*/
function addSetLabelWidthsEvents(currentWindow, labelIdsToSet, percentAcrossRefObj) {
    var mainContainerId = "d_page_content_container";
    var newDelegate = function() { 
        setLabelWidths(mainContainerId, labelIdsToSet, percentAcrossRefObj);
    }

    currentWindow.onload = buildNewEvent(
        currentWindow.onload,
        newDelegate);

    currentWindow.onresize = buildNewEvent(
        currentWindow.onresize,
        newDelegate);
}
