class matrix:

    def __init__(self):
        '''
        Initializes matrix object
        '''

    def formMatrix(self):
        '''
        Matrix is a list of lists (rows)
        Fills in matrix using user inputs
        '''
        self.rows = int(input("Enter number of rows: "))
        self.columns = int(input("Enter number of columns: "))
        self.completeMatrix = []
        for i in range(self.rows):
            self.completeMatrix.append([])
        print(self.completeMatrix)
        for list in self.completeMatrix:
#            print(list)
            for num in range(self.columns):
                self.num = int(input("Enter num: "))
                list.append(self.num)
#            print(list)
        print(self.completeMatrix)

    def rowReduce(self):
        '''
        Puts matrix into RREF using elementary row operations
        **ONLY FIRST COLUMN SO FAR**
        '''
#        print(self.completeMatrix[0])
#        print(self.completeMatrix[0][0])
'''First column'''
        for i in range(self.rows):
            if i == 0:
'''Makes 1,1 = 1'''
                if self.completeMatrix[0][0] != 1:
                    print('nay')
                    self.divisor = self.completeMatrix[0][0]
                    self.completeMatrix[0][0] = self.completeMatrix[0][0]/self.completeMatrix[0][0]
                    print('should be 1 \t', self.completeMatrix[0][0])
'''Divides the rest of the row'''
                    for x in self.completeMatrix[i]:
#                        print ("YOOOOOOO ",x)
                        if x != 1:
                            x = x/self.divisor
#                            print("DIVIDED: ",x)
#            print(self.completeMatrix[0][0])
#                else:
#                    print('yay')
            else:
'''kills rows
ONLY FIRST COLUMN'''
                if self.completeMatrix[i][0] != 0:
                    print(self.completeMatrix[i][0])
                    self.adder = (self.completeMatrix[0][0] * self.completeMatrix[i][0] * -1)
                    for y in range(len(self.completeMatrix[i])):
                        print("YYYYYYY ",y)
                        self.completeMatrix[i][y] = self.adder + self.completeMatrix[i][y]
                        print('\t', self.completeMatrix[i][y])
        print(self.completeMatrix)

        
#kills the rest of the row
#                    for y in self.completeMatrix[i]:
#                        if

#Makes 0,1 = 0
#ONLY FIRST COLUMN
#        if self.completeMatrix[1][0] != 0:
#            print(self.completeMatrix[1][0])
#            self.completeMatrix[1][0] = (self.completeMatrix[0][0] * self.completeMatrix[1][0] * -1) + self.completeMatrix[1][0]
#            print('should be 0 \t', self.completeMatrix[1][0])
#Makes 0,2 = 0
#ONLY FIRST COLUMN
#        if self.completeMatrix[2][0] != 0:
#            print(self.completeMatrix[2][0])
#            self.completeMatrix[2][0] = (self.completeMatrix[0][0] * self.completeMatrix[2][0] * -1) + self.completeMatrix[2][0]
#            print('should be 0 \t', self.completeMatrix[2][0])



#            self.completeMatrix[1][0] = self.completeMatrix[1][0] - self.completeMatrix[1][0]



###Need to combine rows
#        self.end = True
#        while self.end:
#            self.num = input("Enter num: ")
#Check if int
#            try:
#                self.num = int(self.num)
#If no
#            except:
#                self.end = False
#If yes
#            else:
