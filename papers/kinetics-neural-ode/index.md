# Kinetics parameter optimization of hydrocarbon fuels via neural ordinary differential equations

Xingyu Su, Weiqi Ji, Jian An, Zhuyin Ren, Sili Deng, Chung K. Law

Combustion and Flame, 2023. Journal article.

DOI: https://doi.org/10.1016/j.combustflame.2023.112732

Canonical page: https://jiweiqi.github.io/papers/kinetics-neural-ode/

## Abstract

Chemical kinetics mechanisms are essential for understanding, analyzing, and simulating complex combustion phenomena. In this study, a neural ordinary differential equation (Neural ODE) framework is employed to optimize the kinetics parameters of reaction mechanisms. Given experimental or high-cost simulated observations as training data, the proposed algorithm can optimally recover the hidden characteristics in the data. Different datasets of various sizes, types, and noise levels are systematically tested. A classic toy problem of stiff Robertson ODE is first used to demonstrate the learning capability, efficiency, and robustness of the Neural ODE approach. A 41-species, 232-reactions JP-10 skeletal mechanism and a 34-species, 121-reactions n-heptane skeletal mechanism are then optimized with species' temporal profiles and ignition delay times, respectively. Results show that the proposed algorithm can optimize stiff chemical models with sufficient accuracy, efficiency and robustness. It is noted that the trained mechanism not only fits the data perfectly but also retains its physical interpretability, which can be further integrated and validated in practical turbulent combustion simulations. In addition, as demonstrated with the stiff Robertson problem, it is promising to adopt Bayesian inference techniques with Neural ODE to estimate the kinetics parameter uncertainties from experimental data.

## Research summary

Treats kinetic parameter optimization as neural ODE training to calibrate hydrocarbon-fuel models against experimental targets.

将动力学参数优化表述为神经 ODE 训练，利用实验目标标定碳氢燃料模型。

Keywords: neural ODEs, parameter optimization, hydrocarbon fuels

## Resources

- [PDF](https://jiweiqi.github.io/papers/kinetics-neural-ode/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/kinetics-neural-ode/fulltext.txt)
- [BibTeX](https://jiweiqi.github.io/papers/kinetics-neural-ode/citation.bib)

## Sources

- https://doi.org/10.1016/j.combustflame.2023.112732
- https://arxiv.org/abs/2209.01862
- https://hdl.handle.net/1721.1/156212

## Citation

```bibtex
@article{kineticsneuralode2023,
  title = {{Kinetics parameter optimization of hydrocarbon fuels via neural ordinary differential equations}},
  author = {Xingyu Su and Weiqi Ji and Jian An and Zhuyin Ren and Sili Deng and Chung K. Law},
  year = {2023},
  journal = {Combustion and Flame},
  volume = {251},
  pages = {112732},
  doi = {10.1016/j.combustflame.2023.112732},
  eprint = {2209.01862},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/kinetics-neural-ode/}
}
```
