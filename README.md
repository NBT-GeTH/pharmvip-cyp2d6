# pharmvip-CYP2D6

Prepare CYP2D6 result file to PharmVIP-guideline.

## Setup

### Dependencies
*   Python 3.8+.
*   [pandas 1.2.4](https://pandas.pydata.org/)

## Usage 

The input VCF and BAM files will be run Astrolabe software to get outputAstrolabe. (outputAstrolabe.out.txt)
```shell
python diplotype_astrolabe.py outputAstrolabe.out.txt CYP2D6_with_guideline.txt
```
