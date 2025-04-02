fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then(response => response.json())
    .then(data => {
        if (data.hello) {
            document.querySelector("#hello").textContent = hello.data;
        } else {
            console.error('No translation found!');
        }
    })
    .catch(error => console.error("Error while retrieving data :", error));