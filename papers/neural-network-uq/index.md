# Uncertainty Propagation in Deep Neural Network Using Active Subspace

Weiqi Ji, Zhuyin Ren, Chung K. Law

arXiv, 2019. Preprint.

DOI: https://doi.org/10.48550/arxiv.1903.03989

Canonical page: https://jiweiqi.github.io/papers/neural-network-uq/

## Abstract

The inputs of deep neural network (DNN) from real-world data usually come with uncertainties. Yet, it is challenging to propagate the uncertainty in the input features to the DNN predictions at a low computational cost. This work employs a gradient-based subspace method and response surface technique to accelerate the uncertainty propagation in DNN. Specifically, the active subspace method is employed to identify the most important subspace in the input features using the gradient of the DNN output to the inputs. Then the response surface within that low-dimensional subspace can be efficiently built, and the uncertainty of the prediction can be acquired by evaluating the computationally cheap response surface instead of the DNN models. In addition, the subspace can help explain the adversarial examples. The approach is demonstrated in MNIST datasets with a convolutional neural network. Code is available at: https://github.com/jiweiqi/nnsubspace.

## Research summary

Builds response surfaces in gradient-based active subspaces to propagate uncertain neural-network inputs at reduced computational cost.

Keywords: active subspaces, neural networks, input uncertainty, surrogate models

## Resources

- [PDF](https://jiweiqi.github.io/papers/neural-network-uq/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/neural-network-uq/fulltext.txt)
- [GitHub](https://github.com/jiweiqi/nnsubspace)
- [BibTeX](https://jiweiqi.github.io/papers/neural-network-uq/citation.bib)

## Sources

- https://doi.org/10.48550/arxiv.1903.03989
- https://arxiv.org/abs/1903.03989

## Citation

```bibtex
@misc{neuralnetworkuq2019,
  title = {{Uncertainty Propagation in Deep Neural Network Using Active Subspace}},
  author = {Weiqi Ji and Zhuyin Ren and Chung K. Law},
  year = {2019},
  howpublished = {arXiv},
  doi = {10.48550/arxiv.1903.03989},
  eprint = {1903.03989},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/neural-network-uq/}
}
```
