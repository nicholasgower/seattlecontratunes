function getClef(abc){
    let clef="";
    if (abcString.includes("clef=alto") || abcString.includes("clef=C")){
        clef="alto";
    }else if (abcString.includes("clef=bass") || abcString.includes("clef=F")){
        clef="bass";
    }else if (abcString.includes("clef=tenor")){
        clef="tenor";
    }else{
        clef="treble";
    }
    return clef
}