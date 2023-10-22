const uploadBtn = document.getElementById("try");
const fileInput = document.getElementById("file-input");

uploadBtn.addEventListener("click", () => {
  fileInput.click();
});


const form = document.getElementById('upload-form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
});    // THIS IS IMPORTANT BECAUSE THIS PREVENTS THE DEFAULT ACTION OF REDIRECTING THE USER TO ANOTHER URL


function uploadImage(event) {
  // event.preventDefault();   // prevents the user from not putting in anything. 
  const form = document.getElementById('upload-form');
  const fileInput = document.querySelector('input[type="file"]');  
  tryItNow = document.getElementById("try")
  tryItNow.setAttribute("value","Processing...")
  tryItNow.disabled=true
  tryItNow.classList.toggle("process")
  cartoonValue = document.getElementById("colorquant").value
  cartoonValue = 20 - cartoonValue;
  blurBoost = document.getElementById("checkbox").checked  
  const file = fileInput.files[0];  //get the selected file object
  const formData = new FormData();  // new FormData object that can store key-value pairs
  formData.append('image', file); // image is the key, file is the value
  formData.append('k',cartoonValue);
  formData.append('blur',blurBoost);
  fetch('/upload', {  // make an HTTP request to the server to upload the file
    method: 'POST',  // use the POST method to submit the form
    body: formData   // submit formData
  })
  .then(response => response.json())
  .then(data => {
    const linkOriginal = data.link_original
    const linkConverted = data.link_converted 
    window.location.href = `/imagedisplay?link1=${linkOriginal}&link2=${linkConverted}`;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

fileInput.addEventListener('change', uploadImage);