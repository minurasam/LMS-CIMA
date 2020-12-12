
const tableExams = document.getElementById("tableExams");



showExams();

function getExams() {
    var exm = localStorage.getItem("SavedExams");
    if(exm != null){
        exams=JSON.parse(exm);
    }
}

function showExams(){
	getExams();

	var x=tableExams.rows.length;
    while(--x){
        tableExams.deleteRow(x);
    }

    for(let i=0 ; i< exams.length ; i++){
        tableExams.insertRow().innerHTML="<td>"+(i+1)+"</td>"+
                    "<td>"+exams[i].Exam_Level+"</td>"+
                    "<td>"+exams[i].Exam_Subject+"</td>"+
                    "<td>"+exams[i].Exam_Type+"</td>"+
                    "<td>"+'<input type="button" id ="deleteButton" value = "Delete Exam" onClick="deleteRow(this);">'+"</td>";
    }
}


function deleteRow(obj) {

    var index = obj.parentNode.parentNode.rowIndex;
    alert("You Request to Delete "+exams[index-1].Exam_Subject);
    getExams();
    tableExams.deleteRow(index);

    exams=exams.slice(0,index-1).concat(exams.slice(index,exams.length));
    localStorage.setItem("SavedExams",JSON.stringify(exams));
    showExams();
}