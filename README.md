# ant-colony-optimisation

Continuous Assessment for ECM3412 - Nature-Inspired Computation, set by Prof. Ayah Helal (Year 3, Semester 1). Implements the ant colony optimisation algorithm to address the travelling salesperson problem for two given networks. Please see `results/results.pdf` for insights on results and written answers to questions.

This work received a final mark of 70/100.

Please see `specification.pdf` for specification.

### Prerequisites

Project was developed in Python 3. Requirements can be viewed in requirements.txt.

`aco.py` and `elitist-aco.py` require `ant.py` and `load_data.py` to run.

### Usage

The program is executed from `aco.py`. To run the program, please use 

```
python aco.py
```

To run `elitist-aco.py`, please use 

```
python elitist-aco.py
```

Details on modifying parameters/variables to reflect experiments can be found in the Python source code.
This is done at the call of the main method, right at the bottom of the script.

### Results

Results shown in `results/results.pdf` and the associated text files, which can be found in `results/BurmaResults/` and `results/BrazilResults/`. Execution durations are also stored in the text files, and images are included in the directories.
