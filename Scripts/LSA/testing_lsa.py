# -*- coding: utf-8 -*-
"""test_lsa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mcl2WTPTPf68dvQWsePXAtx6cCzRPuP4
"""

# initialization
import sklearn
from __future__ import print_function
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans


import numpy
import pandas as pd
import warnings

# Document-Term matrix


# example = ["Machine learning is super fun",
# 			"Python is super,super cool",
# 			"Statistics is cool, too",
# 			"Data science is fun",
# 			"Python is great for machine learning", 
# 			"I like football",
# 			"Football is great to watch"]


example = ["Coffee brewed by expressing or forcing a small amount of nearly boiling water under pressure through finely ground coffee beans.",
            "An espresso-based coffee drink consisting of espresso with microfoam (steamed milk with small, fine bubbles with a glossy or velvety consistency)", 
            "American fast-food dish, consisting of french fries covered in cheese with the possible addition of various other toppings", 
            "Pounded and breaded chicken is topped with sweet honey, salty dill pickles, and vinegar-y iceberg slaw, then served upon crispy challah toast.", 
            "A layered, flaky texture, similar to a puff pastry.",
            "Data science is fun",
			      "Python is great for machine learning", 
			      "I like football",
		  	    "Football is great to watch","Where can I buy some ice cream","I will go shopping today to buy some groceries","I want to buy a football"
          ]

vectorizer = CountVectorizer(min_df = 1, stop_words = 'english')
dtm = vectorizer.fit_transform(example)

pd.DataFrame(dtm.toarray(), index = example, columns = vectorizer.get_feature_names()).head()

# get words for each columns or called as Bag of Word (BoW)
vectorizer.get_feature_names()

# Singular Value Decomposition SVD and LSA
lsa = TruncatedSVD(2, algorithm = 'arpack')
# type(dtm)
dtm_lsa = lsa.fit_transform(dtm.astype(float))
fig, ax = plt.subplots()
dtm_lsa = Normalizer(copy=False).fit_transform(dtm_lsa)
for i in range(dtm_lsa.shape[0]):
    ax.scatter(dtm_lsa[i, 0], dtm_lsa[i, 1], label=f'{i+1}')
ax.legend()

# dtm_lsa = Normalizer(copy = False).fit_transform(dta_lsa)
# pd.DataFrame(lsa.components_, index=["component_1","component_2"], columns=vectorizer.get_feature_names())

pd.DataFrame(lsa.components_, index = ["component_1", "component_2"], columns = vectorizer.get_feature_names() )

pd.DataFrame(dtm_lsa, index = example, columns = ["component_1", "component_2"] )

xs = [w[0] for w in dtm_lsa]
ys = [w[1] for w in dtm_lsa]
xs, ys

# plotting 
# %pylab inline
import matplotlib.pyplot as plt
figure()
plt.scatter(xs, ys)
xlabel("First Principle Component")
ylabel("Second Principle Component")
title("Plot of points against LSA principle compoenents")
show()

#Plot scatter plot of points with vectors
# %pylab inline
import matplotlib.pyplot as plt
plt.figure()
ax = plt.gca()
ax.quiver(0,0,xs,ys,angles='xy',scale_units='xy',scale=1, linewidth = .01)
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
xlabel('First principal component')
ylabel('Second principal component')
title('Plot of points against LSA principal components')
plt.draw()
plt.show()

# This code checks similarity between the "documents"
similarity = np.asarray(numpy.asmatrix(dtm_lsa) * numpy.asmatrix(dtm_lsa).T)
pd.DataFrame(similarity,index=example, columns=example).head(10)