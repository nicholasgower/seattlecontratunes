var sleepSetTimeout_ctrl;

    function sleep(ms) {
        clearInterval(sleepSetTimeout_ctrl);
        return new Promise(resolve => sleepSetTimeout_ctrl = setTimeout(resolve, ms));
    }



    const thisURL= new URL(window.location.toLocaleString());

    const urlParams= thisURL.searchParams;
    var visualOptions = { responsive: 'resize' };
    
    let abcString = '{{song.abc|escapejs}}';
    abcString=abcString.replace("&quot;",'\"');
    <!--alert(abcString)-->
    <!--var abcString ="X:1\nT:Example\nK:Bb\nBcde|\n";-->
    window.onload= function(){
        
        ABCJS.renderAbc("target", abcString,{jazzchords:false});
    }