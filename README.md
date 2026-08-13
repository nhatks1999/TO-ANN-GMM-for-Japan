<img width="73" height="23" alt="image" src="https://github.com/user-attachments/assets/06aae942-6428-4884-a819-afe78ce0d904" /># TO-ANN-GMM-for-Japan
This repository is used to run the TO-ANN ground-motion prediction model. It contains the following files:
- The "fold_models" folder: contains the five trained fold models and corresponding input scalers.
- The "New_Data.csv": input file for prediction.
- The "Run_prediction.py": Python script used to generate predictions.

The three components described above must be placed in the same directory (i.e., the same folder) before running the prediction.
To run the prediction, users must first enter the input data into **New_Data.csv**. Each row represents one recording to be predicted, starting from Row 2. Multiple recordings can be predicted simultaneously by adding additional rows. The column names in Row 1 **must not** be modified.
The required input parameters are:
- Mw: Moment magnitude
- Event depth (km)
- ET Interface: 1 for interface; 0 otherwise
- ET Crustal: 1 for crustal; 0 otherwise
- ET Slab: 1 for slab, 0 otherwise
- FM Normal: 1 for normal fault; 0 otherwise
- FM Reverse: 1 for reverse fault; 0 otherwise
- FM Strike-slip: 1 for strike-slip; 0 otherwise
- FM Unknown: 1 for unknown fault, 0 otherwise
- Region: Volcanic-effect indicator, 1 for volcanically affected, 0 for not volcanically affected
- Rrup: Rupture distance (km)
- CS: largest shear-wave velocity contrast between adjacent layers
- Vs30: time-averaged shear-wave velocity in the upper 30 m (m/s)
- Address, Event Code, and Station Code can be left blank.

After entering all input parameters, run the **Run_prediction.py** script to generate predictions. Users should not modify the code in this script.
The prediction results will be exported to **Prediction_result.xlsx**. Results are provided in both natural logarithmic form and original units:
- Ds5-75, Ds5-95: seconds (s)
- AI, CAV, PGV: m/s
- PGA, PSA: m/s²

Example prediction: Mw = 5.8,	Event depth = 5,	ET Interface = 0,	ET Crustal = 1, ET Slab = 0, FM Normal = 0, FM Reverse = 1, FM Strike-slip = 0, FM Unknown =0,	Region = 1,	Rrup = 108.3105011,	CS = 6.67, VS30 = 716
---> ln_Ds5-75 = 2.56103038787841,	ln_Ds5-95 = 3.29772043228149,	ln_AI = -7.36018991470336,	ln_CAV = -1.34750723838806,	ln_PGA = -2.69557666778564,	ln_PGV = -5.89683818817138,...
