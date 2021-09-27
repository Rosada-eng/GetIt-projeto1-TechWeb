function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }

  // Exibe / Oculta menu de filtro
  const formTags = document.querySelector(".form-tags")
  const tagMenu = document.querySelector(".tags-container");

  tagMenu.addEventListener("click", () => {
    console.log("Clicked")
    
    if (formTags.style.display === 'flex'){
      formTags.style.display = 'none';
    }
    else {
      formTags.style.display = 'flex';
    }
  })

  // Oculta background de notes sem tags
  var cardTags = document.getElementsByClassName("card-tag")
  console.log(cardTags)
  for (tag of cardTags) {
    console.log(tag.innerText)
    if (tag.innerText == ""){
      console.log(tag)
      tag.style.backgroundColor = '#CECECE00';
    }
  }
  
});

