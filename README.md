# Converter of SMILES in Canonical, Selfie, Inchi Key form

Using the Datamol package, the model receives a SMILE as input, then goes through a process of sanitizing and standardization of the molecule to generate four outputs: Canonical SMILES, SELFIES, InChI and InChIKey

This model was incorporated on 2023-01-25.

## Information
### Identifiers
- **Ersilia Identifier:** `eos7qga`
- **Slug:** `datamol-smiles2canonical`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Chemical notation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `3`
- **Output Consistency:** `Fixed`
- **Interpretation:** Compound represented in its canonical SMILES, SELFIES, and InChIKey forms

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| standard_smiles | string |  | SMILES in standard format |
| selfie | string |  | SELFIES representation of the SMILES |
| inchikey | string |  | InChIKey representation of the SMILES |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos7qga](https://hub.docker.com/r/ersiliaos/eos7qga)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7qga.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7qga.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `727`
- **Image Size (Mb):** `672.77`

**Computational Performance (seconds):**
- 10 inputs: `33.15`
- 100 inputs: `22.76`
- 10000 inputs: `23.16`

### References
- **Source Code**: [https://github.com/datamol-org/datamol](https://github.com/datamol-org/datamol)
- **Publication**: [https://doc.datamol.io/stable/tutorials/Preprocessing.html](https://doc.datamol.io/stable/tutorials/Preprocessing.html)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [carcablop](https://github.com/carcablop)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos7qga
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos7qga
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
