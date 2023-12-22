
class MusicRenderer{
    constructor(abc,target,synthControlTarget){
        // Renders both sheet music(in target) and playback controls(in synthControlTarget) using abc notation "abc."

    var visualObj=ABCJS.renderAbc(target, abcString,{jazzchords:false});
    if (enable_playback == true){
        if (ABCJS.synth.supportsAudio()){
            var synth = new ABCJS.synth.CreateSynth();

            var myContext = new AudioContext();
            synth.init({
                audioContext: myContext,
                visualObj: visualObj[0],
                
                options: {
                   
                    pan: [-0.3, 0.3],
                    fadeLength:10
                }
            }).then(function (results){
                synth.prime().then((response) => {
                    console.log(response.status)
                });
            }).catch(function (reason){
                console.log(reason)
            });
            var synthControl = new ABCJS.synth.SynthController();

            synthControl.load("#"+synthControlTarget,null,{
                displayPlay:true,
                displayProgress:true,
                displayWarp:true,
                displayRestart:true,
                displayLoop:true
            });
            synthControl.setTune(visualObj[0],
                false,
                
                {
                        program: 41
                        
                    }
                
            ).then(function(){
                console.log("Audio successfully loaded.");
            }).catch(function (error){
                console.warn("Audio problem:", error);
            });
        }else{
            document.querySelector('#'+synthControlTarget).innerHTML = 
            "Audio is not supported in this browser.";
        }
    }
    return synthControl;
    }

}
//function renderMusic(abc,target,synthControlTarget){
    
//}
