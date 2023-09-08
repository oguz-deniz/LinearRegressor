# Linear Regressor
This project highlights another unique implementation of mine. Basic linear regression model from scratch, providing an insightful example of one of the fundamental algorithms for regression tasks.

* **Training Error Convergence:** During the iterative update of model parameters (m1, m2, and b), I noticed that my training error, which I measure within my Linear Regression (LR) class, converged to nearly zero around the 400th epoch. This indicates that the model became increasingly accurate in predicting the training data.

     <img src="https://github.com/oguz-deniz/LinearRegressor/assets/98212476/dbeac9d6-bd72-49c0-a6f9-e638a5cb1ed2" alt="Ekran Görüntüsü (206)" width="300">

* **Test Error Measurement:** To measure test error (test loss), I calculated the average change within my LR implementation and utilized the Root Mean Square Error (RMSE) approach. As new test data arrived, I observed that the test error approached approximately 0.32. This measurement allowed me to assess the model's performance on unseen data.

* **Accuracy Calculation:** For accuracy measurement, I normalized both the training loss and test loss values within the range of 0 to 1. In line with expectations, as the training error converged to zero, the training accuracy also converged to a perfect score of 1.0. In the case of the test data, while the accuracy exhibited a more fluctuating pattern, there were noticeable improvements over time.
