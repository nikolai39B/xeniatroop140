/// <reference path="referencePaths.js" />

/* 
FILE:
    eventUtilities.js

DIRECTORY:
    xeniatroop140/scripts

DESCRIPTION:
    This file contians the functions to safely handle events.
*/

function buildNewEvent(oldDelegate, funcToAdd) {
    /// <summary>
    /// Constructs a new delegate using the old delegate and the new method.
    /// </summary>
    /// <param name="oldDelegate" type="function">The old delegate to use.</param>
    /// <param name="funcToAdd" type="function">The new method to add to the delegate.</param>
    /// <returns type="function">The new delegate.</returns>    

    // If the old delegate isn't a function, simply return the
    // new function
    if (typeof oldDelegate != 'function') {
        return funcToAdd;
    }
    
    // Otherwise, make a new function to call everything
    else {
        return function() {
            if (oldDelegate) {
                oldDelegate();
            }
            funcToAdd();
        };
    }
}
