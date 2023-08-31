function erase(noteID){
    const requestOptions = {
    method: 'DELETE',
    redirect: 'follow'
  };

  fetch(`http://0.0.0.0:8080/delete/${noteID}`, requestOptions)
    .then(response => response.text())
    .then(result => {
      console.log(result)
      location.reload()
    })
    .catch(error => console.log('error', error));
  };

  function edit(noteID){
    var requestOptions = {
      method: 'POST',
      redirect: 'follow'
    };
    
    fetch(`http://0.0.0.0:8080/edit/${noteID}`, requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
  }