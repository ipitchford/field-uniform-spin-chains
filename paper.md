EVIDENCE PRESS/RESEARCH RELEASE CANDIDATE

**Field-uniform nonintegrability**

of spin chains

An exact three-site quotient, symmetry averaging and a complete
bilinear--biquadratic field-existence criterion

Anonymous•Version 1.0.1-candidate• September 2026

DOI: <https://doi.org/10.5281/zenodo.23021227>

**Scope and assurance.** The all-range implication uses Hokkyo's revised
reduction theorem. The paper does not classify arbitrary fields on the
three integrable interaction lines, the complete general qutrit
exceptional set, or quasilocal charges. The supplied referee report
concerns version 0.1; the new theorems in this version have exact
computational corroboration but have not received a fresh independent
specialist review.

# Setting, questions and prior results {#sec:setting}

Let $F_1,\ldots,F_m$ be a Hermitian, Hilbert--Schmidt orthonormal basis
of the traceless $d\times d$ matrices, where $m=d^2-1$ and
$\mathop{\mathrm{Tr}}(F_aF_b)=\delta_{ab}$. Consider $$\begin{equation}
\label{eq:ham}
 H_N=\sum_{i=1}^N h_{i,i+1}+\sum_{i=1}^N f_i,
 \qquad h=\sum_{a,b=1}^m J_{ab}F_a\otimes F_b,
 \qquad J=J^T\in M_m(\mathbb R).
\end{equation}$$ The chain is periodic, $N\ge6$, and every $f_i$ is an
arbitrary traceless Hermitian matrix on site $i$. The same interaction
$h$ occurs on every bond. In particular, $h$ has zero one-site partial
traces and is invariant under the site swap. Fields may have unbounded
norms, differ at every site and break all symmetries of $h$.

Every Hermitian swap-symmetric two-site density has a unique
decomposition
$$\widetilde h=cI\otimes I+h+\tfrac12(f\otimes I+I\otimes f),
 \qquad \mathop{\mathrm{Tr}}_1h=\mathop{\mathrm{Tr}}_2h=0.$$ For $d=3$,
the homogeneous-field class therefore has $36+8=44$ real parameters
after an irrelevant scalar is removed. An orthogonal change of operator
coordinates need not be a physical on-site unitary; none of our
arguments equates these transformations.

::: definition
**Definition 1** (Contiguous range). An operator has range at most $k$
if it is a sum of operators supported on cyclic intervals of at most $k$
consecutive sites. Its exact range, denoted $\mathop{\mathrm{len}}(Q)$,
is the smallest such $k$. Coefficients may depend on the site. A
conserved quantity satisfies $[H_N,Q]=0$. A string $A_iI_{i+1}B_{i+2}$
with nonzero traceless endpoints has range three, not two.
:::

We ask a question with an explicit quantifier over the fields: *can any
choice of the $f_i$ admit a local conserved quantity of range at least
three?* A negative answer is stronger than failure of one current to
commute at zero field. Our tests must exclude all shorter-range
corrections and charges without translation symmetry.

## Established ingredients and the present contribution

The local-conservation testing programme goes back to Grabowski and
Mathieu [@GrabowskiMathieu]. Hokkyo's revised theorem reduces an
all-range exclusion to the absence of an exact-range-three $Q$
satisfying $\mathop{\mathrm{len}}[H_N,Q]\le2$, provided its two
hypotheses hold [@HokkyoTest]. Here almost-conservation means that the
commutator has support of range at most two; it does not mean a small
commutator norm. Excluding this almost-conserved quantity is stronger
than excluding an exactly conserved three-site charge. We prove the
hypotheses at full interaction rank and certify them on the two
additional rank-deficient lines needed below.

Earlier spin-1 work establishes the field-free bilinear--biquadratic
classification and the classification with a uniform uniaxial on-site
anisotropy, as well as generic anisotropic models with additional
internal symmetries [@ParkLee; @HSC]. Further $U(1)$-symmetric families
with vanishing quadrupolar couplings are treated by Sengoku and
Watanabe [@SW]. Shiraishi and Yamaguchi prove an isotropic
arbitrary-spin dichotomy [@SY]. Those classifications are important
comparators: our isotropic result does not claim to discover the
zero-field integrable lines. Its additional content is the quantifier
over *every site-dependent Hermitian on-site field*, the exact residual
commutant, and a symmetry principle that gives this conclusion.

#### The precise extension of the isotropic predecessor.

Shiraishi and Yamaguchi [@SY] treat a translation-invariant, zero-field
isotropic Hamiltonian. Their proof for a nonzero three-support
obstruction already constrains the two-site correction using $SU(2)$ and
time-reversal symmetry. Thus removing the correction by symmetry is not,
by itself, a new idea. Here the Hamiltonian may break both internal and
translation symmetries through arbitrary site-dependent fields. We
average the *affine local almost-conservation equations*, including
their field variables, rather than assert that the conserved operator
inherits a symmetry of this Hamiltonian. Under the irreducible,
multiplicity-free hypotheses, averaging kills both the swap-odd
correction and the traceless field while retaining the obstruction. This
is the step that upgrades a zero-field test to an exclusion uniform over
all fields. The quotient-consistency theorem and the residual-commutant
theorem are distinct further statements; neither asserts complete
integrability of a general quotient-zero interaction.

The other contribution is an exact quotient of the three-site equations.
Translation averaging is applied to their leading commutator components,
not to a putative conserved charge under a Hamiltonian whose fields
break translation symmetry. Reversal then reduces the qutrit correction
and field variables to $28+8=36$. The quotient detects concrete
full-rank interactions, and relatively generic families, on which the
earlier cubic partial trace is identically uninformative.

## Relation to the Reshetikhin condition {#sec:reshetikhin}

Put $$\begin{equation}
\label{eq:CD}
 C=[h_{12},h_{23}],\qquad D=[h_{12}+h_{23},C].
\end{equation}$$ The full Reshetikhin condition is the existence of a
two-site $X$ with $$\begin{equation}
\label{eq:reshetikhin}
 D=X_{23}-X_{12}.
\end{equation}$$ Let $\pi(x)=x-\mathop{\mathrm{Tr}}(x)I/d$ and define
$$\begin{equation}
\label{eq:delta}
 \Delta(h)=(\pi_1\pi_3)D,\qquad \mathcal O(h)=\mathop{\mathrm{Tr}}_2D.
\end{equation}$$ Partial traces are unnormalised. The operator $\Delta$
retains the full middle-site matrix space, including its scalar
direction.
Equation [\[eq:reshetikhin\]](#eq:reshetikhin){reference-type="eqref"
reference="eq:reshetikhin"} implies $\Delta=0$, and hence
$\mathcal O=0$. In the last implication we use that $\mathcal O$ already
has traceless endpoints, so $\mathop{\mathrm{Tr}}_2\Delta=\mathcal O$.
The converse from $\mathcal O=0$ fails; the AKLT example below has
$\mathcal O=0$ but $\|\Delta\|_F^2=2560/81$.

Hokkyo proves that the specific boost-generated third conservation law
generates a commuting hierarchy [@HokkyoLaw]. Sanatani, Shiraishi and
Ishii prove a sufficiency result for a regular difference-form
Yang--Baxter construction from the full Reshetikhin condition with a
diagonalisability hypothesis [@SSI]. These results do not identify
vanishing of a partial projection with integrability, nor do they alone
give our arbitrary-field exclusion. The current paper uses their
framework for positioning; its sole external all-range proof dependency
is [@HokkyoTest].

# Leading rigidity and the all-range reduction {#sec:rigidity}

We separate the interaction hypotheses from any choice of fields.

::: {#def:rigid .definition}
**Definition 2** (Leading-rigid interaction). A nonzero interaction
$h\in\mathfrak{sl}_d(\mathbb C)\otimes\mathfrak{sl}_d(\mathbb C)$ is
leading-rigid when it has both properties:

1.  $[x\otimes I,h]=0$ or $[I\otimes x,h]=0$, with
    $x\in\mathfrak{sl}_d(\mathbb C)$, implies $x=0$.

2.  If
    $a,b\in\mathfrak{sl}_d(\mathbb C)\otimes\mathfrak{sl}_d(\mathbb C)$
    satisfy $$\begin{equation}
    \label{eq:pairlocal}
     [a_{12},h_{23}]=[h_{12},b_{23}],
    \end{equation}$$ then $a=b=ch$ for one scalar $c$.
:::

This local pair condition is sufficient for, and stronger in form than,
the global two-site hypothesis of the external theorem. It is convenient
because a fixed finite certificate establishes it for every chain
length.

::: {#lem:fullrank .lemma}
**Lemma 3** (Full rank supplies leading rigidity). *If $J$ is
invertible, $h$ is leading-rigid.*
:::

::: proof
*Proof.* The left and right tensor factors of $h$ span all traceless
matrices, so condition (i) follows from the scalar commutant of
$M_d(\mathbb C)$. For (ii), write $a=\sum M_{rs}F_r\otimes F_s$ and
$b=\sum N_{rs}F_r\otimes F_s$. Comparing the two endpoint factors
in [\[eq:pairlocal\]](#eq:pairlocal){reference-type="eqref"
reference="eq:pairlocal"} gives
$$\left[\sum_sM_{rs}F_s,\sum_tJ_{tu}F_t\right]
 =\left[\sum_sJ_{rs}F_s,\sum_tN_{tu}F_t\right].$$ Both families
determined by $J$ are bases. Thus this equation is $[Lx,y]=[x,Ry]$ for
two endomorphisms of $\mathfrak{sl}_d(\mathbb C)$. The pair-rigidity
lemma in Appendix [10](#app:pair){reference-type="ref"
reference="app:pair"} gives $L=R=c\operatorname{id}$, whence $M=N=cJ$. ◻
:::

The scalarity mechanism is established quasicentroid theory, not a new
Lie-algebra theorem. For a centreless perfect Lie algebra the
quasicentroid equals the centroid; the latter is scalar for a
finite-dimensional complex simple Lie algebra. We attribute this
background to Leger and Luks, as recalled explicitly by Andruszkiewicz,
Brzeziński and Radziszewski [@LegerLuks; @ABR].
Appendix [10](#app:pair){reference-type="ref" reference="app:pair"}
retains a self-contained proof for $\mathfrak{sl}_d$. The application to
the leading-charge equations is what is needed here.

::: {#prop:reduction .proposition}
**Proposition 4** (Specialised Hokkyo reduction). *Suppose $h$ is
leading-rigid. For any fields
in [\[eq:ham\]](#eq:ham){reference-type="eqref" reference="eq:ham"},
existence of a conserved quantity of exact range
$3\le k\le\lfloor N/2\rfloor$ implies the existence of an
exact-range-three $Q$ with $\mathop{\mathrm{len}}[H_N,Q]\le2$. Every
such $Q$ has the form $$\begin{equation}
\label{eq:Qform}
 Q=c C_N+A,\qquad
 C_N=\sum_i[h_{i,i+1},h_{i+1,i+2}],\qquad
 c\ne0,\quad \mathop{\mathrm{len}}(A)\le2.
\end{equation}$$ In particular $C_N$ has exact range three.*
:::

::: proof
*Verification of the external hypotheses.* Condition (i) is exactly the
injectivity assumption (4) of [@HokkyoTest]. A strictly two-local
operator $\sum_i a_i$ has no range-three part in its commutator
precisely when [\[eq:pairlocal\]](#eq:pairlocal){reference-type="eqref"
reference="eq:pairlocal"} holds with $(a,b)=(a_i,a_{i+1})$ at every
interval. Condition (ii) forces $a_i=c_i h$ and $a_{i+1}=c_i h$;
adjacent equations give a common scalar. Hence the source's space
$\mathcal B_{\le}^{(2)}$ equals $\mathbb CH_N^{(2)}$, its assumption
(6). Theorem 1 then gives the range-three reduction, and the $2\to3$
isomorphism of Theorem 2 fixes the leading part to $cC_N$ and guarantees
it is nonzero. The setup of that source explicitly allows site-dependent
on-site terms. ◻
:::

$C_N$ is anti-Hermitian; $iC_N$ is the corresponding Hermitian
observable. Multiplying a charge by this scalar does not change
conservation or its range. No finite-chain numerical calculation
replaces this implication. All finite computations below verify its
hypotheses or the local obstruction.

# An exact quotient that eliminates all fields {#sec:quotient}

Let $\mathfrak h_d$ be the real vector space of traceless Hermitian
$d\times d$ matrices. Write $S$ for the swap on two sites and $R$ for
reversal of three sites. Define $$\mathcal A_-=
 \{a\in\mathfrak h_d\otimes_{\mathbb R}\mathfrak h_d:SaS=-a\},
 \qquad \dim_{\mathbb R}\mathcal A_-=\frac{m(m-1)}{2}.$$ Since $h$ is
swap-symmetric, $RCR=-C$ and $RDR=-D$. Both $D$ and $\Delta$ are
Hermitian. Define a real linear map $$\begin{equation}
\label{eq:T}
 \begin{split}
 T_h:\mathcal A_-\oplus\mathfrak h_d&\longrightarrow
 \mathfrak h_d\otimes_{\mathbb R}\operatorname{Herm}(\mathbb C^d)\otimes_{\mathbb R}\mathfrak h_d,\\
 T_h(a,f)&=i\bigl([h_{12},a_{23}]+[h_{23},a_{12}]\bigr)
       +[f_1+f_2+f_3,C].
 \end{split}
\end{equation}$$ Every term on the right has traceless factors at all
three sites and is Hermitian and reversal-odd. In particular its
endpoint projection is itself.

::: definition
**Definition 5** (Field-eliminated obstruction). The obstruction is the
class of $\Delta(h)$ in the quotient by $\mathop{\mathrm{im}}T_h$.
Equivalently, with the real Hilbert--Schmidt inner product on Hermitian
operators, use the unique orthogonal residual $$\begin{equation}
\label{eq:residual}
 \mathcal U(h)=\Delta(h)-\operatorname{proj}_{\mathop{\mathrm{im}}T_h}\Delta(h).
\end{equation}$$ The zero/nonzero test is intrinsic; an orthonormal
basis is not needed to implement it by exact ranks.
:::

::: {#thm:quotient .theorem}
**Theorem 6** (Exact field elimination). *For a leading-rigid,
Hermitian, swap-symmetric interaction $h$, the following are
equivalent:*

1.  *$\Delta(h)\in\mathop{\mathrm{im}}T_h$, or equivalently
    $\mathcal U(h)=0$.*

2.  *For some periodic $N\ge6$ and some site-dependent Hermitian fields,
    an exact-range-three $Q$ satisfies
    $\mathop{\mathrm{len}}[H_N,Q]\le2$.*

3.  *There are fixed homogeneous fields $f_i=f$ and a fixed two-site
    correction density giving such a $Q$ for every periodic $N\ge6$.*

*Consequently, $\mathcal U(h)\ne0$ excludes every conserved quantity of
exact range $3\le k\le\lfloor N/2\rfloor$, simultaneously for all
$N\ge6$ and all on-site fields.*
:::

::: proof
*Proof.* Assume (b).
Divide [\[eq:Qform\]](#eq:Qform){reference-type="eqref"
reference="eq:Qform"} by its leading coefficient and take its
anti-Hermitian part. Since $H_N$ is Hermitian and $C_N^\dagger=-C_N$,
this preserves both the leading part $C_N$ and the condition on the
commutator. We may therefore write
$$Q=C_N+i\sum_i (a_i)_{i,i+1}+A^{(1)},
 \qquad a_i\in\mathfrak h_d\otimes_{\mathbb R}\mathfrak h_d,
 \qquad \mathop{\mathrm{len}}(A^{(1)})\le1.$$ The four-site
contributions to $[H_N^{(2)},C_N]$ cancel pairwise by the Jacobi
identity and commutation of disjoint bonds. Its remaining contribution
on interval $i,i+1,i+2$ is $D_i$. Taking the exact range-three part on
that interval gives $$\begin{equation}
\label{eq:localeq}
 \Delta+[f_i\otimes I\otimes I+I\otimes f_{i+1}\otimes I+I\otimes I\otimes f_{i+2},C]
 +i\bigl([h_{12},(a_{i+1})_{23}]+[h_{23},(a_i)_{12}]\bigr)=0.
\end{equation}$$ The one-site correction cannot contribute. Average
these equations after identifying their three-site coordinate spaces.
With $$\bar f=N^{-1}\sum_i f_i,\qquad \bar a=N^{-1}\sum_i a_i,$$ we
obtain the same equation with each field equal to $\bar f$ and each
correction equal to $\bar a$. This is an average of *equations*; no
symmetry of the inhomogeneous Hamiltonian is assumed.

Apply the reversal-odd projection $X\mapsto(X-RXR)/2$. It preserves
$\Delta$ and the uniform-field term. It replaces $\bar a$ by
$a_-=(\bar a-S\bar aS)/2$. We obtain $$\Delta+T_h(a_-,\bar f)=0,$$ which
proves (a).

Conversely, if $\Delta+T_h(a,f)=0$, choose uniform fields $f$ and
$Q=C_N+i\sum_i a_{i,i+1}$. The same local calculation makes every
range-three component vanish, while the four-site terms cancel as above.
Thus $\mathop{\mathrm{len}}[H_N,Q]\le2$ for every $N\ge6$. Its leading
part is nonzero by Proposition [4](#prop:reduction){reference-type="ref"
reference="prop:reduction"}. This proves (c); (c) implies (b). The final
conclusion follows from that proposition. ◻
:::

::: {#cor:dual .corollary}
**Corollary 7** (Dual certificate). *If a Hermitian three-site $Z$
satisfies $$\mathop{\mathrm{Tr}}(ZT_h(a,f))=0\quad\hbox{for all }a,f,
 \qquad \mathop{\mathrm{Tr}}(Z\Delta(h))\ne0,$$ then the all-field
exclusion in Theorem [6](#thm:quotient){reference-type="ref"
reference="thm:quotient"} holds. Conversely such a $Z$ exists whenever
$\mathcal U(h)\ne0$; one may take $Z=\mathcal U(h)$.*
:::

For $d=3$, $T_h$ has $28+8=36$ real columns. Its natural ambient space
has dimension $8\cdot9\cdot8=576$, and its image is further restricted
by reversal. The certifier uses a redundant, transparent coordinate
system: real row-major entries of the $27\times27$ matrix followed by
imaginary entries, giving $1458$ rows. Redundancy changes neither rank
nor consistency.

**Meaning of completeness.**
Theorem [6](#thm:quotient){reference-type="ref"
reference="thm:quotient"} is complete for the existential,
field-eliminated *almost-conservation* test in (b). When the quotient
vanishes, the residual range-one and range-two equations may still
prevent exact conservation. The theorem does not identify its zero set
with the integrable locus.

# Multiplicity-free symmetry removes the correction space {#sec:symmetry}

::: {#thm:symmetry .theorem}
**Theorem 8** (Symmetry evaluation of the quotient). *Let a compact
group $G$ act irreducibly and unitarily on $V\cong\mathbb C^d$, and
suppose $V\otimes V$ is a multiplicity-free $G$-representation. Let
$h\in\mathfrak{sl}_d(\mathbb C)\otimes\mathfrak{sl}_d(\mathbb C)$ be
Hermitian, $G$-invariant and leading-rigid. Then $$\begin{equation}
\label{eq:symres}
 \mathcal U(h)=\Delta(h).
\end{equation}$$ In particular, if $\Delta(h)\ne0$, no choice of
site-dependent Hermitian fields admits conserved quantities of the
ranges stated in Theorem [6](#thm:quotient){reference-type="ref"
reference="thm:quotient"}.*
:::

::: proof
*Proof.* The two-site commutant of $G$ is commutative because the
representation is multiplicity-free. The swap belongs to it. Thus every
invariant two-site operator, including $h$, commutes with the swap.

Let $\mathbb E_r$ be Haar averaging of conjugation by $G$ on
$V^{\otimes r}$. Irreducibility implies
$\mathbb E_1(f)=\mathop{\mathrm{Tr}}(f)I/d=0$ for traceless $f$. An
invariant two-site operator commutes with the swap, so averaging a
swap-odd $a$ gives $\mathbb E_2(a)=0$. Invariance of $h$ and $C$ yields
$$\mathbb E_3(T_h(a,f))=T_h(\mathbb E_2(a),\mathbb E_1(f))=0.$$ The
operator $\Delta(h)$ is invariant, since both partial-trace projection
and the commutators are equivariant. Haar averaging is the orthogonal
projection onto invariant operators. Therefore
$\Delta(h)\perp\mathop{\mathrm{im}}T_h$,
proving [\[eq:symres\]](#eq:symres){reference-type="eqref"
reference="eq:symres"}. Theorem [6](#thm:quotient){reference-type="ref"
reference="thm:quotient"} supplies the conclusion. ◻
:::

The fields need not retain the symmetry: the averaging above acts on the
linear correction and field terms, not on $H_N$ as a conserved system.
This is the point that extends the invariant zero-field test to
arbitrary on-site potentials.

::: {#cor:spinS .corollary}
**Corollary 9** (Isotropic interactions at full rank). *For the
irreducible spin-$S$ representation,
$V_S\otimes V_S=\bigoplus_{L=0}^{2S}V_L$ is multiplicity-free. Every
full-traceless-rank isotropic interaction with $\Delta(h)\ne0$ therefore
has the arbitrary-field exclusion property.*
:::

The full-rank condition can be replaced by
Definition [2](#def:rigid){reference-type="ref" reference="def:rigid"}.
We verify the needed rank-deficient spin-1 cases next. No assertion
about every rank-deficient higher-spin interaction is needed.

# The complete spin-1 bilinear--biquadratic field-existence criterion {#sec:blbq}

Let $S_x,S_y,S_z$ be the spin-1 matrices and $$\begin{equation}
\label{eq:blbq}
 B=\sum_{\alpha=x,y,z}S_\alpha\otimes S_\alpha,
 \qquad h(u,v)=uB+v(B^2-\tfrac43I),\qquad (u,v)\in\mathbb R^2.
\end{equation}$$ The scalar subtraction gives zero one-site partial
traces. In a Cartesian spin basis, put $$P|ab\rangle=|ba\rangle,\qquad
 Q_0=|\Omega\rangle\langle\Omega|,\qquad |\Omega\rangle=\sum_{a=0}^2|aa\rangle.$$
Then $B=P-Q_0$, $B^2=I+Q_0$, and $$\begin{equation}
\label{eq:cartesian}
 h(u,v)=uP+(v-u)Q_0-\tfrac v3I.
\end{equation}$$ Here $Q_0$ is a two-site contraction, not a conserved
quantity.

::: {#prop:isocubic .proposition}
**Proposition 10** (Exact cubic and interaction spectrum). *For the
family [\[eq:blbq\]](#eq:blbq){reference-type="eqref"
reference="eq:blbq"}, $$\begin{align}
 \mathcal O(h(u,v))&=0,\label{eq:isoblind}\\
 \Delta(h(u,v))&=u(u-v)(u+v)W,
 &W&=\Delta(h(1,0)),& \|W\|_F^2&=40.\label{eq:isofactor}
\end{align}$$ In the orthonormal traceless operator coordinates, $J$ has
eigenvalues $$\begin{equation}
\label{eq:isospectrum}
 v\quad(\hbox{multiplicity }5),\qquad
 2u-v\quad(\hbox{multiplicity }3),\qquad
 \det J=v^5(2u-v)^3.
\end{equation}$$*
:::

::: proof
*Proof.* The two eigenspaces
in [\[eq:isospectrum\]](#eq:isospectrum){reference-type="eqref"
reference="eq:isospectrum"} are, after complexification, the
symmetric-traceless matrices and antisymmetric matrices in the Cartesian
basis. Substitution
in [\[eq:cartesian\]](#eq:cartesian){reference-type="eqref"
reference="eq:cartesian"}, or contraction against an orthonormal basis
of these spaces, gives the stated eigenvalues.

For transparency, the polynomial identity
in [\[eq:isofactor\]](#eq:isofactor){reference-type="eqref"
reference="eq:isofactor"} has a small exact computational proof. Write
$H=P-Q_0$, $K=Q_0$; the scalar $-vI/3$ does not affect the commutators.
Let $H_{12},H_{23},K_{12},K_{23}$ denote their embeddings and set
$$C_{20}=[H_{12},H_{23}],\quad
 C_{11}=[H_{12},K_{23}]+[K_{12},H_{23}],\quad
 C_{02}=[K_{12},K_{23}].$$ Expanding $D$ in the monomials
$u^3,u^2v,uv^2,v^3$ gives, respectively, $$\begin{align*}
 &[H_{12}+H_{23},C_{20}],\\
 &[H_{12}+H_{23},C_{11}]+[K_{12}+K_{23},C_{20}],\\
 &[H_{12}+H_{23},C_{02}]+[K_{12}+K_{23},C_{11}],\\
 &[K_{12}+K_{23},C_{02}].
\end{align*}$$ Applying $9\pi_1\pi_3$ produces the four integer matrices
$9W,0,-9W,0$. The independent integer checker verifies each entry of
these four matrices; the symbolic checker independently verifies the
full two-variable identity. The matrix $W$ is given exactly in the
evidence. In zero-based row-major indexing, $W_{0,4}=1/3$, so it is
nonzero. Its $96$ nonzero entries comprise $48$ of absolute value $1/3$,
$24$ of absolute value $2/3$ and $24$ of absolute value $1$. Thus
$$\|W\|_F^2=48/9+24(4/9)+24=40.$$ Finally, $\mathcal O$ is rotationally
invariant and odd under endpoint exchange. The two-spin decomposition
$V_1\otimes V_1=V_0\oplus V_1\oplus V_2$ is multiplicity-free, so any
invariant two-site operator commutes with exchange. Hence
$\mathcal O=0$. Its four cubic coefficient matrices are also checked to
vanish exactly. ◻
:::

::: {#lem:rankdef .lemma}
**Lemma 11** (Both rank-deficient lines are leading-rigid). *The
interactions $h(1,0)$ and $h(1,2)$ satisfy
Definition [2](#def:rigid){reference-type="ref" reference="def:rigid"}.
Consequently every nonzero member
of [\[eq:blbq\]](#eq:blbq){reference-type="eqref" reference="eq:blbq"}
is leading-rigid.*
:::

:::: proof
*Proof.*
Equation [\[eq:isospectrum\]](#eq:isospectrum){reference-type="eqref"
reference="eq:isospectrum"} leaves only $v=0$ and $v=2u$ outside full
rank. On the first line the active local factors span the antisymmetric
matrices, whose action on $\mathbb C^3$ is irreducible. On the second
they span all symmetric-traceless matrices. Either set has only scalar
matrices in its commutant, proving the boundary injectivity. The exact
checker also verifies both one-sided maps have rank $8$.

For the pair condition, use the ordered basis $$\begin{equation}
\label{eq:realbasis}
 E_{01},E_{02},E_{10},E_{12},E_{20},E_{21},
 \mathop{\mathrm{diag}}(1,-1,0),\mathop{\mathrm{diag}}(0,1,-1)
\end{equation}$$ for $\mathfrak{sl}_3(\mathbb C)$. The map
$$\mathcal L_h(a,b)=[a_{12},h_{23}]-[h_{12},b_{23}]$$ has $128$ columns
and $729$ rows in row-major matrix coordinates. The supplied certificate
indices select $127\times127$ minors with the following exact residues:

::: center
  Integer interaction      Minor order   Determinant modulo $101$
  ---------------------- ------------- --------------------------
  $P-Q_0=h(1,0)$                   127                         73
  $3P+3Q_0-2I=3h(1,2)$             127                         59
:::

Both minors are nonzero, so the rank is at least $127$ over $\mathbb Q$
and $\mathbb C$. The nonzero domain vector $(h,h)$ lies in the kernel,
so the rank is at most $127$. The kernel is therefore exactly its span,
proving the pair condition. Both checkers reconstruct the maps and their
minors rather than trusting a recorded rank. Nonzero scaling preserves
these properties, and Lemma [3](#lem:fullrank){reference-type="ref"
reference="lem:fullrank"} covers the rest of the family. ◻
::::

::: {#thm:blbq .theorem}
**Theorem 12** (Arbitrary-field exclusion and its sharp interaction
boundary). *Fix $(u,v)\ne(0,0)$. If $$\begin{equation}
\label{eq:nonintegrable}
 u(u^2-v^2)\ne0,
\end{equation}$$ then every periodic $N\ge6$ and every choice of
Hermitian fields $f_1,\ldots,f_N$ has no conserved quantity of exact
range $3\le k\le\lfloor N/2\rfloor$.*

*If $u(u^2-v^2)=0$, the zero-field chain has the nonzero conserved
range-three quantity $C_N$. Thus, for this nonzero interaction family,
*some choice of fields admits a conserved quantity in the stated
higher-range interval if and only if*
$$u=0\quad\hbox{or}\quad u=v\quad\hbox{or}\quad u=-v.$$ The existence
statement holds for every $N\ge6$ with zero fields; it does not assert
preservation under arbitrary fields on those lines.*
:::

::: proof
*Proof.*
For [\[eq:nonintegrable\]](#eq:nonintegrable){reference-type="eqref"
reference="eq:nonintegrable"}, combine
Lemma [11](#lem:rankdef){reference-type="ref" reference="lem:rankdef"},
Proposition [10](#prop:isocubic){reference-type="ref"
reference="prop:isocubic"} and
Theorem [8](#thm:symmetry){reference-type="ref"
reference="thm:symmetry"}.

On the three remaining lines $\Delta=0$. We show why this implies
conservation of $C_N$ here, although no such general implication was
used in Theorem [6](#thm:quotient){reference-type="ref"
reference="thm:quotient"}. Since $D$ has no component with both
endpoints traceless, it is a sum of neighbouring two-site and one-site
terms. Rotational invariance removes all traceless one-site terms. Its
two-site components are invariant and hence swap-even. Reversal oddness
then forces $D=X_{23}-X_{12}$ for a two-site $X$. The translation sum
telescopes to zero. Together with the four-site Jacobi cancellation,
this proves $[H_N^{(2)},C_N]=0$. Leading rigidity and
Proposition [4](#prop:reduction){reference-type="ref"
reference="prop:reduction"} give $C_N\ne0$ of exact range three. The
verifier additionally checks the full telescoping identity at the
representatives $(0,1),(1,1),(1,-1)$; homogeneity covers the lines. ◻
:::

## All remaining short-range charges

::: {#thm:isocommutant .theorem}
**Theorem 13** (Exact local commutant in the excluded family).
*Under [\[eq:nonintegrable\]](#eq:nonintegrable){reference-type="eqref"
reference="eq:nonintegrable"}, let
$$\mathfrak s_f=\{x\in\operatorname{span}_{\mathbb C}\{S_x,S_y,S_z\}:[x,f_i]=0\text{ for every }i\}.$$
Then $$\begin{equation}
\label{eq:isocommutant}
 \{Q:[H_N,Q]=0,\ \mathop{\mathrm{len}}(Q)\le\lfloor N/2\rfloor\}
 =\operatorname{span}_{\mathbb C}\{I,H_N\}+\left\{\sum_i x_i:x\in\mathfrak s_f\right\},
\end{equation}$$ where $x_i$ is the copy of the *same* local matrix $x$
at every site.*
:::

::: proof
*Proof.* Theorem [12](#thm:blbq){reference-type="ref"
reference="thm:blbq"} reduces a charge to range at most two, and leading
rigidity fixes its two-site part to $cH_N^{(2)}$. After subtracting
$cH_N$ and a scalar, the charge is $\sum_i x_i$ for traceless matrices
$x_i$, initially allowed to differ. Its two-site commutator equations
are $$\begin{equation}
\label{eq:bond}
 [x_i\otimes I+I\otimes x_{i+1},h]=0.
\end{equation}$$ Define $D_x$ by $[x,F_b]=\sum_a(D_x)_{ab}F_a$. The
bilinear trace pairing gives $D_x^T=-D_x$, also for complex $x$.
Equation [\[eq:bond\]](#eq:bond){reference-type="eqref"
reference="eq:bond"} and its transpose imply $$\begin{equation}
\label{eq:J2}
 D_{x_i}J-JD_{x_{i+1}}=0,
 \qquad [D_{x_i},J^2]=0.
\end{equation}$$ This implication does not require $J$ to be invertible.

In the Cartesian basis, the two eigenvalues of $J^2$ differ by
$(2u-v)^2-v^2=4u(u-v)\ne0$. Hence $D_{x_i}$ preserves the antisymmetric
and symmetric-traceless matrix spaces separately. Decompose $x_i$ by
transpose parity. Its antisymmetric part preserves those spaces under
commutation, whereas its symmetric part exchanges them. The latter must
therefore commute with all antisymmetric matrices; their scalar
commutant forces this traceless symmetric part to vanish. Thus every
$x_i$ is a spin generator.

For a spin generator, $D_{x_i}$ commutes with $J$. The first equation
in [\[eq:J2\]](#eq:J2){reference-type="eqref" reference="eq:J2"} becomes
$(D_{x_i}-D_{x_{i+1}})J=0$. At least one of the two interaction sectors
is nonzero. The spin action on either active sector has trivial kernel:
equivalently, a spin generator commuting with all antisymmetric matrices
or with all symmetric-traceless matrices is zero. Thus $x_i=x_{i+1}$
around the ring. The remaining one-site equations are exactly
$[x,f_i]=0$ separately at each site. Conversely those conditions make
the displayed uniform spin sum commute with both interactions and
fields, proving equality. ◻
:::

At zero fields this leaves the three components of total spin. Fields
with no common commuting spin direction leave only $I$ and $H_N$. This
is a finite exact condition on the fields, not an assumption about
chaotic spectra or thermalisation.

## AKLT as a sharp check on the projection

For $u=1$, $v=1/3$, $$\det J=\frac{125}{6561}\ne0,\qquad
 \mathcal O(h)=0,\qquad
 \|\Delta(h)\|_F^2=40(1-1/9)^2=\frac{2560}{81}>0.$$ Thus the earlier gap
certificate is genuinely blind at full rank. The new symmetry-evaluated
quotient detects this interaction and excludes higher-range local
charges for *arbitrary* on-site potentials. This strengthens the field
scope of the established AKLT nonintegrability result; it does not claim
the zero-field result as new.

# The cubic quick test and unrestricted genericity {#sec:quick}

::: {#prop:gap .proposition}
**Proposition 14** (The gap projection is a quotient obstruction). *For
any symmetric $h$, $\mathop{\mathrm{Tr}}_2T_h(a,f)=0$. Therefore
$\mathcal O(h)\ne0$ implies $\mathcal U(h)\ne0$. If $J$ is invertible,
this excludes all higher-range charges for arbitrary fields.*
:::

::: proof
*Proof.* Overlapping two-site terms have a commutator at the middle
site, so their middle trace is zero. The density $C$ has three traceless
factors; commutation with an on-site field retains tracelessness at
every site. Thus tracing the middle factor kills both terms of $T_h$.
Since $\mathop{\mathrm{Tr}}_2\Delta=\mathcal O$, membership
$\Delta\in\mathop{\mathrm{im}}T_h$ would imply $\mathcal O=0$. ◻
:::

The actual middle-scalar projection inserts $I/d$ between the two
factors of $\mathcal O$. This factor is required because the trace is
unnormalised.

## Coefficient formula and Hermiticity

Write $[F_a,F_b]=i\sum_c f_{abc}F_c$, with real totally antisymmetric
structure constants. Define the symmetric quadratic matrix
$$\begin{equation}
\label{eq:K}
 K(J)_{rc}=\sum_{a,e,b,t} f_{rae}f_{cbt}J_{ab}J_{et}.
\end{equation}$$ Then direct middle-trace contraction gives
$$\begin{equation}
\label{eq:cubiccoeff}
 \mathcal O(h)=\sum_{r,s}[J,K(J)]_{rs}F_r\otimes F_s.
\end{equation}$$ Indeed, the two terms of $D$ contribute $-KJ$ and $JK$,
respectively; symmetry of $J$ makes $K$ symmetric. Its commutator
coefficient matrix is real and skew-symmetric. This means that the
*tensor operator* is Hermitian and exchange-odd, not anti-Hermitian:
every tensor factor $F_r\otimes F_s$ is Hermitian.

For $d=2$, $f_{abc}=\sqrt2\epsilon_{abc}$ and
$K(J)=4\operatorname{adj}(J)$. Thus $\mathcal O=0$ for every symmetric
qubit interaction. The general quotient remains defined, but no
nonvanishing qubit gap obstruction is asserted.

## Residual short charges beyond simple spectrum

::: {#lem:abelian .lemma}
**Lemma 15** (Abelian interaction eigenspaces). *Suppose the
higher-range charges have been excluded and $h$ is leading-rigid. If
every eigenspace of $J^2$, regarded as a subspace of traceless local
matrices, is abelian under commutation, then $$\begin{equation}
\label{eq:IH}
 \{Q:[H_N,Q]=0,\ \mathop{\mathrm{len}}(Q)\le\lfloor N/2\rfloor\}
 =\operatorname{span}_{\mathbb C}\{I,H_N\}
\end{equation}$$ for every choice of fields. Simple spectrum of $J^2$ is
a sufficient special case.*
:::

::: proof
*Proof.* As in Theorem [13](#thm:isocommutant){reference-type="ref"
reference="thm:isocommutant"}, it remains to
solve [\[eq:bond\]](#eq:bond){reference-type="eqref"
reference="eq:bond"}.
Equation [\[eq:J2\]](#eq:J2){reference-type="eqref" reference="eq:J2"}
makes $D_{x_i}$ block diagonal in the eigenspaces of $J^2$. For $u,v$ in
the same such eigenspace, trace invariance gives
$\mathop{\mathrm{Tr}}(v[x_i,u])=\mathop{\mathrm{Tr}}(x_i[u,v])=0$.
Abelianity therefore makes every block zero. Hence $D_{x_i}=0$, and the
centreless property of $\mathfrak{sl}_d(\mathbb C)$ gives $x_i=0$. ◻
:::

::: {#thm:generic .theorem}
**Theorem 16** (Unrestricted generic nonintegrability). *For every
$d\ge3$, an open dense full-Lebesgue-measure set of real symmetric
traceless interactions has local
commutant [\[eq:IH\]](#eq:IH){reference-type="eqref" reference="eq:IH"}
for every periodic $N\ge6$ and all site-dependent Hermitian fields. For
$d=3$, one explicit sufficient nonzero polynomial is $$\begin{equation}
\label{eq:poly}
 P(J)=\det J\;\mathop{\mathrm{Disc}}_t\det(tI-J^2)\;\mathop{\mathrm{Tr}}(\mathcal O(h)^2),
 \qquad \deg P=8+112+6=126.
\end{equation}$$*
:::

::: proof
*Proof.* Appendix [11](#app:old){reference-type="ref"
reference="app:old"} gives an exact qutrit witness with $\det J\ne0$,
simple spectrum of $J^2$, and $\|\mathcal O\|_F^2=81\,962\,496$. Thus
$P$ is not the zero polynomial, and its nonzero set has the stated
topological and measure properties.
Proposition [14](#prop:gap){reference-type="ref" reference="prop:gap"}
and Lemma [15](#lem:abelian){reference-type="ref"
reference="lem:abelian"} give the conclusion. The same interaction set
works for all chain lengths and fields; there is no size-dependent
exceptional set to intersect. Its product with all uniform fields gives
the 44-parameter statement.

For $d>3$, embed the eight normalised qutrit matrices in a $3\times3$
block and complete them to an orthonormal traceless Hermitian basis. The
embedded obstruction is unchanged and nonzero. Give the complementary
coordinates distinct, sufficiently small positive diagonal coupling
coefficients. The interaction matrix becomes invertible with positive
distinct eigenvalues and the obstruction remains nonzero. The analogous
polynomial is therefore nonzero in every such dimension. ◻
:::

This generic result is inherited from the version-0.1 argument, now
situated inside the stronger quotient. It does not imply coverage of
every symmetry-constrained subfamily. The isotropic blindness of its
last factor is precisely why
Sections [4](#sec:symmetry){reference-type="ref"
reference="sec:symmetry"}--[5](#sec:blbq){reference-type="ref"
reference="sec:blbq"} are necessary.

# Generic exclusion on both blind diagonal hypersurfaces {#sec:hypersurfaces}

Use the unnormalised Hermitian qutrit basis $$\begin{align}
\label{eq:G}
 &(G_1,G_2,G_3,G_4,G_5,G_6,G_7,G_8)\\[-2mm]
 &\quad=(X_{01},Y_{01},\mathop{\mathrm{diag}}(1,-1,0),X_{02},Y_{02},X_{12},Y_{12},\mathop{\mathrm{diag}}(1,1,-2)),\nonumber
\end{align}$$ where $X_{ab}=E_{ab}+E_{ba}$ and
$Y_{ab}=-iE_{ab}+iE_{ba}$. The Gram diagonal is $(2,2,2,2,2,2,2,6)$. For
$h(j)=\sum_{a=1}^8 j_aG_a\otimes G_a$, the exact old identity is
$$\begin{equation}
\label{eq:diaggap}
 \mathcal O(h(j))=4(j_3-3j_8)(j_4j_5-j_6j_7)
       (G_3\otimes G_8-G_8\otimes G_3).
\end{equation}$$ The complete eight-variable identity is verified
symbolically in the bundle. Its zero set is the union of
$$Z_C=\{j_3=3j_8\},\qquad Z_P=\{j_4j_5=j_6j_7\}.$$ The new quotient is
not identically zero on either component.

::: {#thm:blind .theorem}
**Theorem 17** (Two certified blind-locus families). *Each of $Z_C$ and
$Z_P$ contains a nonempty relative Zariski-open set of interactions for
which [\[eq:IH\]](#eq:IH){reference-type="eqref" reference="eq:IH"}
holds for every $N\ge6$ and all on-site fields. These sets are dense and
of full measure in the respective regular real loci after exclusion of
the additional algebraic degeneracies described in the proof.*
:::

:::: proof
*Proof.* The two exact witnesses are $$\begin{equation}
\label{eq:blindwitness}
 j^C=(1,2,24,4,5,6,7,8),\qquad
 j^P=(1,2,3,4,15,5,12,8).
\end{equation}$$ Every entry is nonzero, so both interactions have full
rank. Both have $\mathcal O=0$. In the $1458$-row real-coordinate
convention of Section [3](#sec:quotient){reference-type="ref"
reference="sec:quotient"}, form the augmented matrix
$[9T_h\mid9\Delta]$. The $28$ correction columns use
$G_a\otimes G_b-G_b\otimes G_a$, ordered lexicographically with $a<b$,
followed by $8$ fields $G_a$, then $\Delta$. The supplied $37\times37$
minors have determinants

::: center
  Witness     $\mathop{\mathrm{rank}}_{\mathbb Q}T_h$   $\mathop{\mathrm{rank}}_{\mathbb Q}[T_h\mid\Delta]$   Minor modulo $101$
  --------- ----------------------------------------- ----------------------------------------------------- --------------------
  $j^C$                                            36                                                    37                   43
  $j^P$                                            36                                                    37                   64
:::

Since $T_h$ has at most $36$ columns, either nonzero augmented minor
already proves $\Delta\notin\mathop{\mathrm{im}}T_h$ over $\mathbb R$;
the exact rational ranks provide a corroborating check. By
Theorem [6](#thm:quotient){reference-type="ref"
reference="thm:quotient"}, higher-range charges are excluded.

Each fixed minor is a homogeneous polynomial of degree
$28\cdot1+8\cdot2+3=47$ in $j$. The displayed witnesses show that its
restriction to the corresponding hypersurface is nonzero. The hyperplane
$Z_C$ and the determinant hypersurface $Z_P$ are irreducible, and their
regular real loci are Zariski dense. Thus nonvanishing defines the
stated relatively generic sets.

For $Z_P$, exclude vanishing coordinates and coincidences between the
absolute values of $2j_1,\ldots,2j_7,6j_8$. These conditions hold at
$j^P$, so they remove only proper algebraic subsets. The simple-spectrum
case of Lemma [15](#lem:abelian){reference-type="ref"
reference="lem:abelian"} applies. On $Z_C$, the forced equality
$2j_3=6j_8$ leaves a two-dimensional eigenspace spanned by the commuting
diagonal matrices $G_3,G_8$. Excluding every other absolute-value
coincidence leaves all remaining eigenspaces one-dimensional. These
conditions hold at $j^C$, and the general form of
Lemma [15](#lem:abelian){reference-type="ref" reference="lem:abelian"}
applies. The exact local bond map has rank $16$ at both witnesses, an
additional check of the absence of residual on-site generators. ◻
::::

This statement concerns the two hypersurfaces inside the fixed
eight-parameter diagonal-$G$ family. It is not a decomposition of the
full 36-parameter zero set of $\mathcal O$, and it does not classify
their intersections or every exceptional point.

# Algorithms, benchmarks and evidence {#sec:evidence}

The public program `certify_field_uniform.py` accepts an exact rational
symmetric $8\times8$ coefficient matrix in the $G$ basis. It first
checks full interaction rank, then uses the gap obstruction when
available. If the gap vanishes, it compares the exact ranks of $T_h$ and
$[T_h\mid\Delta]$. A separate $16$-column local bond map determines
whether any one-site generators remain. For the bilinear--biquadratic
family, a named input mode applies
Theorems [12](#thm:blbq){reference-type="ref" reference="thm:blbq"}
and [13](#thm:isocommutant){reference-type="ref"
reference="thm:isocommutant"}, including the rank-deficient cases.

All ranks used to issue a result are exact rational ranks. The stored
nonzero minors use the prime $101$ only as *lower-rank certificates*
over characteristic zero; no vanishing modular minor is interpreted as a
characteristic-zero rank upper bound. Input floats, asymmetric
coefficient arrays, invalid rationals and non-finite values are
rejected. The older `certify_interaction.py` remains as a compatibility
implementation of the quick test.

The matrix sizes depend on local dimension, not chain length. The formal
input size still includes the bit lengths of rational coefficients, so
no claim of constant arithmetic or bit complexity is made. The file
`BENCHMARKS.md` records actual wall-clock timings and the environment
for this release. In the supplied historical run, the seven original
suites passed in $24.626$ seconds, including process startup. The
publication revision adds an eighth suite for portable witnesses and
tamper rejection; fresh timings are retained in the machine-readable
publication receipt. These are illustrative measurements, not
cross-machine guarantees; the machine-readable report records the
environment and individual timings.

The original bundle includes seven runnable suites: the inherited
integer and symbolic checks, the inherited certifier controls, the new
symbolic/modular extension checks, an independent integer implementation
of the isotropic calculation and rank certificates, dense
structure-constant regressions, and controls for the stronger public
certifier. The new independent implementation imports none of the other
submitted modules. This is implementation diversity within the present
work, not an independent human review.

## Portable quotient witnesses

The optional `--witness` output records the input and its digest, the
exact coordinate convention, and either a sparse rational dual
functional $y$ with $y^T(9T_h)=0$ and $y^T(9\Delta)=1$, or rational
coefficients $x$ with $(9T_h)x+9\Delta=0$. The separate
`portable_witness.py` command reconstructs the matrices from a
separately supplied intended interaction and checks these identities by
multiplication, without rank computation. It shares the
matrix-construction code, so it is not an independent implementation.
The ordinary certifier output is labelled an exact-recomputation report.
Neither portable identity certifies leading rigidity, the residual
commutant or the imported all-range theorem; consistency certifies only
almost-conservation. Tamper controls alter coefficients, dimensions,
coordinate conventions and input binding. Assertion-based legacy suites
refuse Python optimisation rather than silently dropping tests.

## What the certificates establish

The two $127$-minors and their known kernel vectors establish exact
pair-kernel dimensions. The $37$-minors certify two new positive
obstruction witnesses and the nonzero polynomial restrictions used for
genericity. The full two-variable identity and four separately
constructed homogeneous coefficient matrices prove the isotropic
factorisation for all real parameters, rather than sampling it. Three
additional dense rational interactions check the direct nested
commutator against the structure-constant formula. The isotropic family
and three qubit examples are negative controls for the *old*
obstruction; the three integrable isotropic lines are positive controls
for a conserved current.

The all-range theorem, symmetry averaging, quotient equivalence and
residual-commutant arguments are mathematical proofs in this manuscript.
They are not reduced to numerical experiments. Exact finite calculations
support the stated algebraic steps, but the proof as a whole has not
been formalised in a proof assistant.

# Limitations and release boundary {#sec:limits}

The complete statement in Theorem [12](#thm:blbq){reference-type="ref"
reference="thm:blbq"} classifies whether *there exists a field choice*
admitting a higher-range charge for an isotropic interaction. It does
not classify all individual field configurations on the three
charge-admitting lines. The general quotient similarly decides existence
of an almost-conserved three-site candidate, not exact integrability
when its obstruction vanishes. The unrestricted rank-deficient qutrit
class, the full quotient-zero set, and the complete exceptional-set
classification remain outside the proved results.

The range bound is $3\le k\le\lfloor N/2\rfloor$ on periodic chains. We
do not exclude charges of larger contiguous range, nonlocal spectral
projectors, polynomials in global charges, quasilocal tails, effective
integrability in a projected low-energy sector, or approximate
conservation at large fields. Nor do we infer thermalisation, the
eigenstate thermalisation hypothesis, or level-spacing statistics.

Version 0.1 received the supplied favourable referee report. The present
version addresses its scholarly revisions and adds theorems that require
new specialist scrutiny; that earlier report must not be presented as
refereeing these additions. The targeted literature search found no
direct prior statement of the combined arbitrary-field theorem and
quotient. This is not a historical-priority certificate. The publication
revision responds to the supplied version-1 review without changing the
main theorems. The review is not authenticated external peer review, and
its separately mentioned sandbox audit archive was not supplied for this
publication replay. The new portable-witness checks are producer-side
evidence. Archival identifiers and exact payload identity are given in
the accompanying citation and release records.

# Self-contained pair-rigidity proof {#app:pair}

::: {#lem:pair .lemma}
**Lemma 18** (Pair rigidity for $\mathfrak{sl}_d$). *If
$L,R\in\mathop{\mathrm{End}}(\mathfrak{sl}_d(\mathbb C))$ satisfy
$[Lx,y]=[x,Ry]$ for all $x,y\in\mathfrak{sl}_d(\mathbb C)$, then
$L=R=c\operatorname{id}$.*
:::

::: proof
*Proof.* Use the complex bilinear trace form, not a conjugate transpose.
Trace invariance and nondegeneracy give $L^*[y,z]=[Ry,z]$. Interchanging
$y,z$ also gives $L^*[y,z]=[y,Rz]$. Thus
$$[Rx,y]=[x,Ry],\qquad [Rx,x]=0.$$ For a regular traceless diagonal $D$,
the second relation says $RD$ is diagonal; by linearity and density this
holds for every traceless diagonal $D$. With $i\ne j$, apply the first
relation to $D,E_{ij}$ to obtain $$RE_{ij}=c_{ij}E_{ij}+D_{ij},\qquad
 (RD)_i-(RD)_j=c_{ij}(D_i-D_j),$$ where $D_{ij}$ is traceless diagonal.
Reversing a root gives $c_{ij}=c_{ji}$. For three distinct indices,
independence of $D_i-D_j$ and $D_j-D_k$ gives $c_{ik}=c_{ij}=c_{jk}$.
Thus all coefficients equal a single $c$ for $d\ge3$; the reversed-root
identity suffices for $d=2$. Hence $RD=cD$ on diagonal matrices.

Apply the relation to $E_{ij},E_{kl}$. The scalar terms cancel, leaving
$$((D_{ij})_k-(D_{ij})_l)E_{kl}
 =((D_{kl})_j-(D_{kl})_i)E_{ij}.$$ Distinct ordered pairs make the two
matrix units independent. For fixed $(i,j)$ this removes all diagonal
differences except possibly its own; the reversed ordered pair removes
that difference as well. Hence $D_{ij}$ is scalar and traceless, and is
zero. We have $R=c\operatorname{id}$. The original relation then makes
$(L-c\operatorname{id})x$ central for every $x$, so
$L=c\operatorname{id}$. ◻
:::

This proof is included for inspectability, with the quasicentroid
attribution in Section [2](#sec:rigidity){reference-type="ref"
reference="sec:rigidity"}. The inherited supplement also verifies a
distinct $512\times128$ formulation of this abstract pair lemma for
$d=3$: a $127$-minor has determinant $32$ modulo $101$, and
$(\operatorname{id},\operatorname{id})$ is the known kernel vector. That
certificate is separate from the two interaction-specific pair
certificates in Lemma [11](#lem:rankdef){reference-type="ref"
reference="lem:rankdef"}.

# Retained cubic witness and a certified perturbation ball {#app:old}

For [\[eq:G\]](#eq:G){reference-type="eqref" reference="eq:G"} and
$j^*=(1,2,3,4,5,6,7,8)$, the interaction is $$\begin{equation}
\label{eq:hstar}
 h_*=\begin{pmatrix}
11&0&0&0&-1&0&0&0&-1\\
0&5&0&3&0&0&0&0&0\\
0&0&-16&0&0&0&9&0&0\\
0&3&0&5&0&0&0&0&0\\
-1&0&0&0&11&0&0&0&-1\\
0&0&0&0&0&-16&0&13&0\\
0&0&9&0&0&0&-16&0&0\\
0&0&0&0&0&13&0&-16&0\\
-1&0&0&0&-1&0&0&0&32
\end{pmatrix}.
\end{equation}$$ Its orthonormal coefficient matrix is
$J_* =\mathop{\mathrm{diag}}(2,4,6,8,10,12,14,48)$. Direct integer
arithmetic gives $$\begin{align*}
 \mathcal O(h_*)&=1848(G_3\otimes G_8-G_8\otimes G_3)\\
 &=3696\mathop{\mathrm{diag}}(0,1,-1,-1,0,1,1,-1,0),\\
 \|\mathcal O(h_*)\|_F^2&=6(3696)^2=81\,962\,496.
\end{align*}$$ The factorised
formula [\[eq:diaggap\]](#eq:diaggap){reference-type="eqref"
reference="eq:diaggap"} follows by expanding
$$\sum_{a,c,e}j_aj_cj_e\mathop{\mathrm{Tr}}(G_e[G_a,G_c])
 \bigl([G_e,G_a]\otimes G_c+G_a\otimes[G_e,G_c]\bigr).$$ Only the
$(3,8)$ and $(8,3)$ basis coefficients survive. The symbolic verifier
checks all coefficients as polynomials in eight indeterminates.

::: {#prop:ball .proposition}
**Proposition 19** (A field-uniform robust neighbourhood). *If $h$ is
Hermitian, swap-symmetric, has zero one-site partial traces and
$\|h-h_*\|_F\le1/10$, then its local commutant
is [\[eq:IH\]](#eq:IH){reference-type="eqref" reference="eq:IH"} for
every choice of fields and every $N\ge6$.*
:::

::: proof
*Proof.* Orthonormality gives $\|J-J_*\|_F=\|h-h_*\|_F$. The eigenvalues
of $J_*$ are positive with minimum $2$ and minimum gap $2$, so the
stated perturbation preserves positivity and simplicity, and hence
simplicity of $J^2$.

For interactions $a,b$, set $M_a=\|a\|_{\mathrm{op}}$,
$M_b=\|b\|_{\mathrm{op}}$ and $\delta=\|a-b\|_F$. Expanding the
difference of the nested commutators and using
$\|[X,Y]\|_F\le2\|X\|_{\mathrm{op}}\|Y\|_F$,
$\|X\otimes I\|_F=\sqrt d\|X\|_F$ and
$\|\mathop{\mathrm{Tr}}_2X\|_F\le\sqrt d\|X\|_F$ gives
$$\|\mathcal O(a)-\mathcal O(b)\|_F
 \le8d\delta(M_a^2+M_aM_b+M_b^2).$$ For clarity, writing $A=a_{12}$,
$B=a_{23}$ and primed letters for $b$, the difference is
$[A+B-A'-B',[A,B]]+[A'+B',[A,B]-[A',B']]$. The two bounds before tracing
are $8\sqrt d\delta M_a^2$ and $8\sqrt d\delta M_b(M_a+M_b)$,
respectively.

The maximum absolute row sum
of [\[eq:hstar\]](#eq:hstar){reference-type="eqref"
reference="eq:hstar"} is $34$, so $M_{h_*}\le34$ and $M_h\le35$.
Consequently $$\|\mathcal O(h)-\mathcal O(h_*)\|_F
 \le\frac{24}{10}(35^2+35\cdot34+34^2)=8570.4
 <\sqrt{81\,962\,496}.$$ The gap obstruction remains nonzero;
Proposition [14](#prop:gap){reference-type="ref" reference="prop:gap"}
and Lemma [15](#lem:abelian){reference-type="ref"
reference="lem:abelian"} finish the proof. ◻
:::

# Certificate conventions and reproducibility {#app:certs}

All matrix indices in the evidence are zero-based. Tensor bases order
the left site first and flatten matrices row by row. The isotropic
certificate `isotropic_W.json` stores exact rational strings. The two
interaction-pair certificates store the integer two-site matrix, the
ordered basis [\[eq:realbasis\]](#eq:realbasis){reference-type="eqref"
reference="eq:realbasis"}, the selected rows and columns, and the
nonzero determinant residue. The $127$-minors use the first $64$ columns
for $a$ and the next $64$ for $b$
in [\[eq:pairlocal\]](#eq:pairlocal){reference-type="eqref"
reference="eq:pairlocal"}.

The two blind-locus files store the eight diagonal $G$ coefficients,
$37$ selected rows, all $37$ augmented columns, and the determinant
modulo $101$. Their matrix is $[9T_h\mid9\Delta]$ in the
real-then-imaginary flattening of
Section [3](#sec:quotient){reference-type="ref"
reference="sec:quotient"}. The factors of $9$ clear the endpoint
projection denominators. Both rank-deficient pair matrices and both
augmented minors are rebuilt from their inputs when checked.

From the bundle directory, install the pinned symbolic dependency and
run:

> python -m pip install -r requirements.txt\
> python verify.py\
> python certify_field_uniform.py evidence/AKLT_input.json

The independent integer checker and the inherited integer checker need
only the Python standard library. Verification reports record actual
results, environment and timings. The checksum manifest protects the
release contents; verification can regenerate timing-bearing reports
without implying their old hashes must remain unchanged. The source
audit distinguishes inspected theorem statements and proofs from
metadata-only or abstract-only comparisons. Original software is
MIT-licensed; original prose and data are dedicated under CC0-1.0, with
third-party exceptions in the licence map. Archival citation metadata
uses the standing scholarly creator Anonymous and the reserved version
DOI printed on the title page; publication itself requires separate
provider readback.

# Acknowledgement of method and review status {#acknowledgement-of-method-and-review-status .unnumbered}

This manuscript was developed with AI-assisted mathematical reasoning
and exact computation. The supplied version-0.1 report motivated the
symmetry analysis and literature corrections. It is included for
provenance; its assessment does not extend automatically to the new
results. Independent review of the quotient equivalence, the
arbitrary-field symmetry step and the complete spin-1 statement is the
principal remaining assurance step.

::: thebibliography
99 Hokkyo, A. (2025). *Rigorous test for quantum integrability and
nonintegrability* (Version 3, 13 April 2025) \[Preprint\].
arXiv:2501.18400.\
<https://arxiv.org/abs/2501.18400v3>

Park, H. K., & Lee, S. (2024). *Proof of nonintegrability of the spin-1
bilinear-biquadratic chain model* \[Preprint\]. arXiv:2410.23286.\
<https://arxiv.org/abs/2410.23286>

Hokkyo, A., Yamaguchi, M., & Chiba, Y. (2025). Absence of nontrivial
local conserved quantities in the spin-1 bilinear-biquadratic chain and
its anisotropic extensions. *Physical Review Research, 7*, 043297.\
<https://doi.org/10.1103/vjtq-sz21>

Sengoku, S., & Watanabe, H. (2026). *Absence of nontrivial local
conserved quantities in a class of $U(1)$-symmetric spin-1 chains*
\[Preprint\]. arXiv:2608.17548.\
<https://arxiv.org/abs/2608.17548>

Shiraishi, N., & Yamaguchi, M. (2026). Dichotomy theorem separating
complete integrability and nonintegrability of isotropic spin chains.
*Physical Review B, 113*, L241111.\
<https://doi.org/10.1103/lcn4-tbcm>

Hokkyo, A. (2026). Integrability from a single conservation law in
quantum spin chains. *Physical Review B, 114*, 055108.\
<https://doi.org/10.1103/y66t-t8zw>

Sanatani, M., Shiraishi, N., & Ishii, F. (2026). *A simple necessary and
sufficient condition for Yang--Baxter integrability* \[Preprint\].
arXiv:2607.29660.\
<https://arxiv.org/abs/2607.29660v1>

Leger, G. F., & Luks, E. M. (2000). Generalized derivations of Lie
algebras. *Journal of Algebra, 228*, 165--203. The quasicentroid
statements are consulted through [@ABR], p. 8.\
<https://www.sciencedirect.com/science/article/pii/S0021869399982509>

Andruszkiewicz, R. R., Brzeziński, T., & Radziszewski, K. (2024). *Lie
affgebras vis-à-vis Lie algebras* \[Preprint\]. arXiv:2409.01996.\
<https://arxiv.org/abs/2409.01996>

Grabowski, M. P., & Mathieu, P. (1995). Integrability test for spin
chains. *Journal of Physics A: Mathematical and General, 28*,
4777--4798.\
<https://doi.org/10.1088/0305-4470/28/17/013>
:::
