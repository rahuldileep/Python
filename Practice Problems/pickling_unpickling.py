import pickle
dict_pickle={'x':80,'y':90,'z':100}
pickle_out=open("dict_pickle","wb")
pickle.dump(dict_pickle,pickle_out)
pickle_out.close()

pickle_in=open("dict_pickle","rb")
dict_pickle2=pickle.load(pickle_in)
print(dict_pickle2)
