fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then(response => response.json())
    .then(data => {
        const movieList = document.querySelector("#list_movies");

        if (!data.results || data.results.length === 0) {
            console.error("No film!");
            return;
        }

        for (const film of data.results) {
            const listItem = document.createElement("li");
            listItem.textContent = film.title;
            movieList.appendChild(listItem);
        }
    })
    .catch(error => console.error("Error while retrieving data :", error));