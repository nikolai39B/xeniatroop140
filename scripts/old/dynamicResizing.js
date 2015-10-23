/// <reference path="referencePaths.js" />

/* 
FILE:
    dynamicResizing.js

DIRECTORY:
    xeniatroop140/scripts

DESCRIPTION:
    This file contians the functions to dynamically resize and center content. Most of these
    methods are designed to be called on window load and resize to insure that the given
    elements remain in the same relative location.

    NOTE: These capabilities should be obtainable using only css. As a result, don't use these methods
    unless you have too.
*/

function resizeWidthBasedOnObject(referenceElementId, elementIdsToSet, percentRefWidth, removePadding, offset) {
    /// <summary>
    /// Sets the width of the given elements relative to the given element.
    /// </summary>
    /// <param name="referenceElementId" type="string">The id of the element to use as reference when setting the other elements.</param>
    /// <param name="elementIdsToSet" type="string[]">A list of ids of the elements whose widths to set.</param>
    /// <param name="percentRefWidth" type="double">A number between 0 and 1 that describes how much of the reference element's width to set the width of the other elements.</param>
    /// <param name="removePadding" type="bool">Whether to include the padding in the ref element's width.</param>
    /// <param name="offset" type="int">An additional offset from the new calculated width.</param>

    // Get the reference object and compute the new width
    var refObj = document.getElementById(referenceElementId);

    // Get the padding
    var totalHorizontalPadding = 0;
    if (removePadding) {
        var computedStyle = window.getComputedStyle(refObj, null);
        var totalHorizontalPadding = parseInt(computedStyle.getPropertyValue('padding-left'));
        totalHorizontalPadding += parseInt(computedStyle.getPropertyValue('padding-right'));
    }

    // Get the new width
    var newWidth = (refObj.clientWidth - totalHorizontalPadding) * percentRefWidth + offset;
    newWidth += "px";

    // Modify the element widths
    var element;
    for (var ii = 0; ii < elementIdsToSet.length; ii++) {
        element = document.getElementById(elementIdsToSet[ii]);
        element.style.width = newWidth;
    }
}

function addResizeWidthsEvents(referenceElementId, elementIdsToSet, percentRefWidth, removePadding, offset) {
    /// <summary>
    /// Adds delegates to the window.onload and window.onresize events to call resizeWidthBasedOnObject() with the given parameters.
    /// </summary>
    /// <param name="referenceElementId" type="string">The id of the element to use as reference when setting the other elements.</param>
    /// <param name="elementIdsToSet" type="string[]">A list of ids of the elements whose widths to set.</param>
    /// <param name="percentRefWidth" type="double">A number between 0 and 1 that describes how much of the reference element's width to set the width of the other elements.</param>
    /// <param name="removePadding" type="bool">Whether to include the padding in the ref element's width.</param>
    /// <param name="offset" type="int">An additional offset from the new calculated width.</param>

    var newDelegate = function () {
        resizeWidthBasedOnObject(referenceElementId, elementIdsToSet, percentRefWidth, removePadding, offset);
    }

    window.onload = buildNewEvent(
        window.onload,
        newDelegate);

    window.onresize = buildNewEvent(
        window.onresize,
        newDelegate);
}

function addResizeWidthsEventsForFormCentering(elementIdsToSet) {
    /// <summary>
    /// Adds delegates to the window.onload and window.onresize events to call resizeWidthBasedOnObject() for the given elements.
    /// Uses the defaults for the other parameters.
    /// </summary>
    /// <param name="elementIdsToSet" type="string[]">A list of ids of the elements whose widths to set.</param>
    var mainContainerId = "d_page_content_container";
    var percentageOfWidthOfContainer = 0.43;

    addResizeWidthsEvents(mainContainerId, elementIdsToSet, percentageOfWidthOfContainer, false, 0);
}
