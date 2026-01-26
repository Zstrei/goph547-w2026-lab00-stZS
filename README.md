# goph547-w2026-lab00-stZS
**Semester:** W2026  
**Instructor:** B. Karchewski  
**Author(s):** Zac Strei


An example repository setup for a simple Python package. Includes examples using Numpy arrays and Matplotlib for visualization.

The recommended way to download or clone the repository is by navigating to the desired directory in a terminal using the cd /path/to/directory command and running either git clone <repository-url> or gh repo clone <owner>/<repository> if the GitHub CLI is installed, which will download the repository files into a new local directory. The repository can also be downloaded/cloned by clicking the green CODE button above the repository directory tree, where it can be downloaded as single zip file or as individual files. Lastly, the repository can also be cloned using HTTPS, SSH, or GitHub CLI via Python. Just be sure to navigate to the directory the files will be stored in beforehand, via the cd /path/to/directory function. 

It is recommended to set up a virtual environment when running the attached files. To set up a virtual environment, navigate to the directory where the downloaded files are stored via the cd /path/to/directory function. Use either python -m venv .venv or python -m virtualenv .venv in PowerShell to create the virtual environment. To run the virtual environment, run source ./.venv/bin/activate. A "(.venv)" should appear on the left side of the Terminal, indicating that the virtual environment has been successfully created.

After setting up the virtual environment, a few packages must be installed to ensure the script runs correctly (numpy and matplotlib). These packages can be installed via the following command: pip install numpy matplotlib setuptools in PowerShell.

After installing the packages, the Python files can be run from PowerShell using run python driver.py or edited in your IDE of choice using code driver.py

The driver.py script, located in the examples/ directory, demonstrates fundamental functionality of the numpy and matplotlib libraries through a series of structured examples. The first portion of the script focuses on NumPy array creation and manipulation, including the construction of arrays and matrices, and the application of element-wise operations, matrix (dot-product) multiplication, and cross products to illustrate basic linear algebra concepts.

The second portion of the script performs image processing and visualization using the rock_canyon.jpg image included in the repository. The image is loaded as a numpy array, converted to grayscale, and cropped using array slicing to isolate a region of interest. Mean colour intensity values for the red, green, and blue channels are computed along both spatial dimensions of the image and visualized using matplotlib subplots. These plots provide a summary of colour variation across the image.





