//Controls sizing of elements with screen width
function songViewOnResize(renderer){
    renderer.changeABC(renderer.abcString); //Rerenders the sheet music at a new width
    //Tbh, I don't know why this works. As far as I know, renderer.abcString is not a valid class variable.

    if (pContent.offsetWidth<450){ //Changes the size of certain elements if on a phone
        
        $(".control-button font").attr("size",6);
        $("div.change-clef").html("")


        
        
        $("#OctaveDown font").html("↓↓")
        $("#OctaveUp font").html("↑↑")
        $("#SemitoneDown font").html("↓")
        $("#SemitoneUp font").html("↑")
        $("button.control-button.4-wide span.octave-text").html("")
        $("button.control-button.4-wide span.semitone-text").html("")
        
        
    }else{
        $(".control-button font").attr("size",6);
        $("div.change-clef").html("Change Clef")


        $("#OctaveDown font").html("↓")
        $("#OctaveUp font").html("↑")
        $("#SemitoneDown font").html("↓")
        $("#SemitoneUp font").html("↑")
        $("button.control-button.4-wide span.octave-text").html("Octave")
        $("button.control-button.4-wide span.semitone-text").html("Semitone")
    }
}