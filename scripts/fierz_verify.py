import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=140)

# ---------- Euclidean gamma matrices (hermitian, chiral rep) ----------
s0=np.eye(2); s1=np.array([[0,1],[1,0]],dtype=complex)
s2=np.array([[0,-1j],[1j,0]]); s3=np.array([[1,0],[0,-1]],dtype=complex)
def kron(a,b): return np.kron(a,b)
# gamma_mu hermitian, {gmu,gnu}=2delta
g=[None]*5
g[1]=kron(s1,s1*0+np.array([[0,1],[1,0]]))  # placeholder; build canonical set below
# canonical Euclidean chiral: gamma_i = [[0, -i sigma_i],[i sigma_i, 0]], gamma_4=[[0,1],[1,0]]
def blk(a,b,c,d): return np.block([[a,b],[c,d]])
Z=np.zeros((2,2),dtype=complex)
g[1]=blk(Z,-1j*s1,1j*s1,Z)
g[2]=blk(Z,-1j*s2,1j*s2,Z)
g[3]=blk(Z,-1j*s3,1j*s3,Z)
g[4]=blk(Z,s0,s0,Z)
g5=g[1]@g[2]@g[3]@g[4]
# checks
for mu in range(1,5):
    for nu in range(1,5):
        assert np.allclose(g[mu]@g[nu]+g[nu]@g[mu], 2*(mu==nu)*np.eye(4)), (mu,nu)
    assert np.allclose(g[mu].conj().T, g[mu])
assert np.allclose(g5.conj().T, g5) and np.allclose(g5@g5, np.eye(4))

# ---------- hermitian orthonormal 16-element basis ----------
basis=[('S', np.eye(4))]
basis.append(('P', g5))
for mu in range(1,5): basis.append((f'V{mu}', g[mu]))
for mu in range(1,5): basis.append((f'A{mu}', 1j*g[mu]@g5))
Tlabels=[]
for mu in range(1,5):
    for nu in range(mu+1,5):
        basis.append((f'T{mu}{nu}', 1j*(g[mu]@g[nu]-g[nu]@g[mu])/2))
for lab,B in basis:
    assert np.allclose(B.conj().T, B), lab
    assert abs(np.trace(B@B)-4)<1e-12, (lab, np.trace(B@B))
for i,(la,Ba) in enumerate(basis):
    for j,(lb,Bb) in enumerate(basis):
        assert abs(np.trace(Ba@Bb) - 4*(i==j))<1e-12

# ---------- completeness: sum_A (B_A)_ij (B_A)_kl = 4 d_il d_kj ----------
Ssum=np.zeros((4,4,4,4),dtype=complex)
for lab,B in basis:
    Ssum += np.einsum('ij,kl->ijkl', B, B)
target=np.zeros_like(Ssum)
for i in range(4):
    for j in range(4):
        target[i,j,j,i]=4
print("completeness (hermitian orthonormal basis):", np.allclose(Ssum,target))

# ---------- the paper's basis {1, i g5, g_mu, g_mu g5, sigma_mu_nu} ----------
paper=[('S', np.eye(4)), ('P_ig5', 1j*g5)]
for mu in range(1,5): paper.append((f'V{mu}', g[mu]))
for mu in range(1,5): paper.append((f'A{mu}_gg5', g[mu]@g5))
for mu in range(1,5):
    for nu in range(mu+1,5):
        paper.append((f'T{mu}{nu}', 1j*(g[mu]@g[nu]-g[nu]@g[mu])/2))
Ppsum=np.zeros((4,4,4,4),dtype=complex)
for lab,B in paper:
    Ppsum += np.einsum('ij,kl->ijkl', B, B)
print("paper basis (Gamma^A = Gamma_A) equals completeness delta:", np.allclose(Ppsum,target))
# per-channel squared-trace signs (attraction pattern) of paper basis:
print("paper-basis tr[Gamma_A Gamma_A]/4 per channel:",
      {lab: np.trace(B@B).real/4 for lab,B in paper[:2]} ,
      "V:", np.trace(paper[2][1]@paper[2][1]).real/4,
      "A(gg5):", np.trace(paper[6][1]@paper[6][1]).real/4,
      "T:", np.trace(paper[10][1]@paper[10][1]).real/4)

# ---------- 5x5 Fierz matrix in hermitian channels ----------
# For channel groups: S(1), P(1), V(4), A(4), T(6):
# (psibar G_A psi)(psibar G_A psi) exchange-reordered:
# F defined by: sum over group members of B_A x B_A, exchanged indices, expanded back.
groups={'S':[0],'P':[1],'V':[2,3,4,5],'A':[6,7,8,9],'T':list(range(10,16))}
labels=list(groups)
F=np.zeros((5,5))
Bs=[B for _,B in basis]
for gi,ga in enumerate(labels):
    # build exchange tensor: sum_{A in ga} (B_A)_il (B_A)_kj  (indices swapped j<->l)
    X=np.zeros((4,4,4,4),dtype=complex)
    for idx in groups[ga]:
        X += np.einsum('il,kj->ijkl', Bs[idx], Bs[idx])
    # expand X_ijkl = sum_B c_B (B)_ij (B)_kl ; c_B = (1/16) tr-projection
    for gj,gb in enumerate(labels):
        c=0
        for idx in groups[gb]:
            c += np.einsum('ijkl,ji,lk->', X, Bs[idx], Bs[idx]).real/16
        F[gi,gj]=c/1  # coefficient of the FULL group-b sum? no: per projection below
# normalize: X = sum over ALL 16 c_A B_A x B_A with c_A = tr proj /16; group entry = sum over members / (# members? no)
# redo properly: coefficient of each basis element, then group-sum with equal coefficient check
F=np.zeros((5,5))
for gi,ga in enumerate(labels):
    X=np.zeros((4,4,4,4),dtype=complex)
    for idx in groups[ga]:
        X += np.einsum('il,kj->ijkl', Bs[idx], Bs[idx])
    coeffs=[]
    for idx2 in range(16):
        c = np.einsum('ijkl,ji,lk->', X, Bs[idx2], Bs[idx2]).real/16
        coeffs.append(c)
    for gj,gb in enumerate(labels):
        cs=[coeffs[idx2] for idx2 in groups[gb]]
        assert max(cs)-min(cs)<1e-10, (ga,gb,cs)
        F[gi,gj]=cs[0]
print("\nFierz exchange matrix F (rows: source channel sum; cols: coefficient per member of target channel)")
print("channels:", labels)
print(F)
# with Grassmann minus sign, the exchange contribution to channel b from quartic in channel a is -F[a,b]
