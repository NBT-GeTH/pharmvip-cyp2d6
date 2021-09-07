# pharmvip-CYP2D6

Prepare CYP2D6 result file to PharmVIP-guideline.

## Setup

### Dependencies
*   Python 3.8+.
*   [pandas 1.2.4](https://pandas.pydata.org/)

## Usage 

The VCF and BAM files will be used as inputs for running Astrolabe software to get CYP2D6 allele prediction result. (outputAstrolabe.out.txt)
1. Run astrolabe software 
- input : VCF and BAM files
- output: outputAstrolabe.out.txt outputAstrolabe.debug.txt outputAstrolabe.novel.txt
```shell
run-astrolabe.sh \
            -conf \$EBROOTASTROLABE/astrolabe.ini \
            -inputVCF ${vcfGzFile} \
            -inputBam ${bamFile} \
            -outFile ${outputAstrolabe}.out.txt \
            -debugFile ${outputAstrolabe}.debug.txt \
            -novelFile ${outputAstrolabe}.novel.txt \
            -ref ${HumanGenomeVersion} \
            -targets CYP2D6
 ```
2. Extract diplotype from outFile to PharmVIP-guideline module (parameter --diplotype_cyp2d6)
- input : outputAstrolabe.out.txt CYP2D6_with_guideline.txt
- output: diplotype_CYP2D6.tsv
```shell
python diplotype_astrolabe.py outputAstrolabe.out.txt CYP2D6_with_guideline.txt
```
