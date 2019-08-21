contract Election {
    int Totalvote;
    int bjpv;
    int cv;
    int aapv;
    int notav;
    

    constructor() public{
        Totalvote=0;
        bjpv=0;
        cv=0;
        aapv=0;
        notav=0;
    }

    function bjp() public {
        bjpv++;
        Totalvote++;
     
 
        
    }
    function congress() public {
        cv++;
        Totalvote++;
     
    
    }
    function aap() public {
        aapv++;
        Totalvote++;
     

    }
    function nota() public {
        notav++;
        Totalvote++;
      

    }

    function getbjp() public view returns (int){
        return bjpv;
    }
    function getcongress() public view returns (int){
        return cv;
    }
    function getaap() public view returns (int){
        return aapv;
    }
    function getnota() public view returns (int){
        return notav;
    }
    function gettv() public view returns (int){
        return Totalvote;
    }
}