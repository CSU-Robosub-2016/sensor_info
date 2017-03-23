class getSensoryData():
    def __init__(self):
        # self.dataFromImu = [0] * 21
        # self.dataFromVison = [0] * 6
        # self.dataFromPressure = [0] * 2
        self.allData = [0] * 29

    def upDateData(self, imuData=[0]*21):
        self.allData[0] = imuData[0]
        self.allData[1] = imuData[1]
        self.allData[2] = imuData[2]
        self.allData[3] = imuData[3]
        self.allData[4] = imuData[4]
        self.allData[5] = imuData[5]
        self.allData[6] = imuData[6]
        self.allData[7] = imuData[7]
        self.allData[8] = imuData[8]
        self.allData[9] = imuData[9]
        self.allData[10] = imuData[10]
        self.allData[12] = imuData[12]
        self.allData[13] = imuData[13]
        self.allData[14] = imuData[14]
        self.allData[15] = imuData[15]
        self.allData[16] = imuData[16]
        self.allData[17] = imuData[17]
        self.allData[18] = imuData[18]
        self.allData[19] = imuData[19]
        self.allData[20] = imuData[20]

    def upDatePressureData(self, pressureData=[0]*2):
        self.allData[21] = pressureData[0]
        self.allData[22] = pressureData[1]

    def upDateVisionData(self, visonData=[0]*5):
        self.allData[23] = visonData[0]
        self.allData[24] = visonData[1]
        self.allData[25] = visonData[2]
        self.allData[26] = visonData[3]
        self.allData[27] = visonData[4]
        self.allData[28] = visonData[5]

    def getAllData(self):
        return self.allData
