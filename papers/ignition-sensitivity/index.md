# Evolution of sensitivity directions during autoignition

Weiqi Ji, Zhuyin Ren, Chung K. Law

Proceedings of the Combustion Institute, 2019. Journal article.

DOI: https://doi.org/10.1016/j.proci.2018.07.005

Canonical page: https://jiweiqi.github.io/papers/ignition-sensitivity/

## Abstract

Sensitivity analysis of the ignition delay time and species profiles to kinetic parameters has been widely used to identify the rate-limiting steps during the autoignition process, providing insights for the optimization of the reaction mechanism. This work studies the time evolution of the sensitivity directions of the temperature and species concentration during autoignition. The direction is represented by a unit vector along the gradient of the simulation output to the kinetic parameters, and the alignment between the two directions are measured by the inner product between the corresponding unit vectors. We use evolution of the sensitivity directions to reveal changes in the rate-limiting steps and the correlation among species at different phases of the ignition delay period. It is found that the sensitivity directions of temperature and the concentrations of the major intermediate species are similar to each other during the entire ignition delay period. In particular, they converge to the same direction when approaching the ignition state, and the direction is the same as the one for the ignition delay time. The correlation is validated for various fuels across a wide range of pressures and temperatures, and works for both single-stage ignition and two-stage ignition. Consequently the sensitivity of the ignition delay time can be efficiently evaluated based on the temperature sensitivity at the ignition point, for which a single run of the simulation can produce the sensitivity to all parameters, as otherwise the sensitivity of the ignition delay time has to be evaluated through finite difference, in which the number of runs equals to the number of parameters. It can also significantly reduce the computation cost of gradient-based algorithms for the purpose of mechanism optimization and uncertainty quantification.

## Research summary

Relates the sensitivity directions of temperature, species and ignition delay, enabling efficient evaluation of ignition-delay sensitivities.

Keywords: sensitivity analysis, ignition delay, chemical kinetics

## Resources

- [PDF](https://jiweiqi.github.io/papers/ignition-sensitivity/paper.pdf)
- [Extracted full text](https://jiweiqi.github.io/papers/ignition-sensitivity/fulltext.txt)
- [GitHub](https://github.com/jiweiqi/IgnSens)
- [BibTeX](https://jiweiqi.github.io/papers/ignition-sensitivity/citation.bib)

## Sources

- https://doi.org/10.1016/j.proci.2018.07.005
- https://collaborate.princeton.edu/en/publications/evolution-of-sensitivity-directions-during-autoignition/

## Citation

```bibtex
@article{ignitionsensitivity2019,
  title = {{Evolution of sensitivity directions during autoignition}},
  author = {Weiqi Ji and Zhuyin Ren and Chung K. Law},
  year = {2019},
  journal = {Proceedings of the Combustion Institute},
  volume = {37},
  pages = {807-815},
  doi = {10.1016/j.proci.2018.07.005},
  number = {1},
  url = {https://jiweiqi.github.io/papers/ignition-sensitivity/}
}
```
