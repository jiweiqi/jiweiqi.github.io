# Using shock tube species time-histories in Bayesian parameter estimation: Effective independent-data number and target selection

Huaibo Chen, Weiqi Ji, Séan J. Cassady, Alison M. Ferris, Ronald K. Hanson, Sili Deng

Proceedings of the Combustion Institute, 2023. Journal article.

DOI: https://doi.org/10.1016/j.proci.2022.08.118

Canonical page: https://jiweiqi.github.io/papers/shock-tube-bayes/

## Abstract

Species time-histories in shock tube experiments provide rich kinetic information for parameter estimation, but there are two problems in using these data in Bayesian approaches. First, the effective independent-data number is not equal to the number of data points in a curve, so brute multiplication of all data points in likelihood function can weaken the constraints from prior information. Second, taking all points of a curve as targets can lead to results different from that of taking several representative points in the curve. In this paper, we employed maximum a posteriori estimation combined with a neural network response surface to optimize a propane mechanism against multispecies time-histories of propane pyrolysis in a shock tube. Three methods of calculating the likelihood function are used: multiplying all points in a curve (C-160), taking the averaged likelihood in each point (C-1), and taking the likelihood of last points (LastP). The influence of effective independent-data number was studied by comparing C-1 and C-160. It was found that C-160 performed slightly better in fitting experimental data, but brute multiplication overtuned the rate constants beyond a reasonable range. The larger the effective independent-data number, the more severe the overtuning, leading to only a slight improvement of model predictions. The influence of target selection is investigated by comparing LastP and C-1. LastP outperformed C-1 slightly, which can be attributed to the fact that larger discrepancies observed between experimental data and model predictions of the last point can increase the weights of likelihood functions. This further implies that several critical points can represent the entire line for point estimation. This paper can provide a reference both for modelers about reasonable utilization of species time-histories, and for experimentalists about the importance of a detailed probability distribution of measurement error, as well as experiment design with emphasis on critical points.

## Research summary

Examines effective independent-data counts and target selection when using shock-tube species time histories for Bayesian kinetic parameter estimation.

Keywords: Bayesian inference, parameter estimation, shock tubes, data correlation

## Resources

- [PDF](https://jiweiqi.github.io/papers/shock-tube-bayes/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/shock-tube-bayes/fulltext.txt)
- [BibTeX](https://jiweiqi.github.io/papers/shock-tube-bayes/citation.bib)

## Sources

- https://doi.org/10.1016/j.proci.2022.08.118
- https://hdl.handle.net/1721.1/156218

## Citation

```bibtex
@article{shocktubebayes2023,
  title = {{Using shock tube species time-histories in Bayesian parameter estimation: Effective independent-data number and target selection}},
  author = {Huaibo Chen and Weiqi Ji and Séan J. Cassady and Alison M. Ferris and Ronald K. Hanson and Sili Deng},
  year = {2023},
  journal = {Proceedings of the Combustion Institute},
  volume = {39},
  pages = {5299-5308},
  doi = {10.1016/j.proci.2022.08.118},
  number = {4},
  url = {https://jiweiqi.github.io/papers/shock-tube-bayes/}
}
```
