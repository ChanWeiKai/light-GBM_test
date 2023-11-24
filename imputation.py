##https://www.machinelearningplus.com/machine-learning/mice-imputation/
import pandas as pd
import miceforest as mf
data=pd.read_excel("C:/Users/kevin/Desktop/研究資料/研究資料/C_train_final2.xlsx")
data.info()
#補值
kds = mf.ImputationKernel(
  data,
  save_all_iterations=True,
  random_state=100
)
kds.mice(5)
imputed_data = kds.complete_data()
imputed_data.to_excel("C:/Users/kevin/Desktop/研究資料/研究資料/C_train_final2_imputed.xlsx", sheet_name='sheet1', index=False)

print(data.isnull().sum())
print(imputed_data.isnull().sum())