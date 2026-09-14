# Stiff neural ordinary differential equations

Suyong Kim, Weiqi Ji, Sili Deng, Yingbo Ma, Christopher Rackauckas

Chaos: An Interdisciplinary Journal of Nonlinear Science, 2021. Journal article.

DOI: https://doi.org/10.1063/5.0060697

Canonical page: https://jiweiqi.github.io/papers/stiff-neural-ode/

## Abstract

Neural Ordinary Differential Equations (ODE) are a promising approach to
learn dynamic models from time-series data in science and engineering
applications. This work aims at learning Neural ODE for stiff systems, which
are usually raised from chemical kinetic modeling in chemical and biological
systems. We first show the challenges of learning neural ODE in the classical
stiff ODE systems of Robertson's problem and propose techniques to mitigate the
challenges associated with scale separations in stiff systems. We then present
successful demonstrations in stiff systems of Robertson's problem and an air
pollution problem. The demonstrations show that the usage of deep networks with
rectified activations, proper scaling of the network outputs as well as loss
functions, and stabilized gradient calculations are the key techniques enabling
the learning of stiff neural ODE. The success of learning stiff neural ODE
opens up possibilities of using neural ODEs in applications with widely varying
time-scales, like chemical dynamics in energy conversion, environmental
engineering, and the life sciences.

## Research summary

Studies stiff neural ODE training using scale-aware architectures, output and loss scaling, and stabilized gradient calculations.

通过网络结构、输出与损失尺度处理及稳定梯度计算，学习刚性神经常微分方程。

Keywords: neural ODEs, stiff systems, differentiable simulation

## Resources

- [PDF](https://jiweiqi.github.io/papers/stiff-neural-ode/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/stiff-neural-ode/fulltext.txt)
- [Code](https://github.com/DENG-MIT/StiffNeuralODE)
- [BibTeX](https://jiweiqi.github.io/papers/stiff-neural-ode/citation.bib)

## Sources

- https://doi.org/10.1063/5.0060697
- https://arxiv.org/abs/2103.15341
- https://hdl.handle.net/1721.1/138719

## Citation

```bibtex
@article{stiffneuralode2021,
  title = {{Stiff neural ordinary differential equations}},
  author = {Suyong Kim and Weiqi Ji and Sili Deng and Yingbo Ma and Christopher Rackauckas},
  year = {2021},
  journal = {Chaos: An Interdisciplinary Journal of Nonlinear Science},
  volume = {31},
  pages = {093122},
  doi = {10.1063/5.0060697},
  number = {9},
  eprint = {2103.15341},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/stiff-neural-ode/}
}
```
