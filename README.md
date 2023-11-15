# High-Level-Event-Mining: A Framework (ICPM 2022) Experiment Replication

This repository is dedicated to the Experiment Replication assignment for the 2IMI00 Seminar Process Analytics course at Eindhoven University of Technology. The framework used in this project is based on [Bianka Bakullari's hlem-framework](https://github.com/biankabakullari/hlem-framework/tree/main).

## Data 
Ensure you have the required dataset dowloaded. It is required to place `.xes log` file into the `event_logs` folder of the folder. The dataset is available via:
https://data.4tu.nl/articles/dataset/BPI_Challenge_2017/12696884

## Installation

Ensure you have the required dependencies installed. Open your terminal or command prompt and run:

```plaintext
pip install -r requirements.txt
```
# ⚠️ Important Notice

If you're replicating the experiment with `evaluationbpm/evaluationbpm23.py`, take note of deprecated functions in the pm4py package (`A_eventually_B`, `A_eventually_B_eventually_C`, `A_eventually_B_eventually_C_eventually_D`). To ensure smooth execution, simply comment out the deprecation annotations in `algo/filtering/log/ltl/ltl_checker.py` file. 

## Replication Steps

Follow these steps to replicate the experiment:

  1. Preprocess the event log data by running the `split.py` script. Before running, update folder paths in the script according to your environment:
     ```plaintext
     python3 split.py
     ```
  2. Execute the High-Level Event Mining experiment using the `main.py` script. Run the following command:
     ```plaintext
     python3 main.py
     ```
  3. Merge the results and obtain the final output by running the `join.py` script. Before running, update folder paths in the script according to your environment:
     ```plaintext
     python3 join.py
     ```
  4. Execute the evaluation script `evaluation_bpm/evaluation_bpm23.py` to retrieve the evaluation of success rate and throughput time for the log. Before running, update folder paths in the script according to your environment:
     ```plaintext
     python3 evaluation_bpm/evaluation_bpm23.py
     ```
Ensure you execute these scripts in the specified order to successfully replicate the experiment. The code is compatible with Python 3.11.
