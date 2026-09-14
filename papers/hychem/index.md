# Data-Driven Approaches to Learn HyChem Models

Weiqi Ji, Julian Zanders, Ji-Woong Park, Sili Deng

ASME ICEF 2021, 2021. Conference paper.

DOI: https://doi.org/10.1115/icef2021-67925

Canonical page: https://jiweiqi.github.io/papers/hychem/

## Abstract

<jats:title>Abstract</jats:title>
               <jats:p>The HyChem (Hybrid Chemistry) approach has recently been proposed for modeling high-temperature combustion of real, multi-component fuels. The approach combines lumped reaction steps for fuel thermal and oxidative pyrolysis with detailed chemistry for the oxidation of the resulting pyrolysis products. Determining the pyrolysis submodel requires extensive experimentation on speciation measurements. Recent work has been directed to learn HyChem from an existing HyChem model for a similar fuel, which requires less data. However, the approach usually shows substantial discrepancies with experimental data within the Negative Temperature Coefficient (NTC) regime, as the low-temperature chemistry is more fuel-specific than high-temperature chemistry. This paper proposes a machine learning approach to learn the HyChem models that can cover both high-temperature and low-temperature regimes. Specifically, we develop a HyChem model using the experimental datasets of ignition delay times covering a wide range of temperatures and equivalence ratios. The chemical kinetic model is treated as a neural network model, and we then employ stochastic gradient descent (SGD), a technique that was developed for deep learning, for the training. We demonstrate the approach in learning the HyChem model for F-24, which is a Jet-A derived fuel, and compare the results with previous work employing genetic algorithms. The results show that the SGD approach can achieve comparable model performance with genetic algorithms but the computational cost is reduced by 1000 times. In addition, with regularization in SGD, the SGD approach changes the kinetic parameters from their original values much less than genetic algorithm and is thus more likely to retrain mechanistic meanings. Finally, our approach is built upon open-source packages and can be applied to the development and optimization of chemical kinetic models for internal combustion engine simulations.</jats:p>

## Research summary

Applies stochastic gradient descent to calibrate lumped HyChem fuel models against ignition-delay measurements across temperature regimes.

使用随机梯度下降，在多个温度区间根据点火延迟实验标定 HyChem 集总燃料模型。

Keywords: SGD, HyChem, kinetic calibration, jet fuels

## Resources

- [PDF](https://jiweiqi.github.io/papers/hychem/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/hychem/fulltext.txt)
- [BibTeX](https://jiweiqi.github.io/papers/hychem/citation.bib)

## Sources

- https://doi.org/10.1115/icef2021-67925
- https://arxiv.org/abs/2104.07875
- https://hdl.handle.net/1721.1/150935

## Citation

```bibtex
@inproceedings{hychem2021,
  title = {{Data-Driven Approaches to Learn HyChem Models}},
  author = {Weiqi Ji and Julian Zanders and Ji-Woong Park and Sili Deng},
  year = {2021},
  booktitle = {ASME ICEF 2021},
  doi = {10.1115/icef2021-67925},
  eprint = {2104.07875},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/hychem/}
}
```
