#!/usr/bin/env python3

#program to log and display NASSP CSM/LEM/IU telemetry data


if __name__ == '__main__':
    
    import socket

    CSM = 1 
    LEM = 0

    CSMlogFileName = 'CSMtelemetryLog.txt'
    LEMlogFileName = 'LEMtelemetryLog.txt'
    ipAddress = '192.168.1.19'
    CSMport = 14242
    LEMport = 14243

    CSMlogFile = open(CSMlogFileName,'a')
    LEMlogFile = open(LEMlogFileName,'a')

    CSMlogFile.write('NEWLOG\n')
    LEMlogFile.write('NEWLOG\n')

    CSMsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    LEMsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    if CSM == 1:
        CSMsocket.connect((ipAddress, CSMport))

    if LEM == 1:
        LEMsocket.connect((ipAddress, LEMport))
    

    try:
        while True:
            if CSM == 1:
                CSMdata = CSMsocket.recv(1024)
                if not CSMdata:
                    break
            
                for ii in range(len(CSMdata)):
                    #print(CSMdata[ii])
                    CSMlogFile.write(str(CSMdata[ii]) + '\n')

            
            
            if LEM == 1:
                LEMdata = LEMsocket.recv(1024)
                if not LEMdata:
                    break

                for jj in range(len(LEMdata)):
                    #print(LEMdata[jj])
                    LEMlogFile.write(str(LEMdata[jj]) + '\n')

    except KeyboardInterrupt:
        print('Stopping Log')


    CSMlogFile.close()
    LEMlogFile.close()
    CSMsocket.close()
    LEMsocket.close()
