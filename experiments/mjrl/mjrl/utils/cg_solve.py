import numpy as np

def cg_solve(f_Ax, b, x_0=None, cg_iters=10, residual_tol=1e-10, rho=None, diag_shrunk=None):
    shrunk = rho is not None and diag_shrunk is not None

    x = np.zeros_like(b) #if x_0 is None else x_0
    r = b.copy() #if x_0 is None else b-f_Ax(x_0)
    p = r.copy()
    rdotr = r.dot(r)

    for i in range(cg_iters):
        # z = f_Ax(p)
        if shrunk:
            hvp_p = (1.0 - rho) * f_Ax(p) + rho * p * diag_shrunk
        else:
            hvp_p = f_Ax(p)
        z = hvp_p

        v = rdotr / p.dot(z)
        x += v * p
        r -= v * z
        newrdotr = r.dot(r)
        mu = newrdotr / rdotr
        p = r + mu * p

        rdotr = newrdotr
        if rdotr < residual_tol:
            break

    return x
