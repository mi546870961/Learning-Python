class User():
	def __init__(self,fist_name,last_name,**info):
		self.infos={}
		self.login_attempts=0
		self.infos['fist_name']=fist_name
		self.infos['last_name']=last_name
		for key,value in info.items():
			self.infos[key]=value
	
	def describe_user(self):
		for key,value in self.infos.items():
			print(key+":"+value)
		print('')
	
	def greet_user(self):
		print("Greeting,"+self.infos['fist_name'].title()+"\n")
		
	def increment_login_attempts(self):
		self.login_attempts+=1
	
	def reset_login_attempts(self):
		self.login_attempts=0
	
	def read_login_attempts(self):
		print(self.infos['fist_name'].title()+" "+
			str(self.login_attempts)+" login attempts")
			
class Admin(User):
	def __init__(self,fist_name,last_name,**info):
		super().__init__(fist_name,last_name,**info)
		self.privileges=["can add post","can delete post","can ban user"]
	def show_privileges(self):
		print(self.infos['fist_name'].title()+" have these privileges:")
		for privilege in self.privileges:
			print(privilege)
	

user1=Admin('chen','yushen',age='27')
user2=User('zhou','mi',sex='female')
user3=User('xiao','mi',type='cat',color='white')

user1.show_privileges()
