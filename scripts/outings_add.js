/// <reference path="referencePaths.js" />

/* 
FILE:
    outings.js

DIRECTORY:
    xeniatroop140/scripts

DESCRIPTION:
    This file contains special behavior for the outings add page.
*/

function resizeIt() {
    var splitText = $('.ta_form_textarea').val().split("\n");

    var lineHeight = getLineWidthAndHeight('a')[1];
    var textAreaWidth = $('.ta_form_textarea').width();

    var linecount = 0;
    for (var ii = 0; ii < splitText.length; ii++) {
        var lineWidth = getLineWidthAndHeight(splitText[ii])[0];
        //console.log(splitText[ii]);
        //console.log(getLineWidthAndHeight(splitText[ii]));
        linecount += Math.max(1, Math.ceil(lineWidth / textAreaWidth));
        //Math.ceil(splitText[ii] / cols);
    }

    $('.ta_form_textarea').height((linecount) * lineHeight);
    console.log($('.ta_form_textarea').height());
    console.log(linecount);
};

function getLineWidthAndHeight(line) {
    $('#d_test_string_dimensions').html(line);
    var h = $('#d_test_string_dimensions').innerHeight();
    var w = $('#d_test_string_dimensions').innerWidth();

    return [w, h];
}


$(document).ready(function () {
    document.oninput = buildNewEvent(document.oninput, resizeIt);
    resizeIt();
    //$('.ta_form_textarea').elastic();

});
