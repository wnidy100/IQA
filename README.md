# Image Quality Analysis (IQA) in Python

A simple test codes for IQA with Python
- BRISQUE
- SIMM

## Requirements

- Python 3.8 or higher
- Required Python packages:
  - `image-quality`
  - `opencv-python`

## Installation

1. Install the necessary packages:

    ```
    pip install image-quality
    pip install opencv-python
    ```

2. After installing the `image-quality` package, you will need to edit a file to ensure compatibility with the BRISQUE algorithm.

## Modification of the `image-quality` package

### Steps to modify the BRISQUE module:

1. Locate the `brisque.py` file inside the `imquality` folder, which is part of the `image-quality` package.
   
   - On most systems, you can find the package in the following directory after installation:
     ```
     <path_to_your_python_env>/Lib/python3.8/site-packages/imquality/brisque.py
     ```

2. Open the `brisque.py` file in a text editor.

3. **Remove** the `multichannel=False` syntax from **line 144**.

4. **Replace** the syntax on **line 45** from:
   
    ```python
    self.image = skimage.colour.rgb2gray(self.image)
    ```

    With the following conditional statement:

    ```python
    if len(self.image.shape) == 3:
        self.image = skimage.color.rgb2gray(self.image)
    ```
