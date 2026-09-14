# SGD-based optimization in modeling combustion kinetics: Case studies in tuning mechanistic and hybrid kinetic models

Weiqi Ji, Xingyu Su, Bin Pang, Yujuan Li, Zhuyin Ren, Sili Deng

Fuel, 2022. Journal article.

DOI: https://doi.org/10.1016/j.fuel.2022.124560

Canonical page: https://jiweiqi.github.io/papers/sgd-kinetics/

## Abstract

Chemical kinetic modeling is an integral part of combustion simulation, and extensive efforts have been devoted to developing high-fidelity yet computationally affordable models. Despite these efforts, modeling combustion kinetics is still challenging due to the demand for expert knowledge and high dimensional optimization against experiments. Therefore, data-driven approaches that enable efficient discovery and calibration of kinetic models have received much attention in recent years, the core of which is the high-dimensional optimization based on big data. Evolutionary algorithms are usually adopted for optimizing chemical kinetic models, although they usually suffer from high computational costs and are limited to a small number of parameters. Meanwhile, gradient-based optimizations, especially the stochastic gradient descent (SGD) methods, have shown success in developing complex models by training large-scale deep learning models. Therefore, this work explores the applications of SGD-based optimizations in tuning mechanistic kinetic models and learning hybrid kinetic models. We first showed that SGD-based optimizations could substantially save computational cost compared to evolutionary algorithms when the number of kinetic parameters in mechanistic models reached about one hundred. We then demonstrated that the SGD-based optimization enabled us to use a neural network model to represent the pyrolysis of the Hybrid Chemistry and optimize the associated hundreds of weights in the neural network. These proof-of-concept studies showed that the SGD-based optimization is more efficient than evolutionary algorithms, is a promising approach for developing chemical kinetic models with high dimensional parameters, and is capable of developing hybrid mechanistic-machine learning kinetic models.

## Research summary

Uses differentiable simulation and stochastic gradient descent to optimize mechanistic and hybrid chemical kinetic models.

结合可微模拟与随机梯度下降，优化机理型和混合型化学动力学模型。

Keywords: SGD, differentiable programming, hybrid modeling

## Resources

- [PDF](https://jiweiqi.github.io/papers/sgd-kinetics/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/sgd-kinetics/fulltext.txt)
- [Code](https://github.com/DENG-MIT/Arrhenius.jl)
- [BibTeX](https://jiweiqi.github.io/papers/sgd-kinetics/citation.bib)

## Sources

- https://doi.org/10.1016/j.fuel.2022.124560
- https://hdl.handle.net/1721.1/156214

## Citation

```bibtex
@article{sgdkinetics2022,
  title = {{SGD-based optimization in modeling combustion kinetics: Case studies in tuning mechanistic and hybrid kinetic models}},
  author = {Weiqi Ji and Xingyu Su and Bin Pang and Yujuan Li and Zhuyin Ren and Sili Deng},
  year = {2022},
  journal = {Fuel},
  volume = {324},
  pages = {124560},
  doi = {10.1016/j.fuel.2022.124560},
  url = {https://jiweiqi.github.io/papers/sgd-kinetics/}
}
```
