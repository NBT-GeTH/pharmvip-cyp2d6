# pharmvip-CYP2D6

Prepare input CYP2D6 file to PharmVIP-guideline.

## Setup

### Dependencies
*   Python 3.8+.
*   [pandas 1.2.4](https://pandas.pydata.org/)

## Usage 

VCF and BAM file will be run Astrolabe software to get outputAstrolabe. (file.out.txt)
```shell
diplotype_astrolabe.py ${outputAstrolabe} ${CYP2D6_with_guideline.txt}
```
