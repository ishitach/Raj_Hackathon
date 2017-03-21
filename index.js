//$function()({
//https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/hofAndMember/ForApp/WDYYYGG?client_id=

function funA(){
//const endpoint = 'https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/hofAndMember/ForApp/WDYYYGG?client_id=ad7288a4-7764-436d-a727-783a977f1fe1'; const names = []; fetch(endpoint) .then(blob => blob.json()) .then(data => names.push(...data));

	window.alert("wel");
}

$.ajax({
			url: 'https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/hofAndMember/ForApp/WDYYYGG?client_id=ad7288a4-7764-436d-a727-783a977f1fe1',
			//url:'http://jsonplaceholder.typicode.com/photos',
			success: funA
		});

//funA();
//ad7288a4-7764-436d-a727-783a977f1fe1
