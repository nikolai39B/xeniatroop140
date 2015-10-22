/// <reference path="referencePaths.js" />

/* 
FILE:
    outings.js

DIRECTORY:
    xeniatroop140/scripts

DESCRIPTION:
    This file contians the function to add the events to automatically resize the outing div elements.
*/

/* NOTE: this is commented out because I realized I could accomplish the effect using css.
function addResizeWidthsEventsForOutingRows(outingId) {
    /// <summary>
    /// Adds delegates to the window.onload and window.onresize events to call resizeWidthBasedOnObject() for the elements
    /// corresponding to the outing with the given id. Uses the defaults for the other parameters.
    /// </summary>
    /// <param name="outingId" type="int (or string)">The id of the outing whose elements' widths to set.</param>

    // Get the reference object id
    var referenceObjectId = outingId + "_container";

    // Get the element ids
    var elementIdsToSet = [];
    var numberOfHalfRows = 4;
    for (var ii = 0; ii < numberOfHalfRows; ii++) {
        elementIdsToSet.push(outingId + "_row_half_" + ii);
    }

    var percentageOfWidthOfContainer = 0.5;

    //addResizeWidthsEvents(referenceObjectId, elementIdsToSet, percentageOfWidthOfContainer, true, 0);
} */
