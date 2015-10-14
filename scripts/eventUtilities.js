/* 
Constructs a new delegate using the old delegate and the new method.

oldDelegate: the old delegate to use
funcToAdd: the new method to add to the delegate

returns: function
*/
function buildNewEvent(oldDelegate, funcToAdd) {
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
