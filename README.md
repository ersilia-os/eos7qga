# Converter of SMILES in Canonical, Selfie, Inchi, Inchi Key form

This implementation presents 4 ways in which molecules can be represented given a smile using the DATAMOL package. This model receives a SMILE as input, then goes through a process of disinfection and standardization of the molecule, to generate Canonical smiles, selfies, inchi and inchi key (the newest version of inchi).

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
* Interpretation: In this implementation, python version 3.8 is used to be able to work with the Datamol python library. For the preprocessing of a molecule, everything that involves the process of sanitizing and standardizing to obtain the representation forms of a smile. Datamol provides a function called _preprocess, given a smile, it converts to a mole, corrects the errors, sanitizes it and standardizes, returning a molecule ready to be converted into its canonical representation, selfies, inchi and inchi key. The default values used for sanitize de mol were: For the snitize_mol function: the default parameters were: sanifix= True and charge_neutral=False. For standardize_mol, the default parameters were: disconnect_metals=False, normalize=True, reionize=True, uncharge=False, stereo=True

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