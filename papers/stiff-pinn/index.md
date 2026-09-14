# Stiff-PINN: Physics-Informed Neural Network for Stiff Chemical Kinetics

Weiqi Ji, Weilun Qiu, Zhiyu Shi, Shaowu Pan, Sili Deng

The Journal of Physical Chemistry A, 2021. Journal article.

DOI: https://doi.org/10.1021/acs.jpca.1c05102

Canonical page: https://jiweiqi.github.io/papers/stiff-pinn/

## Abstract

The recently developed physics-informed neural network (PINN) has achieved success in many science and engineering disciplines by encoding physics laws into the loss functions of the neural network such that the network not only conforms to the measurements and initial and boundary conditions but also satisfies the governing equations. This work first investigates the performance of the PINN in solving stiff chemical kinetic problems with governing equations of stiff ordinary differential equations (ODEs). The results elucidate the challenges of utilizing the PINN in stiff ODE systems. Consequently, we employ quasi-steady-state assumption (QSSA) to reduce the stiffness of the ODE systems, and the PINN then can be successfully applied to the converted non-/mild-stiff systems. Therefore, the results suggest that stiffness could be the major reason for the failure of the regular PINN in the studied stiff chemical kinetic systems. The developed stiff-PINN approach that utilizes QSSA to enable the PINN to solve stiff chemical kinetics shall open the possibility of applying the PINN to various reaction-diffusion systems involving stiff dynamics.

## Research summary

Examines PINN failure on stiff chemical kinetics and uses quasi-steady-state reduction to make the studied systems tractable.

Keywords: PINNs, stiff systems, QSSA, chemical kinetics

## Resources

- [PDF](https://jiweiqi.github.io/papers/stiff-pinn/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/stiff-pinn/fulltext.txt)
- [GitHub](https://github.com/DENG-MIT/Stiff-PINN)
- [BibTeX](https://jiweiqi.github.io/papers/stiff-pinn/citation.bib)

## Sources

- https://doi.org/10.1021/acs.jpca.1c05102
- https://arxiv.org/abs/2011.04520
- https://hdl.handle.net/1721.1/138718

## Citation

```bibtex
@article{stiffpinn2021,
  title = {{Stiff-PINN: Physics-Informed Neural Network for Stiff Chemical Kinetics}},
  author = {Weiqi Ji and Weilun Qiu and Zhiyu Shi and Shaowu Pan and Sili Deng},
  year = {2021},
  journal = {The Journal of Physical Chemistry A},
  volume = {125},
  pages = {8098-8106},
  doi = {10.1021/acs.jpca.1c05102},
  number = {36},
  eprint = {2011.04520},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/stiff-pinn/}
}
```
