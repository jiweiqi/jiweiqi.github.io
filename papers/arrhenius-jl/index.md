# Arrhenius.jl: A Differentiable Combustion Simulation Package

Weiqi Ji, Xingyu Su, Bin Pang, Séan J. Cassady, Alison M. Ferris, Yujuan Li, Zhuyin Ren, Ronald K. Hanson, Sili Deng

arXiv, 2021. Preprint.

DOI: https://doi.org/10.48550/arxiv.2107.06172

Canonical page: https://jiweiqi.github.io/papers/arrhenius-jl/

## Abstract

Combustion kinetic modeling is an integral part of combustion simulation, and extensive studies have been devoted to developing both high fidelity and computationally affordable models. Despite these efforts, modeling combustion kinetics is still challenging due to the demand for expert knowledge and optimization against experiments, as well as the lack of understanding of the associated uncertainties. Therefore, data-driven approaches that enable efficient discovery and calibration of kinetic models have received much attention in recent years, the core of which is the optimization based on big data. Differentiable programming is a promising approach for learning kinetic models from data by efficiently computing the gradient of objective functions to model parameters. However, it is often challenging to implement differentiable programming in practice. Therefore, it is still not available in widely utilized combustion simulation packages such as CHEMKIN and Cantera. Here, we present a differentiable combustion simulation package leveraging the eco-system in Julia, including DifferentialEquations.jl for solving differential equations, ForwardDiff.jl for auto-differentiation, and Flux.jl for incorporating neural network models into combustion simulations and optimizing neural network models using the state-of-the-art deep learning optimizers. We demonstrate the benefits of differentiable programming in efficient and accurate gradient computations, with applications in uncertainty quantification, kinetic model reduction, data assimilation, and model discovery.

## Research summary

Introduces differentiable combustion modeling in Julia for gradient-based sensitivity analysis, calibration, uncertainty quantification and model discovery.

Keywords: differentiable programming, Julia, Arrhenius.jl, UQ

## Resources

- [PDF](https://jiweiqi.github.io/papers/arrhenius-jl/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/arrhenius-jl/fulltext.txt)
- [GitHub](https://github.com/DENG-MIT/Arrhenius.jl)
- [BibTeX](https://jiweiqi.github.io/papers/arrhenius-jl/citation.bib)

## Sources

- https://doi.org/10.48550/arxiv.2107.06172
- https://arxiv.org/abs/2107.06172

## Citation

```bibtex
@misc{arrheniusjl2021,
  title = {{Arrhenius.jl: A Differentiable Combustion Simulation Package}},
  author = {Weiqi Ji and Xingyu Su and Bin Pang and Séan J. Cassady and Alison M. Ferris and Yujuan Li and Zhuyin Ren and Ronald K. Hanson and Sili Deng},
  year = {2021},
  howpublished = {arXiv},
  doi = {10.48550/arxiv.2107.06172},
  eprint = {2107.06172},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/arrhenius-jl/}
}
```
