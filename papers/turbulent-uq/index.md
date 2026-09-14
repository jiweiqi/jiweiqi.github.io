# Quantifying kinetic uncertainty in turbulent combustion simulations using active subspaces

Weiqi Ji, Zhuyin Ren, Youssef Marzouk, Chung K. Law

Proceedings of the Combustion Institute, 2019. Journal article.

DOI: https://doi.org/10.1016/j.proci.2018.06.206

Canonical page: https://jiweiqi.github.io/papers/turbulent-uq/

## Abstract

Uncertainty quantification in expensive turbulent combustion simulations usually adopts response surface techniques to accelerate Monte Carlo sampling. However, it is computationally intractable to build response surfaces for high-dimensional kinetic parameters. We employ the active subspaces approach to reduce the dimension of the parameter space, such that building a response surface on the resulting low-dimensional subspace requires many fewer runs of the expensive simulation, rendering the approach suitable for various turbulent combustion models. We demonstrate this approach in simulations of the Cabra H 2 /N 2 jet flame, propagating the uncertainties of 21 kinetic parameters to the liftoff height. We identify a one-dimensional active subspace for the liftoff height using 84 runs of the simulations, from which a response surface with a one-dimensional input is built; the probability distribution of the liftoff height is then characterized by evaluating a large number of samples using the inexpensive response surface. In addition, the active subspace provides a global sensitivity metric for determining the most influential reactions. Comparison with autoignition tests reveals that the sensitivities to the HO 2 -related reactions in the Cabra flame are promoted by the diffusion processes. The present work demonstrates the capability of active subspaces in quantifying uncertainty in turbulent combustion simulations and provides physical insights into the flame via the active subspace-based sensitivity metric.

## Research summary

Uses active subspaces and response surfaces to propagate kinetic uncertainty to the liftoff height of a turbulent Cabra hydrogen jet flame.

通过主动子空间与响应面，将化学动力学参数不确定性传播至 Cabra 湍流火焰的抬升高度。

Keywords: active subspaces, turbulent combustion, uncertainty propagation

## Resources

- [PDF](https://jiweiqi.github.io/papers/turbulent-uq/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/turbulent-uq/fulltext.txt)
- [BibTeX](https://jiweiqi.github.io/papers/turbulent-uq/citation.bib)

## Sources

- https://doi.org/10.1016/j.proci.2018.06.206
- https://hdl.handle.net/1721.1/126335

## Citation

```bibtex
@article{turbulentuq2019,
  title = {{Quantifying kinetic uncertainty in turbulent combustion simulations using active subspaces}},
  author = {Weiqi Ji and Zhuyin Ren and Youssef Marzouk and Chung K. Law},
  year = {2019},
  journal = {Proceedings of the Combustion Institute},
  volume = {37},
  pages = {2175-2182},
  doi = {10.1016/j.proci.2018.06.206},
  number = {2},
  url = {https://jiweiqi.github.io/papers/turbulent-uq/}
}
```
