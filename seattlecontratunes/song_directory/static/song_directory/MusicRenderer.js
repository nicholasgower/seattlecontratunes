
class MusicRenderer{
    visualObj; //Class variables are declared here before the constructor assigns them.
    program;
    synth;
    synthControl;
    synthControlTarget;
    target;
    changeSynthTune(){
        this.synthControl.setTune(this.visualObj[0],
            false,
            
            {
                    program: this.program
                    
                }
            
        ).then(function(){
            console.log("Audio successfully loaded.");
        }).catch(function (error){
            console.warn("Audio problem:", error);
        });
    }
    changeSynthControl(){
        this.synthControl.load("#"+this.synthControlTarget,null,{
            displayPlay:true,
            displayProgress:true,
            displayWarp:true,
            displayRestart:true,
            displayLoop:true
        });
    }
    setupSynth(){
        if (ABCJS.synth.supportsAudio()){
            this.synth = new ABCJS.synth.CreateSynth();

            var myContext = new AudioContext();
            const thisSynth=this.synth;
            this.synth.init({
                audioContext: myContext,
                visualObj: this.visualObj[0],
                
                options: {
                
                    pan: [-0.3, 0.3],
                    fadeLength:10
                }
            }).then(function (results){
                


                thisSynth.prime().then((response) => {
                    console.log(response.status)
                });
            }).catch(function (reason){
                console.log(reason)
            });
            this.synthControl = new ABCJS.synth.SynthController();

            this.changeSynthControl()
            this.changeSynthTune()
        }
    }
    constructor(abc,target,synthControlTarget,program=41){
        // Renders both sheet music(in target) and playback controls(in synthControlTarget) using abc notation "abc."
        const enable_playback=true;
        const width= document.querySelector('body').offsetWidth;
        //console.log(width);
        this.visualObj=ABCJS.renderAbc(target, abcString,{jazzchords:false,staffwidth: width*0.92});
        this.program=program;
        this.synthControlTarget=synthControlTarget;
        this.target=target;
        if (enable_playback == true){
            this.setupSynth();
        }
    
    }
    get visualObj(){
        return visualObj;
    }

    set changeVisualObj(new_value){
        this.visualObj=new_value;
    }
    get synth(){
        return synth;
    }
    get synthControl(){
        return synthControl;
    }
    changeABC(abc){
        console.log(abc);
        this.visualObj=ABCJS.renderAbc(this.target, abc,{jazzchords:false});
        //this.setupSynth();
        //this.changeSynthTune();

    }
    
    

    

}
//function renderMusic(abc,target,synthControlTarget){
    
//}
