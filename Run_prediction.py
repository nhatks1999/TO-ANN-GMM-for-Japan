import numpy as np
import pandas as pd
from tensorflow import keras

NUM_FOLDS = 5
ARTIFACTS_DIR = "fold_models"
INPUT_NEW_DATA = "New_Data.csv"
OUTPUT_FILE = "Prediction_result.xlsx"

df_temp = pd.read_csv(INPUT_NEW_DATA, nrows=1)
cols_to_drop_train = list(range(0, 3)) + list(range(11, df_temp.shape[1]))
X_train_cols = df_temp.drop(df_temp.columns[cols_to_drop_train], axis=1).columns.tolist()


df_new = pd.read_csv(INPUT_NEW_DATA)
X_new_raw = df_new[X_train_cols].astype("float32")
motion_ids = df_new.iloc[:, 0].values

# Determine numeric và categorical columns
cat_cols = ["Tectonic label", "Focal label", "Region"]
num_idx = [i for i, col in enumerate(X_train_cols) if col not in cat_cols]

# PREDICTION FOR 5 FOLDS
all_fold_preds_ln = []
print("\n--- Start prediction ---")

for fold in range(1, NUM_FOLDS + 1):
    scaler_path = f"{ARTIFACTS_DIR}/scaler_fold_{fold}.csv"
    scaler_df = pd.read_csv(scaler_path)

    mean = scaler_df.iloc[0][X_train_cols].values[num_idx].astype(float)
    scale = scaler_df.iloc[1][X_train_cols].values[num_idx].astype(float)

    X_new_s = X_new_raw.values.copy()
    X_new_s[:, num_idx] = (X_new_s[:, num_idx] - mean) / scale

    model_path = f"{ARTIFACTS_DIR}/model_fold_{fold}.keras"
    model = keras.models.load_model(model_path)

    y_pred_fold_ln = model.predict(X_new_s, verbose=0)
    all_fold_preds_ln.append(y_pred_fold_ln)
    print(f"-> Finish Fold {fold}")


# RESULTS PROCESSING AND FILE EXPORT
# Average predictions of 5 folds for ln(Y)
y_final_ln = np.mean(all_fold_preds_ln, axis=0)

# Convert to Linear
y_final_linear = np.exp(y_final_ln)

target_names = ["Ds5-75", "Ds5-95", "AI", "CAV", "PGA", "PGV", "S0.010", "S0.020", "S0.022", "S0.025", "S0.029", "S0.030",
                "S0.032", "S0.035", "S0.036", "S0.040", "S0.042", "S0.044", "S0.045", "S0.046", "S0.048", "S0.050",
                "S0.055", "S0.060", "S0.065", "S0.067", "S0.070", "S0.075", "S0.080", "S0.085", "S0.090", "S0.095",
                "S0.100", "S0.110", "S0.120", "S0.130", "S0.133", "S0.140", "S0.150", "S0.160", "S0.170", "S0.180",
                "S0.190", "S0.200", "S0.220", "S0.240", "S0.250", "S0.260", "S0.280", "S0.290", "S0.300", "S0.320",
                "S0.340", "S0.350", "S0.360", "S0.380", "S0.400", "S0.420", "S0.440", "S0.450", "S0.460", "S0.480",
                "S0.500", "S0.550", "S0.600", "S0.650", "S0.667", "S0.700", "S0.750", "S0.800", "S0.850", "S0.900",
                "S0.950", "S1.000", "S1.100", "S1.200", "S1.300", "S1.400", "S1.500", "S1.600", "S1.700", "S1.800",
                "S1.900", "S2.000", "S2.200", "S2.400", "S2.500", "S2.600", "S2.800", "S3.000", "S3.200", "S3.400",
                "S3.500", "S3.600", "S3.800", "S4.000", "S4.200", "S4.400", "S4.600", "S4.800", "S5.000", "S5.500",
                "S6.000", "S6.500", "S7.000", "S7.500", "S8.000", "S8.500", "S9.000", "S9.500", "S10.000"]

df_ln = pd.DataFrame(y_final_ln, columns=[f"ln_{c}" for c in target_names])
df_linear = pd.DataFrame(y_final_linear, columns=[f"Linear_{c}" for c in target_names])

df_final = pd.DataFrame({"Address": motion_ids})
df_final = pd.concat([df_final, df_ln, df_linear], axis=1)

# Save file Excel
df_final.to_excel(OUTPUT_FILE, index=False)
print(f"\n--- SUCCESS ---")
print(f"Results saved at: {OUTPUT_FILE}")