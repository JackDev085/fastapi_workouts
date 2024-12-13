const cardContainers = document.querySelectorAll(".cards");

function create_card(card_create) {
  return `
  <div class="card">
    <div className="image">
      <img src="${card_create.gif_url}" alt="${card_create.name}" />
    </div>
    <div class="card-header">
      <h3>${card_create.name}</h3>
    </div>
    <div class="card-body">
      <p>${card_create.description}</p>
    </div>
  </div>
  `;
}

fetch("http://127.0.0.1:8000/treinos/")
  .then((response) => response.json())

  .then((data) => {
    data.forEach((card) => {
      cardContainers.forEach((container) => {
        container.innerHTML += create_card(card);
      });
    });
  })
  .catch((error) => {
    console.log(error);
  });
