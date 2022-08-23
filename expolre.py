import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# load the data
FD001_train = np.loadtxt('CMAPSSData/train_FD001.txt', dtype=float)
FD001_test = np.loadtxt('CMAPSSData/test_FD001.txt', dtype=float)

FD002_train = np.loadtxt('CMAPSSData/train_FD002.txt', dtype=float)
FD002_test = np.loadtxt('CMAPSSData/test_FD002.txt', dtype=float)

FD003_train = np.loadtxt('CMAPSSData/train_FD003.txt', dtype=float)
FD003_test = np.loadtxt('CMAPSSData/test_FD003.txt', dtype=float)

FD004_train = np.loadtxt('CMAPSSData/train_FD004.txt', dtype=float)
FD004_test = np.loadtxt('CMAPSSData/test_FD004.txt', dtype=float)


train = (FD001_train, FD002_train, FD003_train, FD004_train)
test = (FD001_test, FD002_test, FD003_test, FD004_test)

with PdfPages('explore.pdf') as pp:
    for j in range(4):
        fig = plt.figure()
        fig.tight_layout()
        for i in range(5, 26):
            ax = fig.add_subplot(7, 3, i-4)
            ax.scatter(train[j][:,1], train[j][:,i], s=0.5)
            ax.scatter(test[j][:,1], test[j][:,i], s=0.5)
            ax.set_xlabel('Cycle')
            ax.set_ylabel(f'Sensor{i-4}')
        pp.savefig(figure=fig)