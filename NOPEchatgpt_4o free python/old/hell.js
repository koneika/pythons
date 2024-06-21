let searchUrl = "https://chatgpt.com/";

fetch(searchUrl)
  .then(response => response.text())
  .then(html => {
    // Здесь вы можете попытаться извлечь результаты поиска из полученного HTML
    console.log(html);
  });


let searchUrl = "https://chatgpt.com/";

window.open(searchUrl, "_blank");