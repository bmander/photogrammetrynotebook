import numpy as np

def make_rotation_matrix(alpha,beta,gamma):
    A_x = np.array([[1,0,0],
                    [0,np.cos(alpha),-np.sin(alpha)],
                    [0,np.sin(alpha),np.cos(alpha)]])
    A_y = np.array([[np.cos(beta),0,np.sin(beta)],
                    [0,1,0],
                    [-np.sin(beta),0,np.cos(beta)]])
    A_z = np.array([[np.cos(gamma),-np.sin(gamma),0],
                    [np.sin(gamma),np.cos(gamma),0],
                    [0,0,1]])

    A = np.dot( np.dot(A_x,A_y), A_z )
    
    return A