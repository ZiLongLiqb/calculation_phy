#CTRL+b可以直接运行
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

class pendulum(object):
	def __init__(self):
		self.theta0=1
		self.v0=0
		self.time_step=0.02
		self.time_begin=0
		self.time_end=100
		self.a=1
		self.b=1

	def func(self,w,t):
		theta,v=w
		return np.array([v,-self.b/self.a*np.sin(theta)])

	def generate(self):
		self.time=np.arange(self.time_begin,self.time_end,self.time_step)
		self.track=odeint(self.func,(self.theta0,self.v0),self.time)

class pendulum_resist(object):
	def __init__(self):
		self.theta0=1
		self.v0=0
		self.time_step=0.2
		self.time_begin=0
		self.time_end=1000
		self.a=1
		self.b=1
		self.c=1

	def func(self,w,t):
		theta,v=w
		return np.array([v,-self.b/self.a*v-self.c/self.a*np.sin(theta)])

	def generate(self):
		self.time=np.arange(self.time_begin,self.time_end,self.time_step)
		self.track=odeint(self.func,(self.theta0,self.v0),self.time)

class pendulum_resist_drive(object):
	def __init__(self):
		self.theta0=1
		self.v0=0.1
		self.time_step=0.05
		self.time_begin=0
		self.time_end=4000
		self.a=2
		self.b=1
		self.c=2
		self.A0=1

	def func(self,w,t):
		theta,v=w
		return np.array([v,-self.b/self.a*v-self.c/self.a*np.sin(theta)+self.A0*np.cos(2/3*t)])

	def generate(self):
		self.time=np.arange(self.time_begin,self.time_end,self.time_step)
		self.track=odeint(self.func,(self.theta0,self.v0),self.time)

p=pendulum_resist_drive()
p.A0=1.7
p.generate()
plt.figure()
discard=3000
t=np.arange(0,4000,0.05)
plt.plot(t[discard:],p.track[:,1][discard:])
plt.figure()
plt.title("p.A0=")
#plt.gca().set_aspect(1)
plt.subplot(221)
plt.plot(p.track[:,0][discard:],p.track[:,1][discard:],'c')
plt.xlabel("theta")
plt.ylabel("v")
plt.subplot(222)
plt.xlabel("t")
plt.ylabel("theta")
plt.plot(t[discard:],p.track[:,0][discard:],'c')
#plt.xlim(0,500)
plt.subplot(223)
plt.xlim(0,1000)
plt.xlabel("f")
plt.ylabel("amplitude")
trans=np.fft.fft(p.track[:,1][discard:])
N=int(len(trans)/2)+1
plt.plot(np.abs(trans[:N])/N*2,'c')
plt.subplot(224)
trans1=np.fft.fft(p.track[:,0][discard:])
N=int(len(trans1)/2)+1
plt.plot(np.abs(trans1[:N])/N*2,'c')
plt.xlim(0,1000)
plt.show()

def f(begin,end,step):
	A=np.arange(begin,end,step)
	discard=1000
	bins=len(A)
	data=np.zeros((bins,(len(np.arange(0,300,0.05))-discard),3))
	for k in range(bins):
		p=pendulum_resist_drive()
		p.A0=A[k]
		p.generate()
		data[k,:,0]=A[k]
		data[k,:,1]=p.track[:,0][discard:]
		data[k,:,2]=p.track[:,1][discard:]
	data=data.reshape(bins*(len(np.arange(0,300,0.05))-discard),3)
	fig=plt.figure()
	ax=Axes3D(fig)
	ax.plot(data[:,0],data[:,1],data[:,2],".")
	plt.show()
	plt.figure()
	plt.plot(data[:,0],data[:,1],".")
	plt.show()

#f(0.5,2.0,0.05)
