import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, LabelEncoder, binarize
import pickle

#Read in the upsampled data
adult_all_upsampled = pd.read_csv('/content/drive/MyDrive/Team Gogurt Capstone/CA Data/adult_all_upsampled_levels.csv')

features = ['RACE - UCLA CHPR DEFINITION, UNABRIDGED (PUF 1 YR RECODE)', 'EDUCATIONAL ATTAINMENT (PUF 1 YR RECODE)',
            'RURAL AND URBAN - CLARITAS (BY CENSUS TRACT) (6 LVLS)', 'BORN IN U.S.', 'LEVEL OF ENGLISH PROFICIENCY: GENERAL ', 'SELF-REPORTED AGE (PUT 1 YR RECODE)',
            'SELF-REPORTED GENDER', 'WORKING STATUS (PUF 1 YR RECODE)','COVERED BY MEDI-CAL',
            'MARITAL STATUS- 4 CATEGORIES']

#----------Pre-processing----------

#Encoding
encoder = OrdinalEncoder()
adult_all_encoded = encoder.fit_transform(adult_all_upsampled[features])
adult_all_encoded = pd.DataFrame(adult_all_encoded, columns=features)
adult_all_encoded = pd.DataFrame(adult_all_encoded)

#1 is food secure and 0 is food insecure
adult_all_upsampled.loc[adult_all_upsampled['FOOD SECURITY STATUS (2 LVLS)'] == 'FOOD SECURITY', 'FOOD SECURITY STATUS (2 LVLS)'] = 1
adult_all_upsampled.loc[adult_all_upsampled['FOOD SECURITY STATUS (2 LVLS)'] == 'FOOD INSECURITY WITH/ WITHOUT HUNGER', 'FOOD SECURITY STATUS (2 LVLS)'] = 0
adult_all_upsampled.loc[adult_all_upsampled['FOOD SECURITY STATUS (2 LVLS)'] == 'INAPPLICABLE - >=200% FPL', 'FOOD SECURITY STATUS (2 LVLS)'] = 1

adult_all_upsampled.loc[adult_all_upsampled['SERIOUS PSYCHOLOGICAL DISTRESS'] == 'PROXY SKIPPED', 'SERIOUS PSYCHOLOGICAL DISTRESS'] = -1
adult_all_upsampled['SERIOUS PSYCHOLOGICAL DISTRESS'] = adult_all_upsampled['SERIOUS PSYCHOLOGICAL DISTRESS'].astype("float")
adult_all_encoded["SERIOUS PSYCHOLOGICAL DISTRESS"] = adult_all_upsampled["SERIOUS PSYCHOLOGICAL DISTRESS"]

#----------1st Model: Logistic Regression for Food Secure vs. Food Insecure----------

X = adult_all_encoded
y = adult_all_upsampled['FOOD SECURITY STATUS (2 LVLS)'].astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size = 0.2, stratify=y)

lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_prob = lr.predict_proba(X_test)[:,1]
y_pred_prob = y_pred_prob.reshape(1, -1)
y_pred_class = binarize(y_pred_prob, 0.82)[0]
y_pred_class = y_pred_class.astype(int)


#----------2nd Model: Multiclass XGBoost Model----------

adult_all_upsampled = pd.read_csv('/content/drive/MyDrive/Team Gogurt Capstone/CA Data/adult_all_upsampled_three_levels.csv')

X_test_negative = X_test[y_pred_class == 0]
X_test_negative.index
y_test_negative = adult_all_upsampled['FOOD SECURITY STATUS LEVEL'][X_test.index][y_pred_class == 0]

X_second = adult_all_encoded
y_second = adult_all_upsampled['FOOD SECURITY STATUS LEVEL']
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_second, y_second, test_size = 0.2, random_state=0, stratify = y_second)

multi_class_model = XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0,
              learning_rate=0.1, max_delta_step=0, max_depth=9,
              min_child_weight=1, missing=None, n_estimators=180, n_jobs=1,
              nthread=4, num_class=3, objective='multi:softprob',
              random_state=0, reg_alpha=0, reg_lambda=1, scale_pos_weight=1,
              seed=42, silent=None, subsample=1, verbosity=1)

multi_class_model.fit(X_train_2, y_train_2)
y_pred_second = multi_class_model.predict(X_test_negative)

# save the models
model_1 = 'model_1.pickle'
pickle.dump(lr, open(model_1, 'wb'))

model_2 = 'model_2.pickle'
pickle.dump(multi_class_model, open(model_2, 'wb'))