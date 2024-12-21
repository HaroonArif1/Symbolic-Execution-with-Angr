# Symbolic Execution with Angr

This repository contains projects involving symbolic execution using the Angr framework. The work includes generating control flow graphs (CFGs) and performing symbolic execution on binary files.

## Overview
Symbolic execution is a technique for analyzing programs to determine inputs that cause specific behaviors. Using Angr, we implemented:
- **Task 1**: Control-Flow Graph (CFG) generation and analysis.
- **Task 2**: Symbolic execution to identify 'put' functions and calculate targeted addresses.

## Features
- **Task 1**:
  - Generated a static CFG using Angr's `CFGFast` feature.
  - Analyzed the graph for the number of nodes, edges, and instruction types.
- **Task 2**:
  - Performed symbolic execution to identify and generate correct inputs for 'put' functions.
 
## Binary File
The repository includes a sample binary file (`test`) in the `bin` directory. This file is used to demonstrate symbolic execution and control-flow graph analysis using Angr.

**Note:** The binary file is an ELF file compiled for Linux systems and is required to run the analysis scripts.

## Prerequisites
- Python 3.x
- Angr library
- Ubuntu (tested on 20.04)

## How to Run
### Clone the Repository
```bash
git clone https://github.com/HaroonArif1/Symbolic-Execution-with-Angr.git
cd Symbolic-Execution-with-Angr
```

### Install Dependencies
```bash
sudo apt-get update
sudo apt-get install python3-dev python3-pip
pip3 install angr
```

### Execute the Scripts
- **Task 1** (CFG Generation):
  ```bash
  python3 task1lab2.py
  ```
- **Task 2** (Symbolic Execution):
  ```bash
  python3 task2lab2.py
  ```

## Results
- **Task 1 (CFG Analysis):**
  - Nodes: 67
  - Edges: 78
  - Instruction Types: 22

- **Task 2 (Symbolic Execution):**
  - Identified the addresses of 'put' functions.
  - Generated inputs to trigger these functions.

## Files
- `task1lab2.py`: Script for CFG generation.
- `task2lab2.py`: Script for symbolic execution.
- `cfg.png`: Visual representation of the CFG.
- `cfg.raw`: Raw CFG data.

## Setup and Tutorials
### Installing Angr
1. Visit the official Angr repository: [https://github.com/angr/angr](https://github.com/angr/angr).
2. Follow the detailed installation guide: [Angr Installation Documentation](https://docs.angr.io/introductory-errata/install).

### Environment Setup
- **Ubuntu/Linux** (Tested on Ubuntu 20.04):
  ```bash
  sudo apt-get update
  sudo apt-get install python3-dev python3-pip
  pip3 install angr
  ```
- **Windows/Mac**: Refer to the [official installation guide](https://docs.angr.io/introductory-errata/install).

### Tutorials
- Learn the basics of Angr through this beginner-friendly tutorial:  
  [Angr Introduction (Part 0)](https://blog.notso.pro/2019-03-20-angr-introduction-part0/).
