# Neural Differential Equations for Inverse Modeling in Model Combustors

Xingyu Su, Weiqi Ji, Long Zhang, Wantong Wu, Zhuyin Ren, Sili Deng

ASME IMECE 2021, 2021. Conference paper.

DOI: https://doi.org/10.1115/imece2021-69657

Canonical page: https://jiweiqi.github.io/papers/inverse-combustors/

## Abstract

Abstract
               Monitoring the dynamics processes in combustors is crucial for safe and efficient operations. However, in practice, only limited data can be obtained due to limitations in the measurable quantities, visualization window, and temporal resolution. This work proposes an approach based on neural differential equations to approximate the unknown quantities from available sparse measurements. The approach tackles the challenges of nonlinearity and the curse of dimensionality in inverse modeling by representing the dynamic signal using neural network models. In addition, we augment physical models for combustion with neural differential equations to enable learning from sparse measurements. We demonstrated the inverse modeling approach in a model combustor system by simulating the oscillation of an industrial combustor with a perfectly stirred reactor. Given the sparse measurements of the temperature inside the combustor, upstream fluctuations in compositions and/or flow rates can be inferred. Various types of fluctuations in the upstream, as well as the responses in the combustor, were synthesized to train and validate the algorithm. The results demonstrated that the approach can efficiently and accurately infer the dynamics of the unknown inlet boundary conditions, even without assuming the types of fluctuations. Those demonstrations shall open a lot of opportunities in utilizing neural differential equations for fault diagnostics and model-based dynamic control of industrial power systems.

## Research summary

Infers unknown inlet composition and flow fluctuations from sparse combustor-temperature measurements using neural differential equations.

利用神经微分方程，从稀疏燃烧室温度观测反演入口组分与流量波动。

Keywords: inverse problems, neural differential equations, combustor dynamics

## Resources

- [PDF](https://jiweiqi.github.io/papers/inverse-combustors/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/inverse-combustors/fulltext.txt)
- [BibTeX](https://jiweiqi.github.io/papers/inverse-combustors/citation.bib)

## Sources

- https://doi.org/10.1115/imece2021-69657
- https://arxiv.org/abs/2107.11510

## Citation

```bibtex
@inproceedings{inversecombustors2021,
  title = {{Neural Differential Equations for Inverse Modeling in Model Combustors}},
  author = {Xingyu Su and Weiqi Ji and Long Zhang and Wantong Wu and Zhuyin Ren and Sili Deng},
  year = {2021},
  booktitle = {ASME IMECE 2021},
  doi = {10.1115/imece2021-69657},
  eprint = {2107.11510},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/inverse-combustors/}
}
```
