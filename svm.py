from clean import getEmbeddings
import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import scikitplot.plotters as skplt


#Need to generate the train/test split for the combined news dataset
#train_test_split("Data/News_Dataset/combined_news.csv")

def plot_cmat(yte, ypred):
    '''Plotting confusion matrix'''
    skplt.plot_confusion_matrix(yte,ypred)
    plt.show()


xtr,xte,ytr,yte = getEmbeddings("Data/News_Dataset/ultimate.csv")
np.save('./xtr', xtr)
np.save('./xte', xte)
np.save('./ytr', ytr)
np.save('./yte', yte)

xtr = np.load('./xtr.npy', allow_pickle = True)
xte = np.load('./xte.npy', allow_pickle = True)
ytr = np.load('./ytr.npy', allow_pickle = True)
yte = np.load('./yte.npy', allow_pickle = True)

clf = SVC()
clf.fit(xtr, ytr)
y_pred = clf.predict(xte)
m = yte.shape[0]
n = (yte != y_pred).sum()
print("Accuracy = " + format((m-n)/m*100, '.2f') + "%")   # 88.42%

plot_cmat(yte, y_pred)
