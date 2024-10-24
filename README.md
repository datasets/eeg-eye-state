<a href="https://datahub.io/core/eeg-eye-state"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

This dataset contains instances of EEG measurements where the output is whether eye was open or not.

All data is from one continuous EEG measurement with the Emotiv EEG Neuroheadset. 
The duration of the measurement was 117 seconds. 
The eye state was detected via a camera during the EEG measurement and added later manually to the file after analyzing the video frames. 
* 0 the eye-open state;
* 1 indicates the eye-closed;

All values are in chronological order with the first measured value at the top of the data.

The features correspond to 14 EEG measurements from the headset, 
labeled AF3, F7, F3, FC5, T7, P, O1, O2, P8, T8, FC6, F4, F8, AF4.

## Data

This dataset was found on [OpenML - eeg-eye-state](https://www.openml.org/d/1471)

Data is located in directory `data`

`data/eeg-eye-state.csv`

## Preparation

This script should be run using Python 3.

Scripts are in directory `scripts`

`scripts/main.py`

## License
Licensed under the [Public Domain Dedication and Licence][pddl] (assuming
either no rights or public domain licence in source data).

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/