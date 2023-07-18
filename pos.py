from models import User
from random import SystemRandom
g=5
p=2000000579

def verify(curr_user,current_owner, property_chosen,z,u,c,a):

    if a==0:
        gen=SystemRandom()
        c=gen.randrange(p)
        return c
    else:
        if((pow(g,z,p)==(u*pow(curr_user.h,c,p))%p) and curr_user.wealth >= property_chosen.amount):
            return True
        else:
            return False


def comm(u,r,c,x,a):

    
    if a==0:
        gen=SystemRandom()
        r=gen.randrange(p)
        
        u=pow(g,r,p)
        return {u,r}

    else:
        
        z=r+c*x
        return z
       
        # if verify(curr_user, z, current_owner, property_chosen,1):


def find_pos(curr_user, current_owner, property_chosen):
    
    leader = None
    balance = -1
    for user in User.users:
        if user.wealth >= balance:
            balance = user.wealth
            leader = user
    u,r=comm(0,0,0,0,0)
    c=verify(curr_user,current_owner, property_chosen,0,0,0,0)
    z=comm(u,r,c,curr_user.x,1)
    if verify(curr_user,current_owner, property_chosen,z,u,c,1):
        return leader
    else:
        return -1





