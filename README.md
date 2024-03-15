
# Simple Box Plot Creation using Matplotlib and VS Code

This repository contains instructions and a Python script for creating simple box plots using Matplotlib. 
![Figure_8](https://github.com/paulhosch/Box-Plot/assets/39274609/fc94c289-b5b2-42e8-bb8b-aeae587ee448)


## Setup

### Install Python

- Download the latest version of Python for your operating system from [python.org](https://www.python.org/).
- Follow the installation instructions, making sure to add Python to your system's PATH.

### Install Visual Studio Code (VS Code)

- Download VS Code from [code.visualstudio.com/download](https://code.visualstudio.com/download).
- Install VS Code by following the provided instructions.

### Install Python Extension for VS Code

- Open VS Code, access the Extensions view by clicking on the square icon on the sidebar or pressing `Ctrl+Shift+X`.
- Search for "Python" and install the extension provided by Microsoft.

## Installation

### Clone the Git Repository

Clone the Box Plot repository and navigate to it by running the following command in the VS Code Terminal:

```bash
git clone https://github.com/paulhosch/Box-Plot-dir.git
cd Box-Plot-dir
```

### Create a Virtual Python Environment

Inside the cloned directory, create a virtual environment by entering the following in the VS Code Terminal:

For Windows:
```bash
python -m venv boxPlotEnv
```

For macOS/Linux:
```bash
python3 -m venv boxPlotEnv
```

### Activate the Virtual Environment

Activate the virtual environment to use its Python interpreter and installed libraries. 

For Windows:
```bash
.\boxPlotEnv\Scripts\activate
```

For macOS/Linux:
```bash
source boxPlotEnv/bin/activate
```

### Setting Up VS Code to Use the Virtual Environment

VS Code can automatically suggest using the virtual environment in your project. To manually set the interpreter:

1. Open the Command Palette by pressing `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS).
2. Type `Python: Select Interpreter` and select it.
3. Choose the interpreter from your project's virtual environment folder (e.g., `./boxPlotEnv/bin/python3` or `.\boxPlotEnv\Scripts\python.exe`).

### Install Required Libraries

Install the necessary Python packages using pip. This installation will be local to the virtual environment. Required libraries include Matplotlib, Pandas, and Numpy. Install them by running:

```bash
pip install -r boxPlotReq
```

## Prepare Data

Ensure your data is preprocessed and saved in a CSV file. The data should be clean, with each column representing a different dataset for the box plot.

Below is an example of how the raw CSV file should look for creating multiple box plots in one diagram, with datasets of varying cardinalities:

```
SFM new;SFM crumpled;FFP2 folded;FFP2 open;RFM
0.047267442;0.055819672;0.286736842;0.066764706;0.060668151
...
```

## Run and Customize the Script

Navigate to `boxPlotMain.py` in the VS Code Editor. Update the `data_file_path` and `save_path` variables in the script to point to the correct locations on your system. You can also adjust the plot's appearance as desired. I highly recomend doing so with the help of chatGPT or Copiolot, simply copy and paste the main script and prompt the requested changes. 
To run the script, simply press the run button in VS Code.

