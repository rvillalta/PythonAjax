$(document).ready(function(){
	alert('Aqui voy !!');
})
document.getElementById('boton').addEventListener('click', function() {
      fetch('http://localhost:5000/addtask',{
      		method: 'POST',
      		headers: {
      			    'Accept': '*/*',
      			    'Content-Type': 'application/json'
      			},
      			body:JSON.stringify({
					    "title": "Palili2",
					    "description": "Todavia Huele a Berrenchin !!!"
					})

      })
        .then(response => {
        	//debugger
        })
        .catch(error => {
        	console.log(error)
        });
    });

function ajaxPositive(response) {
      console.log('response.ok: ', response.ok);
      if(response.ok) {
        response.text().then(showResult);
      } else {
        showError('status code: ' + response.status);
      }
    }

    function showResult(txt) {
      console.log('muestro respuesta: ', txt);
    }

    function showError(err) { 
      console.log('muestor error', err);
    }