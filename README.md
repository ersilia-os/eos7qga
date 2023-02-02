# Converter of SMILES in Canonical, Selfie, Inchi, Inchi Key form

Using the Datamol package, the model receives a SMILE as input, then goes through a process of sanitizing and standardization of the molecule to generate four outputs: Canonical SMILES, SELFIES, InChI and InChIKey

## Identifiers

* EOS model ID: `eos7qga`
* Slug: `datamol-smiles2canonical`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `Matrix`
* Interpretation: Compound represented in its canonical SMILES, SELFIES, InChI and InChIKey forms

## References

* [Publication](https://doc.datamol.io/stable/tutorials/Preprocessing.html)
* [Source Code](https://github.com/datamol-org/datamol)
* Ersilia contributor: [carcablop](https://github.com/carcablop)

## Citation

If you use this model, please cite the [original authors](https://doc.datamol.io/stable/tutorials/Preprocessing.html) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a Apache-2.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!