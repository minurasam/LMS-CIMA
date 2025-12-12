











const dropButton = document.querySelector('#drop-button');
const msg = document.querySelector('.msg');
const dropList = document.querySelector('.droping');



dropButton.addEventListener('click',onSubmit);

const levelInput = document.querySelector('#dlecture-level');
const subjectInput = document.querySelector('#lecture-subject');
const moduleInput = document.querySelector('#lecture-module');





function onSubmit(e) {
	e.preventDefault();
    
	if((levelInput.value == 'none' || subjectInput.value == 'none') || moduleInput.value === 'none' ){
		msg.innerHTML = 'Please Select the above fields';
		setTimeout(() => msg.remove(),2500);
	}else{
		const list = document.createElement('li');
		list.appendChild(document.createTextNode(levelInput.value+' - '+subjectInput.value+' - '+moduleInput.value));
		dropList.appendChild(list);
	}
}

//dropButton.addEventListener('click',onSubmit);