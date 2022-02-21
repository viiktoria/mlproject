import seaborn as sns
from sklearn.datasets import make_blobs
def hello_world():
    return "Hello world from mlproject"


def try_me():
    X, y = make_blobs(n_samples=2000, centers=5, n_features=6, random_state=6)
    scatter = sns.scatterplot(x = X[:,0],y = X[:,1], c=y)
    print('scatter')
    return scatter
