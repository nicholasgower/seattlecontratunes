// Generated by ChatGPT. Prompt: "I want to move a server-side function in a django server to the client. Write a javascript equivalent to this code: def changedClef(self,id,clef="bass"):  
//        self_abc=self.get(id=id).abc
//        clef_index=self_abc.index("\nK:")
//        next_newline=self_abc.index("\n",clef_index+1)
//        injection=" clef={}".format(clef)
//        return "".join((self_abc[:next_newline],injection,self_abc[next_newline:]))"

function changedClef(abc, clef = "bass") {
    let clef_index = abc.indexOf("\nK:");
    let next_newline = abc.indexOf("\n", clef_index + 1);
    let injection = ` clef=${clef}`;
    let out=`${abc.substring(0, next_newline)}${injection}${abc.substring(next_newline)}`;
    console.log(out)
    return out;
}

function changeClefButton(){
    return function(){

    }

}

// Generated by ChatGPT. Prompt: "Write a javascript function that accepts an abc string and returns an abc string with all notes reduced in pitch by one octave."

function reducePitchByOneOctave(abcString) {
    // Regular expression to match ABC notes
    const noteRegex = /[A-Ga-g]['|,]*/g;
  
    // Function to handle the pitch reduction for each matched note
    function reducePitch(match) {
      // Iterate through each character in the matched note
      const reducedNote = match.replace(/[A-Ga-g]/g, (char) => {
        // If the character is a letter (representing a pitch), reduce it by one octave
        if (char >= 'a' && char <= 'g') {
          return String.fromCharCode(char.charCodeAt(0) + 7);
        } else if (char >= 'A' && char <= 'G') {
          return String.fromCharCode(char.charCodeAt(0) + 7);
        }
        // If the character is an apostrophe or comma, keep it unchanged
        return char;
      });
  
      return reducedNote;
    }
    // Replace each matched note in the ABC string with the reduced pitch
  const result = abcString.replace(noteRegex, reducePitch);

  return result;
}