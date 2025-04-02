document.querySelector("#add_item").addEventListener("click", () => {
    const list = document.querySelector("my_list");
    const newElement = document.createElement("li");
    newElement.textContent = "Item";
    list.appendChild(newElement);
});