#!/usr/bin/env python3

#program to log and display NASSP CSM/LEM/IU telemetry data


if __name__ == '__main__':
    
    import socket

    CSM = 1 
    LEM = 1

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

    CSMsocket.connect((ipAddress, CSMport))
    LEMsocket.connect((ipAddress, LEMport))

    try:

        while True:
            if CSM == 1:
                CSMdata = CSMsocket.recv(1024)
                if not CSMdata:
                    break
        
                CSMbuffer = memoryview(CSMdata).cast('B')
        
                for ii in CSMbuffer:
                    CSMlogFile.write(CSMbuffer[ii] + '\n')

            if LEM == 1:
                LEMdata = LEMsocket.recv(1024)
                if not LEMdata:
                    break

                LEMbuffer = memoryview(LEMdata).cast('B')

                for jj in LEMbuffer:
                    LEMlogFile.write(CSMbuffer[jj] + '\n')

    except KeyboardInterupt:

        CSMlogFile.close()
        LEMlogFile.close()

        CSMsocket.close()
        LEMsocket.close()


