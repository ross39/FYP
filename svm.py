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


<<<<<<< HEAD
xtr,xte,ytr,yte = getEmbeddings("Data/News_Dataset/ultimate.csv")
=======
xtr,xte,ytr,yte = getEmbeddings("Data/News_Dataset#2/train.csv")
>>>>>>> 30ef7bd4361ab47f7cb94326624fc93df9dc76b5
np.save('./xtr', xtr)
np.save('./xte', xte)
np.save('./ytr', ytr)
np.save('./yte', yte)

xtr = np.load('./xtr.npy')
xte = np.load('./xte.npy')
ytr = np.load('./ytr.npy')
yte = np.load('./yte.npy')

clf = SVC()
clf.fit(xtr, ytr)
y_pred = clf.predict(xte)
m = yte.shape[0]
n = (yte != y_pred).sum()
print("Accuracy = " + format((m-n)/m*100, '.2f') + "%")   # 88.42%

plot_cmat(yte, y_pred)
