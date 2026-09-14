# Autonomous kinetic modeling of biomass pyrolysis using chemical reaction neural networks

Weiqi Ji, Franz Richter, Michael J. Gollner, Sili Deng

Combustion and Flame, 2022. Journal article.

DOI: https://doi.org/10.1016/j.combustflame.2022.111992

Canonical page: https://jiweiqi.github.io/papers/biomass-crnn/

## Abstract

Modeling the burning processes of biomass such as wood, grass, and crops is crucial for the modeling and prediction of wildland and urban fire behavior. Despite its importance, the burning of solid fuels remains poorly understood, which can be partly attributed to the unknown chemical kinetics of most solid fuels. Most available kinetic models were built upon expert knowledge, which requires chemical insights and years of experience. This work presents a framework for autonomously discovering biomass pyrolysis kinetic models from thermogravimetric analyzer (TGA) experimental data using the recently developed chemical reaction neural networks (CRNN). The approach incorporated the CRNN model into the framework of neural ordinary differential equations to predict the residual mass in TGA data. In addition to the flexibility of neural-network-based models, the learned CRNN model is interpretable, by incorporating the fundamental physics laws, such as the law of mass action and Arrhenius law, into the neural network structure. The learned CRNN model can then be translated into the classical forms of biomass chemical kinetic models, which facilitates the extraction of chemical insights and the integration of the kinetic model into large-scale fire simulations. We demonstrated the effectiveness of the framework in predicting the pyrolysis and oxidation of cellulose. This successful demonstration opens the possibility of rapid and autonomous chemical kinetic modeling of solid fuels, such as wildfire fuels and industrial polymers.

## Research summary

Learns biomass pyrolysis kinetics from thermogravimetric measurements with interpretable chemical reaction neural networks.

通过可解释化学反应神经网络，从热重实验中学习生物质热解动力学。

Keywords: CRNN, biomass pyrolysis, model discovery

## Resources

- [PDF](https://jiweiqi.github.io/papers/biomass-crnn/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/biomass-crnn/fulltext.txt)
- [Code](https://github.com/DENG-MIT/Biomass.jl)
- [BibTeX](https://jiweiqi.github.io/papers/biomass-crnn/citation.bib)

## Sources

- https://doi.org/10.1016/j.combustflame.2022.111992
- https://arxiv.org/abs/2105.11397
- https://hdl.handle.net/1721.1/156213

## Citation

```bibtex
@article{biomasscrnn2022,
  title = {{Autonomous kinetic modeling of biomass pyrolysis using chemical reaction neural networks}},
  author = {Weiqi Ji and Franz Richter and Michael J. Gollner and Sili Deng},
  year = {2022},
  journal = {Combustion and Flame},
  volume = {240},
  pages = {111992},
  doi = {10.1016/j.combustflame.2022.111992},
  eprint = {2105.11397},
  archivePrefix = {arXiv},
  url = {https://jiweiqi.github.io/papers/biomass-crnn/}
}
```
