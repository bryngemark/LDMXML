import pandas as pd
import numpy as np
from libDetDescr import EcalID, HcalID,EcalTriggerID
def RNN_ETS_3e(ecal_path:str, energy_path:str, tspos_path:str ,output_path:str, n:int = 1000, nc:int = 0):
    readerC = pd.read_csv(ecal_path, chunksize=n) #This assumes that the file containing the EcalIDs is too large to load into RAM if not then remove the chunking of the csv
    for chunkC in readerC:#Will iterate over the chunks of the read csv file
        nE = 0
        NRR = chunkC.shape[0]
        NC = chunkC.shape[1]
        readerE = pd.read_csv(energy_path, chunksize=n)#
        for chunkE in readerE:
            nTS = 0
            if nE<nc:
                nE = nE+1
                continue
            elif nE>nc:
                break
            elif nE==nc:
                readerTS = pd.read_csv(tspos_path, chunksize=n)#Once again assuming that the TS file is too large
                for chunkTS in readerTS:
                    if nTS<nc:
                        nTS = nTS+1
                        continue
                    elif nTS>nc:
                        break
                    elif nTS == nc and nTS == nE:
                        if nc==0:
                            for j in range(n):
                                B = np.zeros(shape = (363))
                                Y1 = int(chunkTS['{}'.format('Y1')][j])
                                Y2 = int(chunkTS['{}'.format('Y2')][j])
                                Y3 = int(chunkTS['{}'.format('Y3')][j])
                                if Y1 == Y3 and Y1==Y2:
                                    B[0] = (Y1*1000+1)
                                    B[1] = 0
                                    B[2] = 0
                                elif Y3==Y2:
                                    B[0] = (Y1*1000+1)
                                    B[1] = (Y2*1000+1)
                                    B[2] = 0
                                elif Y1==Y2:
                                    B[0] = (Y2*1000+1)
                                    B[1] = 0
                                    B[2] = (Y3*1000+1)
                                elif Y1==Y3:
                                    B[0] = (Y1*1000+1)
                                    B[1] = (Y2*1000+1)
                                    B[2] = 0
                                else:
                                    B[0] = (Y1*1000+1)
                                    B[1] = (Y2*1000+1)
                                    B[2] = (Y3*1000+1)
                                for i in range(360):
                                    D = chunkC['{}'.format(i)][j]
                                    if pd.isna(D) == False and pd.isna(chunkE['{}'.format(i)][j])==False:
                                                DD = int(D)
                                                C = EcalID(DD).cell()
                                                M = EcalID(DD).module()
                                                L = EcalID(DD).layer()
                                                B[i+3] = (L+1)*10000000+1000000*(M)+1000*C+chunkE['{}'.format(i)][j]
                                B = np.array(B)
                                np.savez_compressed(output_path + '3e{}.npz'.format(nc), B)#Saves the array to a file named for example 1e1.npz in the NPZ file format.
                        elif NRR <n:
                            for j in range(nc*n,nc*n+NRR):
                                B = np.zeros(shape = (363))
                                Y1 = int(chunkTS['{}'.format('Y1')][j])
                                Y2 = int(chunkTS['{}'.format('Y2')][j])
                                Y3 = int(chunkTS['{}'.format('Y3')][j])
                                if Y1 == Y3 and Y1==Y2:
                                    B[0] = (Y1*1000+1)
                                    B[1] = 0
                                    B[2] = 0
                                elif Y3==Y2:
                                    B[0] = (Y1*1000+1)
                                    B[1] = (Y2*1000+1)
                                    B[2] = 0
                                elif Y1==Y2:
                                    B[0] = (Y2*1000+1)
                                    B[1] = 0
                                    B[2] = (Y3*1000+1)
                                elif Y1==Y3:
                                    B[0] = (Y1*1000+1)
                                    B[1] = (Y2*1000+1)
                                    B[2] = 0
                                else:
                                    B[0] = (Y1*1000+1)
                                    B[1] = (Y2*1000+1)
                                    B[2] = (Y3*1000+1)
                                for i in range(360):
                                    D = chunkC['{}'.format(i)][j]
                                    if pd.isna(D) == False and pd.isna(chunkE['{}'.format(i)][j])==False:
                                                DD = int(D)
                                                C = EcalID(DD).cell()
                                                M = EcalID(DD).module()
                                                L = EcalID(DD).layer()
                                                B[i+3] = (L+1)*10000000+1000000*(M)+1000*C+chunkE['{}'.format(i)][j]
                                B = np.array(B)
                                np.savez_compressed(output_path + '3e{}.npz'.format(nc), B)
                        else:
                            for j in range(nc*NRR,(nc+1)*NRR):
                                B = np.zeros(shape = (363))
                                Y1 = int(chunkTS['{}'.format('Y1')][j])
                                Y2 = int(chunkTS['{}'.format('Y2')][j])
                                Y3 = int(chunkTS['{}'.format('Y3')][j])
                                if Y1 == Y3 and Y1==Y2:
                                    B[0] = (Y1*1000+1)
                                    B[1] = 0
                                    B[2] = 0
                                elif Y3==Y2:
                                    B[0] = (Y1*1000+1)
                                    B[1] = (Y2*1000+1)
                                    B[2] = 0
                                elif Y1==Y2:
                                    B[0] = (Y2*1000+1)
                                    B[1] = 0
                                    B[2] = (Y3*1000+1)
                                elif Y1==Y3:
                                    B[0] = (Y1*1000+1)
                                    B[1] = (Y2*1000+1)
                                    B[2] = 0
                                else:
                                    B[0] = (Y1*1000+1)
                                    B[1] = (Y2*1000+1)
                                    B[2] = (Y3*1000+1)
                                for i in range(360):
                                    D = chunkC['{}'.format(i)][j]
                                    if pd.isna(D) == False and pd.isna(chunkE['{}'.format(i)][j])==False:
                                                DD = int(D)
                                                C = EcalID(DD).cell()
                                                M = EcalID(DD).module()
                                                L = EcalID(DD).layer()
                                                B[i+3] = (L+1)*10000000+1000000*(M)+1000*C+chunkE['{}'.format(i)][j]
                                B = np.array(B)
                                np.savez_compressed(output_path + '3e{}.npz'.format(nc), B)
                        nTS = nTS+1
                nE = nE+1
        nc = nc+1