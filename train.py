import numpy as np
import csv
import sys

from validate import validate

"""
Predicts the target values for data in the file at 'test_X_file_path', using the weights learned during training.
Writes the predicted values to the file named "predicted_test_Y_lr.csv". It should be created in the same directory where this code file is present.
This code is provided to help you get started and is NOT a complete implementation. Modify it based on the requirements of the project.
"""

def import_data_and_weights(test_X_file_path, weights_file_path):
    test_X = np.genfromtxt(test_X_file_path, delimiter=',', dtype=np.float64, skip_header=1)
    #print(test_X)
    weights = np.genfromtxt(weights_file_path, delimiter=',', dtype=np.float64)
    #print(weights)
    
    return test_X, weights


def predict_target_values(test_X, weights):
    # Write your code to Predict Target Variables
    # HINT: You can use other functions which you've already implemented in coding assignments.
    ones=np.ones(len(test_X))
    test_X=np.insert(test_X,0,ones,axis=1)
    theta=np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(test_X),test_X)),np.transpose(test_X)),weights)
    print(theta)
    return theta
    pass

def write_to_csv_file(pred_Y, predicted_Y_file_name):
    print(pred_Y)
    pred_Y = pred_Y.reshape(len(pred_Y), 1)
    print(pred_Y)
    with open(predicted_Y_file_name, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerows(pred_Y)
        csv_file.close()


def predict(test_X_file_path):
    test_X, weights = import_data_and_weights(test_X_file_path,"train_Y_lr.csv")
    pred_Y = predict_target_values(test_X, weights)
    write_to_csv_file(pred_Y, "WEIGHTS_FILE.csv")


if __name__ == "__main__":
    test_X_file_path='train_X_lr.csv'
    #print(test_X_file_path)
    predict(test_X_file_path)
    # Uncomment to test on the training data
    #validate(test_X_file_path, actual_test_Y_file_path="train_Y_lr.csv") 
