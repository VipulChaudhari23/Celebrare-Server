const form = document.getElementById("__form__");
const btn = document.getElementById("submit-btn");
const loader = document.getElementById("loading")

form.onsubmit = async (e) => {
    e.preventDefault();
    btn.style.display = "none";
    loader.style.display = "block";

    let response = await fetch('/create-video', {
        method: 'POST',
        body: new FormData(form)
    });

    let result = await response.json();

    alert(result["videoUrl"])
    // document.getElementById("output").innerHTML = result["videoUrl"]

    loader.style.display = "none";
    btn.style.display = "block";
}