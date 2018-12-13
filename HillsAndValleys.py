# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    def checkForHillsAndValleys(P,Q,A):

        P_VALID_HILL = False
        Q_VALID_HILL = False

        P_VALID_VALLEY = False
        Q_VALID_VALLEY = False

        if P-1 < 0:
            P_VALID_HILL = True
            P_VALID_VALLEY = True
        elif A[P] < A[P-1]:
            P_VALID_VALLEY = True
        elif A[P] > A[P-1]:
            P_VALID_HILL = True

        if Q+1 > len(A)-1:
            Q_VALID_HILL = True
            Q_VALID_VALLEY = True
        elif A[Q] < A[Q+1]:
            Q_VALID_VALLEY = True
        elif A[Q] > A[Q+1]:
            Q_VALID_HILL = True



    
        VALID_HILL = P_VALID_HILL and Q_VALID_HILL
        VALID_VALLEY = P_VALID_VALLEY and Q_VALID_VALLEY

        return (VALID_HILL or VALID_VALLEY)
    
    def iterate(A,runningPCount, currentP):
        
        if(currentP < len(A)-1):
            if(A[currentP] == A[currentP+1]):
                runningPCount += 1
                currentP += 1
                iterate(A,runningPCount, currentP)
            return runningPCount, currentP
        else:
             return(runningPCount, currentP)   
        
    
    def getNextSegment(A, runningPCount,currentP, validCount):

            

            runningPCount, currentQ = iterate(A,runningPCount,currentP)
            
            if(checkForHillsAndValleys(currentP,currentQ,A)):
                validCount += 1
            
            #print(currentP,currentQ, A[currentP], A[currentQ])
            if(currentQ < len(A)-1):
                validCount = getNextSegment(A,runningPCount, currentQ+1, validCount)

            return validCount

        
        
            
        
    vc = getNextSegment(A, 0, 0, 0)
    print(vc)
    
   return vc


A =  [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]

solution(A)

