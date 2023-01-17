from dataPreprocessing import data_process
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import numpy as np 

def decide_model():
    label_data=data_process()

    # Assigning the featurs as X and trarget as y
    X= label_data.drop(["price"],axis =1)
    y= label_data["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state=7)

    # Building pipelins of standard scaler and model for varios regressors.

    pipeline_lr=Pipeline([("scalar1",StandardScaler()),
                        ("lr_classifier",LinearRegression())])

    pipeline_dt=Pipeline([("scalar2",StandardScaler()),
                        ("dt_classifier",DecisionTreeRegressor())])

    pipeline_rf=Pipeline([("scalar3",StandardScaler()),
                        ("rf_classifier",RandomForestRegressor())])


    pipeline_kn=Pipeline([("scalar4",StandardScaler()),
                        ("rf_classifier",KNeighborsRegressor())])


    pipeline_xgb=Pipeline([("scalar5",StandardScaler()),
                        ("rf_classifier",XGBRegressor())])

    # List of all the pipelines
    pipelines = [pipeline_lr, pipeline_dt, pipeline_rf, pipeline_kn, pipeline_xgb]

    # Dictionary of pipelines and model types for ease of reference
    pipe_dict = {0: "LinearRegression", 1: "DecisionTree", 2: "RandomForest",3: "KNeighbors", 4: "XGBRegressor"}

    # Fit the pipelines
    for pipe in pipelines:
        pipe.fit(X_train, y_train)

    #Finding RMS values for each regressor
    cv_results_rms = []
    mean_cv_score = []
    for i, model in enumerate(pipelines):
        cv_score = cross_val_score(model, X_train,y_train,scoring="neg_root_mean_squared_error", cv=10)
        cv_results_rms.append(cv_score)
        print("%s: %f " % (pipe_dict[i], cv_score.mean()))
        mean_cv_score.append(cv_score.mean())
    
    #Deciding final model
    unsorted_cv_score = mean_cv_score[:]
    mean_cv_score.sort()
    result = unsorted_cv_score.index(mean_cv_score[-1])
    model = pipe_dict[result]
    print("The best regressor is", model)
    
    # Model prediction on test data 
    if model=="XGBRegressor":
        pred = pipeline_xgb.predict(X_test)
    elif model=="KNeighbors":
        pred = pipeline_kn.predict(X_test)
    elif model=="RandomForest":
        pred = pipeline_rf.predict(X_test)
    elif model=="DecisionTree":
        pred = pipeline_dt.predict(X_test)
    elif model=="LinearRegression":
        pred = pipeline_lr.predict(X_test)
    
    # Model Evaluation
    print("The", model,"model is evaluated on test data and the results are as follows:")
    print("R^2:",metrics.r2_score(y_test, pred))
    print("Adjusted R^2:",1 - (1-metrics.r2_score(y_test, pred))*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1))
    print("MAE:",metrics.mean_absolute_error(y_test, pred))
    print("MSE:",metrics.mean_squared_error(y_test, pred))
    print("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, pred)))


decide_model()

