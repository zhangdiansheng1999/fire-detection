import os
import matplotlib.pyplot as plt
import numpy as np

def plt_auto(confidence_path, threhold_confidence):	
	threhold_confidence = str(threhold_confidence)
	png_path = os.path.join(confidence_path,threhold_confidence)
	APfile = os.path.join(confidence_path, 'AP.txt')
	F1file = os.path.join(confidence_path, 'F1.txt')
	Recallfile = os.path.join(confidence_path, 'Recall.txt')
	Precisionfile = os.path.join(confidence_path, 'Precision.txt')
	variate,fire,smoke,mAP = [],[],[],[]
	a,b,c = [],[],[]
	d,e,f = [],[],[]
	g,h,i = [],[],[]
	with open(APfile, 'r') as APf:
	    lines = APf.readlines()#2
	    for line in lines:#3
	        value = [float(s) for s in line.split()]#4
	        variate.append(value[0])
	        fire.append(value[1])#5
	        smoke.append(value[2])
	        mAP.append(value[3])
	    print(variate)        
	    print(fire)
	    print(smoke)
	    print(mAP)

	    plt.figure()
	    plt.plot(variate,fire,label='fire')
	    plt.plot(variate,smoke,label='smoke',color="red",linewidth=1.0)
	    plt.plot(variate,mAP,label='mAP',color="green",linewidth=1.0,linestyle='dotted')
	    plt.title("AP_" + threhold_confidence)
	    plt.legend()	   

	#     #标记fire的最大值和最小值点
	#     fire_min=np.argmin(fire)
	#     fire_max=np.argmax(fire)
	#     show_min='['+str(fire_min)+' '+str(fire[fire_min])+']'
	#     show_max='['+str(fire_max)+' '+str(fire[fire_max])+']'        
	#     plt.plot(fire_min,fire[fire_min],'ko') 
	#     plt.plot(fire_max,fire[fire_max],'ko') 
	#     plt.annotate(show_min,xy=(fire_min,fire[fire_min]),xytext=(fire_min,fire[fire_min]))
	#     plt.annotate(show_max,xy=(fire_max,fire[fire_max]),xytext=(fire_max,fire[fire_max]))

	#     #标记smoke的最大值和最小值点
	#     smoke_min=np.argmin(smoke)
	#     smoke_max=np.argmax(smoke)
	#     show_min='['+str(smoke_min)+' '+str(smoke[smoke_min])+']'
	#     show_max='['+str(smoke_max)+' '+str(smoke[smoke_max])+']'        
	#     plt.plot(smoke_min,smoke[smoke_min],'ko') 
	#     plt.plot(smoke_max,smoke[smoke_max],'ko') 
	#     plt.annotate(show_min,xy=(smoke_min,smoke[smoke_min]),xytext=(smoke_min,smoke[smoke_min]))
	#     plt.annotate(show_max,xy=(smoke_max,smoke[smoke_max]),xytext=(smoke_max,smoke[smoke_max]))

	#     #标记mAP的最大值和最小值点
	#     mAP_min=np.argmin(mAP)
	#     mAP_max=np.argmax(mAP)
	#     show_min='['+str(mAP_min)+' '+str(mAP[mAP_min])+']'
	#     show_max='['+str(mAP_max)+' '+str(mAP[mAP_max])+']'        
	#     plt.plot(mAP_min,mAP[mAP_min],'ko') 
	#     plt.plot(mAP_max,mAP[mAP_max],'ko') 
	#     plt.annotate(show_min,xy=(mAP_min,mAP[mAP_min]),xytext=(mAP_min,mAP[mAP_min]))
	#     plt.annotate(show_max,xy=(mAP_max,mAP[mAP_max]),xytext=(mAP_max,mAP[mAP_max]))
	    plt.savefig(png_path + "AP.png")


	with open(F1file, 'r') as F1f:
	    lines = F1f.readlines()#2
	    for line in lines:#3
	        value = [float(s) for s in line.split()]#4
	        a.append(value[0])
	        b.append(value[1])#5
	        c.append(value[2])
	        



	    plt.figure()
	    plt.plot(a,b,label='fire')
	    plt.plot(a,c,label='smoke',color="red",linewidth=1.0)
	    plt.title("F1_" + threhold_confidence)
	    plt.legend()	   

	#     #标记fire的最大值和最小值点
	#     fire_min=np.argmin(fire)
	#     fire_max=np.argmax(fire)
	#     show_min='['+str(fire_min)+' '+str(fire[fire_min])+']'
	#     show_max='['+str(fire_max)+' '+str(fire[fire_max])+']'        
	#     plt.plot(fire_min,fire[fire_min],'ko') 
	#     plt.plot(fire_max,fire[fire_max],'ko') 
	#     plt.annotate(show_min,xy=(fire_min,fire[fire_min]),xytext=(fire_min,fire[fire_min]))
	#     plt.annotate(show_max,xy=(fire_max,fire[fire_max]),xytext=(fire_max,fire[fire_max]))

	#     #标记smoke的最大值和最小值点
	#     smoke_min=np.argmin(smoke)
	#     smoke_max=np.argmax(smoke)
	#     show_min='['+str(smoke_min)+' '+str(smoke[smoke_min])+']'
	#     show_max='['+str(smoke_max)+' '+str(smoke[smoke_max])+']'        
	#     plt.plot(smoke_min,smoke[smoke_min],'ko') 
	#     plt.plot(smoke_max,smoke[smoke_max],'ko') 
	#     plt.annotate(show_min,xy=(smoke_min,smoke[smoke_min]),xytext=(smoke_min,smoke[smoke_min]))
	#     plt.annotate(show_max,xy=(smoke_max,smoke[smoke_max]),xytext=(smoke_max,smoke[smoke_max]))
	    plt.savefig(png_path + "F1.png")


	with open(Recallfile, 'r') as Recallf:
	    lines = Recallf.readlines()#2
	    for line in lines:#3
	        value = [float(s) for s in line.split()]#4
	        d.append(value[0])
	        e.append(value[1])#5
	        f.append(value[2])
	        

	    plt.figure()
	    plt.plot(d,e,label='fire')
	    plt.plot(d,f,label='smoke',color="red",linewidth=1.0)
	    plt.title("Recall_" + threhold_confidence)
	    plt.legend()	   

	    # #标记fire的最大值和最小值点
	    # fire_min=np.argmin(fire)
	    # fire_max=np.argmax(fire)
	    # show_min='['+str(fire_min)+' '+str(fire[fire_min])+']'
	    # show_max='['+str(fire_max)+' '+str(fire[fire_max])+']'        
	    # plt.plot(fire_min,fire[fire_min],'ko') 
	    # plt.plot(fire_max,fire[fire_max],'ko') 
	    # plt.annotate(show_min,xy=(fire_min,fire[fire_min]),xytext=(fire_min,fire[fire_min]))
	    # plt.annotate(show_max,xy=(fire_max,fire[fire_max]),xytext=(fire_max,fire[fire_max]))

	    # #标记smoke的最大值和最小值点
	    # smoke_min=np.argmin(smoke)
	    # smoke_max=np.argmax(smoke)
	    # show_min='['+str(smoke_min)+' '+str(smoke[smoke_min])+']'
	    # show_max='['+str(smoke_max)+' '+str(smoke[smoke_max])+']'        
	    # plt.plot(smoke_min,smoke[smoke_min],'ko') 
	    # plt.plot(smoke_max,smoke[smoke_max],'ko') 
	    # plt.annotate(show_min,xy=(smoke_min,smoke[smoke_min]),xytext=(smoke_min,smoke[smoke_min]))
	    # plt.annotate(show_max,xy=(smoke_max,smoke[smoke_max]),xytext=(smoke_max,smoke[smoke_max]))
	    plt.savefig(png_path + "Recallf.png")


	with open(Precisionfile, 'r') as Precisionf:
	    lines = Precisionf.readlines()#2
	    for line in lines:#3
	        value = [float(s) for s in line.split()]#4
	        g.append(value[0])
	        h.append(value[1])#5
	        i.append(value[2])
	        

	    plt.figure()
	    plt.plot(g,h,label='fire')
	    plt.plot(g,i,label='smoke',color="red",linewidth=1.0)
	    plt.title("Precision_" + threhold_confidence)
	    plt.legend()	   

	    # #标记fire的最大值和最小值点
	    # fire_min=np.argmin(fire)
	    # fire_max=np.argmax(fire)
	    # show_min='['+str(fire_min)+' '+str(fire[fire_min])+']'
	    # show_max='['+str(fire_max)+' '+str(fire[fire_max])+']'        
	    # plt.plot(fire_min,fire[fire_min],'ko') 
	    # plt.plot(fire_max,fire[fire_max],'ko') 
	    # plt.annotate(show_min,xy=(fire_min,fire[fire_min]),xytext=(fire_min,fire[fire_min]))
	    # plt.annotate(show_max,xy=(fire_max,fire[fire_max]),xytext=(fire_max,fire[fire_max]))

	    # #标记smoke的最大值和最小值点
	    # smoke_min=np.argmin(smoke)
	    # smoke_max=np.argmax(smoke)
	    # show_min='['+str(smoke_min)+' '+str(smoke[smoke_min])+']'
	    # show_max='['+str(smoke_max)+' '+str(smoke[smoke_max])+']'        
	    # plt.plot(smoke_min,smoke[smoke_min],'ko') 
	    # plt.plot(smoke_max,smoke[smoke_max],'ko') 
	    # plt.annotate(show_min,xy=(smoke_min,smoke[smoke_min]),xytext=(smoke_min,smoke[smoke_min]))
	    # plt.annotate(show_max,xy=(smoke_max,smoke[smoke_max]),xytext=(smoke_max,smoke[smoke_max]))
	    plt.savefig(png_path + "Precision.png")





