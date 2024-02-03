
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
        this.changeABC(abc)
        

        //width=1000;
        

        
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
        //console.log(abcString);
        const body=document.querySelector('.content')
        window.devicePixelRatio=1
        const DPR= window.devicePixelRatio
        console.log(body.offsetWidth,body.clientWidth,DPR)
        
        const width= body.clientWidth*0.95;
        //const width=1400;
        //let wrap_rules={ minSpacing: 2, maxSpacing: 2,lastLineLimit: true,preferredMeasuresPerLine: 4 }
        let wrap_rules;
        if (width<700){
            wrap_rules={ minSpacing: 1.2, maxSpacing: 2.7,lastLineLimit: true };
        }else{
            wrap_rules=null;
        }

        this.visualObj=ABCJS.renderAbc(target, abcString,{jazzchords:false,staffwidth: width, wrap: wrap_rules, lineThickness:0.3,add_classes:true});

        //Makes additional modifications to the sheet music's appearance.
        //Default font size for extra text is 21. When width<740, scale the font proportionally so that text that would fit when width=740 fits on the screen.
        const font_size_bottom_standard=21;
        const font_size_composer_standard=19;
        const width_standard=900;
        if (width<width_standard){
            $("svg g.abcjs-meta-bottom text.abcjs-extra-text").attr("font-size",width/width_standard*font_size_bottom_standard)
            $("text.abcjs-composer").attr("font-size",width/width_standard*font_size_composer_standard)
            $("text.abcjs-rhythm").attr("font-size",width/width_standard*font_size_composer_standard)
        }


        
        //this.setupSynth();
        //this.changeSynthTune();

    }
    


    

}

//function renderMusic(abc,target,synthControlTarget){
    
//}
