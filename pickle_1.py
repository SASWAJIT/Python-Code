import pickle
my_dict={1:'a',2:'b'}
pickle_file=open("picklefile.txt",'wb+')
pickle.dump(my_dict,pickle_file)
pickle_file=open("picklefile.txt",'rb+')
new_dict=pickle.load(pickle_file)
print(new_dict)