# Autonomous Discovery of Unknown Reaction Pathways from Data by Chemical Reaction Neural Network

Weiqi Ji, Sili Deng

The Journal of Physical Chemistry A, 2021. Journal article.

DOI: https://doi.org/10.1021/acs.jpca.0c09316

Canonical page: https://jiweiqi.github.io/papers/crnn/

## Abstract

Chemical reactions occur in energy, environmental, biological, and many other natural systems, and the inference of the reaction networks is essential to understand and design the chemical processes in engineering and life sciences. Yet, revealing the reaction pathways for complex systems and processes is still challenging because of the lack of knowledge of the involved species and reactions. Here, we present a neural network approach that autonomously discovers reaction pathways from the time-resolved species concentration data. The proposed chemical reaction neural network (CRNN), by design, satisfies the fundamental physics laws, including the law of mass action and the Arrhenius law. Consequently, the CRNN is physically interpretable such that the reaction pathways can be interpreted, and the kinetic parameters can be quantified simultaneously from the weights of the neural network. The inference of the chemical pathways is accomplished by training the CRNN with species concentration data via stochastic gradient descent. We demonstrate the successful implementations and the robustness of the approach in elucidating the chemical reaction pathways of several chemical engineering and biochemical systems. The autonomous inference by the CRNN approach precludes the need for expert knowledge in proposing candidate networks and addresses the curse of dimensionality in complex systems. The physical interpretability also makes the CRNN capable of not only fitting the data for a given system but also developing knowledge of unknown pathways that could be generalized to similar chemical systems.

## Research summary

Infers interpretable reaction pathways and kinetic parameters from concentration time series using a neural architecture based on mass-action and Arrhenius laws.

Keywords: CRNN, reaction discovery, neural ODEs, interpretable models

## Resources

- [PDF](https://jiweiqi.github.io/papers/crnn/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/crnn/fulltext.txt)
- [GitHub](https://github.com/DENG-MIT/CRNN)
- [BibTeX](https://jiweiqi.github.io/papers/crnn/citation.bib)

## Sources

- https://doi.org/10.1021/acs.jpca.0c09316
- https://arxiv.org/abs/2002.09062

## Citation

```bibtex
@article{crnn2021,
  title = {{Autonomous Discovery of Unknown Reaction Pathways from Data by Chemical Reaction Neural Network}},
  author = {Weiqi Ji and Sili Deng},
  year = {2021},
  journal = {The Journal of Physical Chemistry A},
  volume = {125},
  pages = {1082-1092},
  doi = {10.1021/acs.jpca.0c09316},
  number = {4},
  eprint = {2002.09062},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/crnn/}
}
```
