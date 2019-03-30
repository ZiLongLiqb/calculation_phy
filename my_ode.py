import numpy as np 
from scipy.integrate import odeint


def my_ode(func,begin_value,time_list):
	results=np.zeros((len(time_list),len(begin_value)))
	value=begin_value
	results[0,:]=value
	for i in range(len(time_list)-1):
		delta_t=time_list[i+1]-time_list[i]
		value1=func(value,time_list[i])
		value2=func(value+value1*delta_t/2,time_list[i]+delta_t/2)	
		value3=func(value+value2*delta_t/2,time_list[i]+delta_t/2)
		value4=func(value+value3*delta_t,time_list[i+1])
		value=value+delta_t*1/6*(value1+2*(value2+value3)+value4)
		results[i+1,:]=value
	return results

class pelunum_resist_drive(object):
	def __init__(self,theta_0=1,theta_w_0=0,time_inteval=1,resist=1,drive=1,w_0=1):
		self.theta_0=theta_0
		self.theta_w_0=theta_w_0
		self.time_inteval=time_inteval
		self.resist=resist
		self.drive=drive
		self.w_0=w_0

	def func(self,value,t):
		theta,w=value
		return np.array([w,self.drive*np.cos(self.w_0*t)-np.sin(theta)-self.resist*w])

	def Pelunum(self):
		begin_value=np.array([self.theta_0,self.theta_w_0],dtype=float)
		time_list=np.arange(0,100,self.time_inteval)
		return my_ode(self.func,begin_value,time_list)

a=pelunum_resist_drive(theta_0=0.01,resist=1/2,time_inteval=0.05,w_0=1/2,drive=0.05)
result=a.Pelunum()
print(result)
import matplotlib.pyplot as plt 
ignore=600
plt.figure()
plt.scatter(result[ignore:,0],result[ignore:,1],s=3)
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\omega$")
#plt.scatter(np.arange(0,100,0.05),result[:,0],s=1)
'''t=np.arange(0,200,0.01)
y=-1/15*np.cos(4*t)
plt.plot(t,y)'''
plt.show()