# TO-ANN-GMM-for-Japan
This repository is used to run the TO-ANN ground-motion prediction model. It contains the following files:
- The "fold_models" folder: contains the five trained fold models and corresponding input scalers.
- The "New_Data.csv": input file for prediction.
- The "Run_prediction.py": Python script used to generate predictions.

The three components described above must be placed in the same directory (i.e., the same folder) before running the prediction.
To run the prediction, users must first enter the input data into **New_Data.csv**. Each row represents one recording to be predicted, starting from Row 2. Multiple recordings can be predicted simultaneously by adding additional rows. The column names in Row 1 **must not** be modified.
The required input parameters are:
- Mw: Moment magnitude
- Event depth (km)
- Tectonic label: 1 for Interface, 2 for Crustal, 3 for Slab
- Focal label: 1 for Normal, 2 for Reverse, 3 for Strike-slip, 4 for Unknown
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

  Example prediction: Mw = 5.2,	Event depth = 5,	Tectonic label = 2,	Focal label = 2,	Region = 0,	Rrup = 51.98894,	CS = 3.93, VS30 = 241
  ---> ln_Ds5-75 = 1.854894876,	ln_Ds5-95 = 2.868935823,	ln_AI = -5.366474152,	ln_CAV = -0.498953491,	ln_PGA = -1.62449801,	ln_PGV = -4.741275311,...
