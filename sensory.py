class getSensoryData():
    ##
    # @breif Defines incoming variables.
    def __init__(self):
        # self.dataFromImu = [0] * 21
        # self.dataFromVison = [0] * 6
        # self.dataFromPressure = [0] * 2
        self.allData = [0] * 29
    
    ##
    # @brief Updates filtered IMU Data, x is forward/back, y left/right, z up/down
    def upDateData(self, imuData=[0]*21):
        self.allData[0] = imuData[0] #x-direction acceleration
        self.allData[1] = imuData[1] #y-direction acceleration
        self.allData[2] = imuData[2] #z-direction acceleration
        self.allData[3] = imuData[3] #x-direction velocity
        self.allData[4] = imuData[4] #y-direction velocity
        self.allData[5] = imuData[5] #z-direction velocity
        self.allData[6] = imuData[6] #x-direction position
        self.allData[7] = imuData[7] #y-direction position
        self.allData[8] = imuData[8] #z-direction position
        self.allData[9] = imuData[9] #x-axis rotation
        self.allData[10] = imuData[10] #y-axis rotation
        self.allData[10] = imuData[10] #z-axis rotation
        self.allData[12] = imuData[12] #x-axis rotation velocity
        self.allData[13] = imuData[13] #y-axis rotation velocity
        self.allData[14] = imuData[14] #z-axis rotation velocity
        self.allData[15] = imuData[15] #x-axis rotation acceleration
        self.allData[16] = imuData[16] #y-axis rotation acceleration
        self.allData[17] = imuData[17] #z-axis rotation acceleration
        self.allData[18] = imuData[18] #x-direction magnetic
        self.allData[19] = imuData[19] #y-direction magnetic
        self.allData[20] = imuData[20] #z-direction magnetic
        
    ##
    # @brief Updates pressure sensor data, read in PSI
    def upDatePressureData(self, pressureData=[0]*2):
        self.allData[21] = pressureData[0] #Pressure sensor 1 Pascal
        self.allData[22] = pressureData[1] #Pressure sensor 2 Pascal
        
    ##
    # @brief Makes yes / no based on camera readings, 1 for yes, 0 for no
    def upDateVisionData(self, visonData=[0]*5):
        self.allData[23] = visonData[0] # Up yes/no
        self.allData[24] = visonData[1] # Down yes/no
        self.allData[25] = visonData[2] # Left yes/no
        self.allData[26] = visonData[3] # Right yes/no
        self.allData[27] = visonData[4] # Forward yes/no
        self.allData[28] = visonData[5] # Back yes/no

    def getAllData(self):
        return self.allData
