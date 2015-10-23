/// <reference path="referencePaths.js" />

/* 
FILE:
    outings.js

DIRECTORY:
    xeniatroop140/scripts

DESCRIPTION:
    This file contains special behavior for the outings add page.
*/

$(document).ready(function () {
    // Add the event to resize textareas
    document.oninput = buildNewEvent(document.oninput, fitTextAreasToContent);
    fitTextAreasToContent();
});
