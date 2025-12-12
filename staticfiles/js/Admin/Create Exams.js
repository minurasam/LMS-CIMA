let levels = document.getElementById("lecture-level");
const subjects = document.getElementById("lecture-subject");
const types = document.getElementById("types");
const BA1 = document.getElementById("BA1");
const BA2 = document.getElementById("BA2");
const BA3 = document.getElementById("BA3");
const BA4 = document.getElementById("BA4");
const E1 = document.getElementById("E1");
const P1 = document.getElementById("P1");
const F1 = document.getElementById("F1");
const E2 = document.getElementById("E2");
const P2 = document.getElementById("P2");
const F2 = document.getElementById("F2");
const E3 = document.getElementById("E3");
const P3 = document.getElementById("P3");
const F3 = document.getElementById("F3");

levelSelect();

var exams = new Array();

function levelSelect(){

	 	BA1.style.display="none";
		BA2.style.display="none";
	 	BA3.style.display="none";
	 	BA4.style.display="none";
	 	E1.style.display="none";
	 	P1.style.display="none";
	 	F1.style.display="none";
	 	E2.style.display="none";
	 	P2.style.display="none";
	 	F2.style.display="none";
	 	E3.style.display="none";
	 	P3.style.display="none";
	 	F3.style.display="none";
	
	if(levels.value == 'Level1') {
	 	BA1.style.display="block";
		BA2.style.display="block";
	 	BA3.style.display="block";
	 	BA4.style.display="block";
	}

	if(levels.value == 'Level2'){
		E1.style.display="block";
	 	P1.style.display="block";
	 	F1.style.display="block";
	}

	if(levels.value == 'Level3'){
		E2.style.display="block";
	 	P2.style.display="block";
	 	F2.style.display="block";
	}

	if(levels.value == 'Level4'){
		E3.style.display="block";
	 	P3.style.display="block";
	 	F3.style.display="block";
	}
	//console.log(levels.value);
}


function createExam(){

	if(levels.value == 'none' || subjects.value == 'none' || types.value == 'none'){
		document.getElementById("msg").style.opacity = '1';
	}else{

		getExams();
		let exam = {
			Exam_Level: levels.options[levels.selectedIndex].text,
			Exam_Subject: subjects.options[subjects.selectedIndex].text,
			Exam_Type: types.options[types.selectedIndex].text
		}
		exams.push(exam);
		localStorage.setItem("SavedExams",JSON.stringify(exams));

		console.log(levels.options[levels.selectedIndex].text);
		console.log(subjects.options[subjects.selectedIndex].text);
		console.log(types.options[types.selectedIndex].text);

		levels.value = 'none';
		subjects.value = 'none';
		types.value = 'none';
		parent.location='exams.html';
	}
	
}

function getExams() {
    var exm = localStorage.getItem("SavedExams");
    if(exm != null){
        exams=JSON.parse(exm);
    }
}

