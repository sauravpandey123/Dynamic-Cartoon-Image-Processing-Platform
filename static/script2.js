const image = document.getElementById('converted');
const brightnessSlider = document.getElementById('brightness');

brightnessSlider.addEventListener('input', function () {
  const brightnessValue = parseFloat(this.value);
  changeBrightness(image, brightnessValue);
});

function changeBrightness(image, brightnessValue) {
  image.style.filter = `brightness(${brightnessValue * 10 + 150}%)`;
}

const downloadBtn = document.getElementById('download-btn');

// Ensure the image is fully loaded
image.addEventListener('load', function () {
  downloadBtn.addEventListener('click', function () {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    const brightness = parseFloat(brightnessSlider.value) * 10 + 100;

    canvas.width = image.naturalWidth;
    canvas.height = image.naturalHeight;

    ctx.filter = `brightness(${brightness}%)`;
    ctx.drawImage(image, 0, 0);

    const updatedImageUrl = canvas.toDataURL('image/jpeg');

    const link = document.createElement('a');
    link.href = updatedImageUrl;
    link.download = 'downloadedImage.jpg';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  });
});
