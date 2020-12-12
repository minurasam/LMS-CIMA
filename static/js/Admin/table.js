//var drop_subs=document.querySelector("#drop_subs");
//var new_row=document.createElement("tr");
//var new_data=document.createElement("td");
var select=document.querySelector("#lecture-module");
var dsubs=document.querySelector("#drop_subs");
var drop1=document.querySelector("#dbutton");

drop1.style.display="none";


/*
new_data.textContent="new_data1";

new_row.appendChild(new_data);

table1.appendChild(new_row);
*/

const m1=["sub1","sub2","sub3"];
const m1_type=["PDF","PDF","PDF"];
const m2=["sub4","sub5","sub6"];
const m2_type=["PDF","Video","Video"];
const m3=["sub7","sub8","sub9"];
const m3_type=["Video","Video","Video"];


function subs_select()
{
    
    var module1=select.options[select.selectedIndex].value;
    
    if(module1=="none")
        {
            dsubs.innerHTML="Please select a Module"
            drop1.style.display="none";
        }
    
     else if(module1=="M1")
      {    
        drop1.style.display="block";  
        dsubs.innerHTML="";  
        $("#drop_subs").append("<table class=tbll><tr class=trdata><th class=thdata1><input type=checkbox id=checkAll></th><th class=thdata>Title</th><th class=thdata>Type</th></tr></table>");  
        for(i=0;i<m1.length;i++)
            {
                $(".tbll").append("<tr class=trdata><td class=chkdata><input type=checkbox class=checkb></td><td class=tddata><label class=lbl>"+m1[i]+"</label></td><td class=tddata><label>"+m1_type[i]+"</label></td></tr>");
            }
       //   $("#drop_subs").append("<label><input type=checkbox name=checkAll id=checkAll>Select All</label>");
      }
    else if(module1=="M2")
      {    
        drop1.style.display="block";  
        dsubs.innerHTML=""; 
        $("#drop_subs").append("<table class=tbll><tr class=trdata><th class=thdata1><input type=checkbox id=checkAll></th><th class=thdata>Title</th><th class=thdata>Type</th></tr></table>");    
        for(i=0;i<m2.length;i++)
            {
                 $(".tbll").append("<tr class=trdata><td class=chkdata><input type=checkbox class=checkb></td><td class=tddata><label class=lbl>"+m2[i]+"</label></td><td class=tddata><label>"+m2_type[i]+"</label></td></tr>");
            }
      }
    else if(module1=="M3")
      {     
        drop1.style.display="block";  
        dsubs.innerHTML="";
        $("#drop_subs").append("<table class=tbll><tr class=trdata><th class=thdata1><input type=checkbox id=checkAll></th><th class=thdata>Title</th><th class=thdata>Type</th></tr></table>");    
        for(i=0;i<m3.length;i++)
            {
                 $(".tbll").append("<tr class=trdata><td class=chkdata><input type=checkbox class=checkb></td><td class=tddata><label class=lbl>"+m3[i]+"</label></td><td class=tddata><label>"+m3_type[i]+"</label></td></tr>");
            }
      }
}
  
function drop()
{
   jQuery("input:checkbox:checked").parents("tr").remove();
}

document.getElementById("checkAll").onclick=function(){
    var checkboxes=document.getElementsByClassName("checkb");
    for(var checkbox of checkboxes)
        {
            checkbox.appendChecked=this.appendChecked;
        }
}
               
//$(".lbl").has("input:checked").remove();
