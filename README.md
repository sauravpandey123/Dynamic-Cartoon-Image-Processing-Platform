# Dynamic Cartoon Image Processing Platform

![Cartoonifier Image](./background.PNG)

**Dynamic Cartoon Image Processing Platform** is a web-based application designed to transform images into cartoon-styled versions. It is built with Flask, Python, and OpenCV, providing users with an interactive experience and offering various features to enhance and personalize the cartoon effect.

## Features

- **Bilateral Filtering**: The application employs bilateral filtering for initial edge detection and image enhancement.
- **Color Quantization using K-means**: The K-means clustering algorithm is utilized for color quantization, enhancing cartoon aesthetics by consolidating similar color shades.
- **Dynamic User Interface**: The platform features a dynamic JavaScript interface that allows users to make real-time brightness adjustments and provides a streamlined image download process.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sauravpandey123/Dynamic-Cartoon-Image-Processing-Platform

2. Navigate to the project directory:
   ```bash
   cd dynamic-cartoon-image-processing-platform

3. Install the required packages
   ```bash
   pip install -r requirements.txt

4. Run the app
   ```bash
   python app.py

5. Open your browser and navigate to http://127.0.0.1:5000/ to access the platform.

## Usage

1. Upload an image using the upload button.
2. Adjust your "cartoon meter" to change your degree of cartoonification.
3. Click on the "Try It Now" button.
4. Adjust brightness of the cartoon if needed and download it to your device.

## Contributing
If you would like to contribute to this project or suggest improvements, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License.
