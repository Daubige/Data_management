import pandas as pd
from pathlib import Path
import os.path


# CREATION DU CSV RESULT

trial_path = "V:\\2021\\GREOUX\\PHENOMOBILE\\17IVPHENOHD_150289-149867\\"
trial_path = Path(trial_path)
print(trial_path)


for Date2 in trial_path.rglob("Session 2021*\l2"):
    print(str(Date2))
    csvs = list(Path(Date2).glob("PHENOHD*csv"))
    print(csvs)
    list_csvs = [pd.read_csv(csv, sep=";") for csv in csvs]

    try:
        os.remove(os.path.join(Date2, "Pheno_result.csv"))
    except OSError as e:
        print(e)
    else:
        print("File data is deleted successfully")

    df = pd.concat(list_csvs)

    if "Unnamed: 0" in df.columns:
        del df["Unnamed: 0"]

    df.to_csv((os.path.join(Date2, "Pheno_result.csv")), sep=";", index=False)

    print("fin concatenation")


Resultfiles = list(trial_path.glob('Session 2021*\l2\Pheno_result.csv'))
print(Resultfiles)

list_csvs_result = [pd.read_csv(csv, sep=";") for csv in Resultfiles]

try:
    os.remove(os.path.join(trial_path, "Pheno_result_Full.csv"))
except OSError as e:
    print(e)
else:
    print("File essai is deleted successfully")

df = pd.concat(list_csvs_result)

df.to_csv((os.path.join(trial_path, "Pheno_result_Full.csv")), sep=";", index=False)

