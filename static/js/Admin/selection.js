var select=document.querySelector("#alecture-level");
var level1=select.options[select.selectedIndex].value;
var op1=document.querySelector("#op1");
var op2=document.querySelector("#op2");
var op3=document.querySelector("#op3");
var op4=document.querySelector("#op4");
var op5=document.querySelector("#op5");
var op6=document.querySelector("#op6");
var op7=document.querySelector("#op7");
var op8=document.querySelector("#op8");
var op9=document.querySelector("#op9");
var op10=document.querySelector("#op10");
var op11=document.querySelector("#op11");
var op12=document.querySelector("#op12");
var op13=document.querySelector("#op13"); 
var op14=document.querySelector("#op14");

var mo1=document.querySelector("#mo1");
var mo2=document.querySelector("#mo2");
var mo3=document.querySelector("#mo3");

//alert(select.options[select.selectedIndex].value);
//alert("test");


  if(level1=="none")
        {
            op2.style.display="none";
            op3.style.display="none";
            op4.style.display="none";
            op5.style.display="none";
            op6.style.display="none";
            op7.style.display="none";
            op8.style.display="none";
            op9.style.display="none";
            op10.style.display="none";
            op11.style.display="none";
            op12.style.display="none";
            op13.style.display="none";
            op14.style.display="none";
            
            mo1.style.display="none";
            mo2.style.display="none";
            mo3.style.display="none";
        }

function dp_select()
{
    
    var select=document.querySelector("#alecture-level");
    var level=select.options[select.selectedIndex].value;
    var select1=document.querySelector("#subs");
    var select2=document.querySelector("#lecture-module");
    mo1.style.display="block";
    mo2.style.display="block";
    mo3.style.display="block";
    
      if(level=="none")
        {
            select1.selectedIndex=0;
            select2.selectedIndex=0;
            op1.style.display="block";
            op2.style.display="none";
            op3.style.display="none";
            op4.style.display="none";
            op5.style.display="none";
            op6.style.display="none";
            op7.style.display="none";
            op8.style.display="none";
            op9.style.display="none";
            op10.style.display="none";
            op11.style.display="none";
            op12.style.display="none";
            op13.style.display="none";
            op14.style.display="none";
        }
    
      if(level=="Certificate Level")
        {
            select1.selectedIndex=0;
            select2.selectedIndex=0;
            op1.style.display="none"
            op2.style.display="block";
            op3.style.display="block";
            op4.style.display="block";
            op5.style.display="block";
            op6.style.display="none";
            op7.style.display="none";
            op8.style.display="none";
            op9.style.display="none";
            op10.style.display="none";
            op11.style.display="none";
            op12.style.display="none";
            op13.style.display="none";
            op14.style.display="none";
        }
    
      if(level=="Operational Level")
        {
            select1.selectedIndex=0;
            select2.selectedIndex=0;
            op1.style.display="none"
            op2.style.display="none";
            op3.style.display="none";
            op4.style.display="none";
            op5.style.display="none";
            op6.style.display="block";
            op7.style.display="block";
            op8.style.display="block";
            op9.style.display="none";
            op10.style.display="none";
            op11.style.display="none";
            op12.style.display="none";
            op13.style.display="none";
            op14.style.display="none";
        }
    
      if(level=="Management Level")
        {
            select1.selectedIndex=0;
            select2.selectedIndex=0;
            op1.style.display="none"
            op2.style.display="none";
            op3.style.display="none";
            op4.style.display="none";
            op5.style.display="none";
            op6.style.display="none";
            op7.style.display="none";
            op8.style.display="none";
            op9.style.display="block";
            op10.style.display="block";
            op11.style.display="block";
            op12.style.display="none";
            op13.style.display="none";
            op14.style.display="none";
        }
    
      if(level=="Strategic Level")
        {
            select1.selectedIndex=0;
            select2.selectedIndex=0;
            op1.style.display="none"
            op2.style.display="none";
            op3.style.display="none";
            op4.style.display="none";
            op5.style.display="none";
            op6.style.display="none";
            op7.style.display="none";
            op8.style.display="none";
            op9.style.display="none";
            op10.style.display="none";
            op11.style.display="none";
            op12.style.display="block";
            op13.style.display="block";
            op14.style.display="block";
        }
    
}


