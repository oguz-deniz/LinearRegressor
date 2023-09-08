from typing import List

class LinearRegression:

    def __init__(self, learning_rate=None, epoch=None):

        self.learning_rate = learning_rate
        self.epoch = epoch
        self.m1 = 1
        self.m2 = 2
        self.b = 0
        self.loss_values = []
        self.loss_values_test = []
    
    def makePredictionTrain(self,height:List[int],weight:List[int]):
    
        preds = []

        for i in range(0,len(height)):

            pred = self.m1*height[i] + self.m2*weight[i] + self.b
            preds.append(pred)

        return preds

    def fit(self, x_train: List[int], y_train: List[int], z_train: List[int]):

        n = len(x_train)
        

        for _ in range(0,self.epoch):

            predictions = self.makePredictionTrain(x_train,y_train)

            loss = sum((predictions[i] - z_train[i])**2 for i in range(len(predictions))) / n
            self.loss_values.append(loss)


            dm1 = 0
            dm2 = 0
            dbias = 0

            for j in range(len(predictions)):

                dm1 +=  (2/n) * ((predictions[j] - z_train[j]) * x_train[j])

                dm2 +=  (2/n) * ((predictions[j] - z_train[j]) * y_train[j])

                dbias += (2/n) * (predictions[j] - z_train[j])



            self.m1 = self.m1 - self.learning_rate*dm1

            self.m2 = self.m2 - self.learning_rate*dm2

            self.b = self.b - self.learning_rate*dbias

    
        return
    
    def makePredictionTest(self,height:List[int],weight:List[int],actual:List[int]):
        
        preds2 = []
        cumulative_loss = 0

        for i in range(0,len(height)):

            pred = self.m1*(height[i]) + self.m2*(weight[i]) + self.b
            preds2.append(pred)
            error = ((pred-actual[i])**2)**1/2
            cumulative_loss += error
            average_error = cumulative_loss / (i + 1)
            self.loss_values_test.append(average_error)

        return preds2


    def predict(self, x_test: List[int],y_test:List[int]):

        heights_test = [sublist[0] for sublist in x_test]

        weights_test = [sublist[1] for sublist in x_test]


        return self.makePredictionTest(heights_test,weights_test,y_test)
       

       

