import os

#############可用&按原顺序命名##############输出filerename.txt为对应关系##############

path='/home/dl/zds/back/algorithm/ssd-pytorch-master/logs'
file_1=[file[:-4] for file in os.listdir(path) if file[-4:]=='.pth']
for index , name  in enumerate(file_1):
    file_1[index]=str(name)
file_2=sorted(file_1)
i=5
for file in file_2:
    if len(str(file))<300:
        #newname='%05d'%(i)+'.pth'  ###左补0形成五位
        newname='%s'%(str(i))+'.pth'
        i+=5
        os.rename(os.path.join(path,str(file)+'.pth'),os.path.join(path,newname))
        with open('filerename.txt','a') as f:
            f.write(str(file)+'>>>>>>>>>>>>>>'+newname+'\n')
            f.close

#############可用&按原顺序命名##############输出filerename.txt为对应关系##############
