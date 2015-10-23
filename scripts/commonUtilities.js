/// <reference path="referencePaths.js" />

/* 
FILE:
    commonUtilities.js

DIRECTORY:
    xeniatroop140/scripts

DESCRIPTION:
    This file contians general utility functions.
*/

//--------//
// Events //
//--------//
function buildNewEvent(oldDelegate, funcToAdd) {
    /// <summary>
    /// Constructs a new delegate using the old delegate and the new method.
    /// </summary>
    /// <param name="oldDelegate" type="function">The old delegate to use.</param>
    /// <param name="funcToAdd" type="function">The new method to add to the delegate.</param>
    /// <returns type="function">The new delegate.</returns>    
    // If the old delegate isn't a function, simply return the new function
    if (typeof oldDelegate != 'function') {
        return funcToAdd;
    }

        // Otherwise, make a new function to call everything
    else {
        return function () {
            if (oldDelegate) {
                oldDelegate();
            }
            funcToAdd();
        };
    }
}


//------//
// Text //
//------//
function fitTextAreasToContent() {
    /// <summary>
    /// Resizes the height of each textarea in the document to exactly fit its content.
    /// </summary>
    // Get the minimum height by finding the height of an arbitrary character
    var lineHeight = getTextHeight("a");

    // Loop through each textarea
    var height, numLines, text, textAreaWidth, width;
    $.each($("textarea"), function () {
        // Get the textarea width
        textAreaWidth = $(this).width();

        // Loop through each line in the textarea to compute the total number of lines
        numLines = 0;
        var lineWidth;
        $.each($(this).val().split("\n"), function (ii, line) {
            lineWidth = getTextWidth(line);

            // Factor in both empty and long lines
            numLines += Math.max(1, Math.ceil(lineWidth / textAreaWidth));
        });

        // Set the textarea dimensions
        $(this).height(numLines * lineHeight);
    });
};

function getTextWidth(text) {
    /// <summary>
    /// Gets the width of the given text.
    /// </summary>
    /// <param name="text" type="string">The text whose width to return.</param>
    /// <returns type="int">The width in pixels of the text.</returns>
    var textContainer = $("#d_text_dimensions_div");
    textContainer.html(text);
    return textContainer.innerWidth();
}

function getTextHeight(text) {
    /// <summary>
    /// Gets the height of the given text.
    /// </summary>
    /// <param name="text" type="string">The text whose height to return.</param>
    /// <returns type="int">The height in pixels of the text.</returns>
    var textContainer = $("#d_text_dimensions_div");
    textContainer.html(text);
    return textContainer.innerHeight();
}