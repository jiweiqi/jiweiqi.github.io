# Kinetic subspace investigation using neural network for uncertainty quantification in nonpremixed flamelets

Benjamin C. Koenig, Weiqi Ji, Sili Deng

Proceedings of the Combustion Institute, 2023. Journal article.

DOI: https://doi.org/10.1016/j.proci.2022.07.226

Canonical page: https://jiweiqi.github.io/papers/flamelet-subspace/

## Abstract

Propagating uncertainties in kinetic models through turbulent combustion simulations to properly quantify the uncertainties in the simulation results remains a challenging and numerically expensive problem. Efficient approaches have been proposed for certain flames in the flamelet region by reducing their uncertainty input from a high-dimensional kinetic parameter space to a one-dimensional variable. However, this one-dimensional assumption does not apply to all flamelet regimes. In the current work, we developed a systematic approach to discover low-dimensional active subspace reductions that apply to the entire mixture fraction space of the flamelet, and that function even in cases where the uncertainty response is not uniform across the entire solution domain and the one-dimensional assumption does not apply. In doing so, we are able to achieve uncertainty quantification with a tunable tradeoff between high accuracy and low computational cost through careful selection of subspace dimensionality. We facilitated computation in this method using a specifically designed deep neural network based surrogate model to compute the temperature gradients of the flamelet profile to the kinetic parameters. We presented, as a proof-of-concept, a two-stage active subspace reduction on the kinetic parameter space of a nonpremixed methane flamelet. In doing so we demonstrated that its uncertainty response cannot be represented by a one-dimensional kinetic variable due to its uncorrelated behavior across the mixture fraction domain. We instead proposed a four-dimensional active subspace that captures 98% of the uncertainty response in the flame profile at largely reduced computational cost compared to the full kinetic parameter space. The tunability, generality, and reduced computational cost of this method demonstrate its potential to facilitate uncertainty quantification of complex and large-scale combustion problems.

## Research summary

Uses a neural-network surrogate to identify multidimensional kinetic subspaces for uncertainty propagation across nonpremixed flamelet profiles.

以神经网络代理计算梯度，识别覆盖非预混火焰片空间分布的多维动力学子空间。

Keywords: active subspaces, neural surrogates, flamelets, uncertainty quantification

## Resources

- [PDF](https://jiweiqi.github.io/papers/flamelet-subspace/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/flamelet-subspace/fulltext.txt)
- [BibTeX](https://jiweiqi.github.io/papers/flamelet-subspace/citation.bib)

## Sources

- https://doi.org/10.1016/j.proci.2022.07.226
- https://hdl.handle.net/1721.1/156211

## Citation

```bibtex
@article{flameletsubspace2023,
  title = {{Kinetic subspace investigation using neural network for uncertainty quantification in nonpremixed flamelets}},
  author = {Benjamin C. Koenig and Weiqi Ji and Sili Deng},
  year = {2023},
  journal = {Proceedings of the Combustion Institute},
  volume = {39},
  pages = {5229-5238},
  doi = {10.1016/j.proci.2022.07.226},
  number = {4},
  url = {https://jiweiqi.github.io/papers/flamelet-subspace/}
}
```
