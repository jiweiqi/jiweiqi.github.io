# Shared low-dimensional subspaces for propagating kinetic uncertainty to multiple outputs

Weiqi Ji, Jiaxing Wang, Olivier Zahm, Youssef M. Marzouk, Bin Yang, Zhuyin Ren, Chung K. Law

Combustion and Flame, 2018. Journal article.

DOI: https://doi.org/10.1016/j.combustflame.2017.11.021

Canonical page: https://jiweiqi.github.io/papers/shared-subspaces/

## Abstract

Forward propagation of kinetic uncertainty in combustion simulations usually adopts response surface techniques to accelerate Monte Carlo sampling. Yet it is computationally challenging to build response surfaces for high-dimensional input parameters and expensive combustion models. This study uses the active subspace method to identify a low-dimensional subspace of the input space, within which response surfaces can be built. Active subspace methods have previously been developed only for single (scalar) model outputs, however. This paper introduces a new method that can simultaneously approximate the marginal probability density functions of multiple outputs using a single low-dimensional shared subspace. We identify the shared subspace by solving a least-squares system to compute an appropriate combination of single-output active subspaces. Because the identification of the active subspace for each individual output may require a significant number of samples, this process may be computationally intractable for expensive models such as turbulent combustion simulations. Instead, we propose a heuristic approach that learns the relevant subspaces from cheaper combustion models. The performance of the active subspace for a single output, and of the shared subspace for multiple outputs, is first demonstrated with the ignition delay times and laminar flame speeds of hydrogen/air, methane/air, and dimethyl ether (DME)/air mixtures. Then we demonstrate extrapolatory performance of the shared subspace: using a shared subspace trained on the ignition delays at constant volume, we perform forward propagation of kinetic uncertainties through zero-dimensional HCCI simulations—in particular, single-stage ignition of a natural gas/air mixture and two-stage ignition of a DME/air mixture. We show that the shared subspace can accurately reproduce the probability of ignition failure and the probability density of ignition crank angle conditioned on successful ignition, given uncertainty in the kinetics.

## Research summary

Combines single-output active subspaces into a shared low-dimensional representation for propagating kinetic uncertainty to multiple quantities of interest.

Keywords: active subspaces, dimension reduction, multiple outputs, HCCI

## Resources

- [Related GitHub code](https://github.com/DENG-MIT/ArrheniusActiveSubspace)
- [BibTeX](https://jiweiqi.github.io/papers/shared-subspaces/citation.bib)

## Sources

- https://doi.org/10.1016/j.combustflame.2017.11.021
- https://uqgroup.mit.edu/publications/
- https://github.com/DENG-MIT/ArrheniusActiveSubspace

## Citation

```bibtex
@article{sharedsubspaces2018,
  title = {{Shared low-dimensional subspaces for propagating kinetic uncertainty to multiple outputs}},
  author = {Weiqi Ji and Jiaxing Wang and Olivier Zahm and Youssef M. Marzouk and Bin Yang and Zhuyin Ren and Chung K. Law},
  year = {2018},
  journal = {Combustion and Flame},
  volume = {190},
  pages = {146-157},
  doi = {10.1016/j.combustflame.2017.11.021},
  url = {https://jiweiqi.github.io/papers/shared-subspaces/}
}
```
