# EarthCam-PRNG
## Installation
To install all required dependencies, execute the bash installation script:

`./install.sh`

## Execution
TODO

## Image Scraper
TODO

## Image Scrambler
The image scrambler permutes every pixel of the provided images (down to the individual RGB values).
An example of an imaged before and after scrambling is provided below.

## Image Converter
After xoring the scrambled images, the resulting image is measured in terms of entropy.
Specifically the R, G, and B channels of the image are measured for entropy separately and averaged to generate a single output value.
If the image contains enough entropy, the image is converted to a series of bytes (to be used elsewhere).
The histogram below showcases the frequency of byte values taken from images processed through the entire system.
![Byte Frequency Histogram](/images/frequency_histogram.png)

## Architecture
The system's entire architecture can be seen in the following image.
![Architecture Diagram](/images/architecture_diagram.png)

## Dependencies
* opencv-python (4.5.1.48)
* streamlink (2.0.0)
* numpy (1.20.1)
* pandas (1.2.3)
* scipy (1.6.1)
