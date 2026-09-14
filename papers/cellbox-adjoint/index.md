# Inference of cell dynamics on perturbation data using adjoint sensitivity

Weiqi Ji, Bo Yuan, Ciyue Shen, Aviv Regev, Chris Sander, Sili Deng

ICLR 2021 Workshop on Deep Learning for Simulation (SimDL), 2021. Workshop paper.

DOI: https://doi.org/10.48550/arxiv.2104.06467

Canonical page: https://jiweiqi.github.io/papers/cellbox-adjoint/

## Abstract

Data-driven dynamic models of cell biology can be used to predict cell response to unseen perturbations. Recent work (CellBox) had demonstrated the derivation of interpretable models with explicit interaction terms, in which the parameters were optimized using machine learning techniques. While the previous work was tested only in a single biological setting, this work aims to extend the range of applicability of this model inference approach to a diversity of biological systems. Here we adapted CellBox in Julia differential programming and augmented the method with adjoint algorithms, which has recently been used in the context of neural ODEs. We trained the models using simulated data from both abstract and biology-inspired networks, which afford the ability to evaluate the recovery of the ground truth network structure. The resulting accuracy of prediction by these models is high both in terms of low error against data and excellent agreement with the network structure used for the simulated training data. While there is no analogous ground truth for real life biological systems, this work demonstrates the ability to construct and parameterize a considerable diversity of network models with high predictive ability. The expectation is that this kind of procedure can be used on real perturbation-response data to derive models applicable to diverse biological systems.

## Research summary

Uses adjoint sensitivity and differentiable programming to infer cell-network dynamics from simulated perturbation-response data.

结合伴随灵敏度与可微编程，从模拟扰动响应数据推断细胞网络动力学。

Keywords: adjoint sensitivity, CellBox, network inference, systems biology

## Resources

- [PDF](https://jiweiqi.github.io/papers/cellbox-adjoint/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/cellbox-adjoint/fulltext.txt)
- [Code](https://github.com/jiweiqi/CellBox.jl)
- [BibTeX](https://jiweiqi.github.io/papers/cellbox-adjoint/citation.bib)

## Sources

- https://doi.org/10.48550/arxiv.2104.06467
- https://arxiv.org/abs/2104.06467
- https://simdl.github.io/papers/

## Citation

```bibtex
@inproceedings{cellboxadjoint2021,
  title = {{Inference of cell dynamics on perturbation data using adjoint sensitivity}},
  author = {Weiqi Ji and Bo Yuan and Ciyue Shen and Aviv Regev and Chris Sander and Sili Deng},
  year = {2021},
  booktitle = {ICLR 2021 Workshop on Deep Learning for Simulation (SimDL)},
  doi = {10.48550/arxiv.2104.06467},
  eprint = {2104.06467},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/cellbox-adjoint/}
}
```
