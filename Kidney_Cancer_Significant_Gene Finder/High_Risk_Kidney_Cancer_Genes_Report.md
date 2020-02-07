# Analysis of Differentially Expressed Genes Between Low and High Survival Rate Patients with Kidney Cancer  
Author Alex Hakansson

## Abstract: 
In this project, patients were classified as highrisk if they had an overall survival of less than 3 years and low risk if they were still alive. The difference in gene expression between high and low risk patients of the TCGA-KIRC was analyzed in order to determine genes that increase and decrease the lethality of kidney cancer. Having a better understanding of what genes make cancer more aggressive can help us make better treatments for the patients who need it the most. It can also help us determine high risk patients who may need to pursue more aggressive treatment options. The ontologies of the most differentially expressed genes were determined. The ontologies were then compared to find shared motifs between the genes. Although no significant enrichment in the ontologies was found, the differentially expressed genes were cited to be related to cancer. Specifically, a number of the genes were, or were related to, Cancer-Testis genes, genes that are related to cancer but are normally only expressed in male testis. These antigens are believed to be good targets for immunotherapy and brings new possibilities to treat high risk patients expressing these genes.


## Introduction:
Due to the nature of cancer, not everyone's cancer is the same even if they have the same type of cancer. Some cancers are more lethal than others due to these differences. The type and quantity of proteins being produced have a great effect on cancer lethality[11]. One way to measure the proteins being produced is through RNA seq data. By measuring the level of expression of each gene in the form of RNA, we can see which proteins are being made and the changes in expression levels across samples. There are multiple ways to normalize the counts of RNA seq data. The one used in this study is FPKM-UQ. FPKM-UQ normalizes the read count by number of reads, length of the reads, and then by dividing by the number of reads of the gene in the 75th quartile of reads. This is to control for the fact that if one gene is expressed more in one sample than another, the FPKM (normalized by the number of fragments then by read length) will cause the FPKM of the other genes to drop even if their expression level is unchanged [6].
Looking at differences in expression level between high and low risk patients, we can determine which genes make cancer more deadly and which genes make it more benign. By analyzing differentially expressed genes we can better understand which gene promote cancer and find better treatments for cancers expressing these genes [3]. Looking at the ontology of these genes can help us understand what they do in the cancer cell. By looking at which pathways differentially expressed genes more often belong to, researchers can examine these pathways and learn how to treat cancer by targeting these pathways that are important for more lethal cancers [5]. Studying these pathways may also lead to the discovery of new antigens to target with immunotherapy [7].

## Method:

### Getting The Data:
The data used was of TCGA-KIRK project, upper quartile normalized FPKM whole transcriptome data of 537 patients with renal clear cell carcinoma [10]. The data was aquired using the GDC data portal, filtering for TCGA-Kirk transcriptome data with FPKM-UQ in its name. 
After extracting the tar file of the data, FPKM data was compiled into a table using a custom detailed in the notebook. The table was then read as a dataframe using pandas, transposed and transcripts with no expression data were removed. The new table was then written to file.

### Preprocessing:

The table was read into a jupyter notebook. In order to get the clinical data (time lived after diagnosis), the file names in the table were replaced with the clinical ID of each sample. To do this the file names had to be converted into their case_id's using the sample files from GDC and a custom function that can be found in the jupyter notebook. During this conversion, samples that were not from the primary tumor were removed. The clinical data was then added.

### Filtering:

To get more distinct results, patients who were reported to have passed away but who lived for more than 3 years were removed from the data set as it is unclear whether or not these patients were high or low risk. The mean, standard deviation, coefficient of variance (CV) and number of 0's in each gene column were found. Genes with more than 450 zeroes were removed for having too little data. Genes with CVs less than 1 were removed for having low variance. The Z-Scores and P-Values for the remaining genes were found between the remaining patients who survived and those who did not. P-Values were determined using python's scipy package.

### Finding Significant Genes:

Gene significance was taken at .05 significance level with using Holm-Bonferroni correction. Using this method 31 significant genes were found. 

### Analyzing Significant Genes:

The list of 31 significant genes was converted from ensembl ID to official gene name using Biotools.fr [1]. The converted gene names were then uploaded to Metascape and DAVID to see if they had any related ontologies [4,9]. The top 10 most significantly differentiated genes were then searched in UniProt and NCBI for more information about their function and their relation to cancer[2,8].

## Results:

Before filtering the data set contained 58200 transcripts and 537 patient transcript files. After filtering, there were 35887 transcripts and 472 patients. the majority of the cuts made were made by removing genes with CV less than 1. This can be seen in the histogram of the CV of the genes before and after the cuts.

#### Histogram of Frequency vs CV Before Filtering
![Image of Yaktocat](https://github.com/cse185-sp18/cse185-final-project-AlexHakansson/blob/master/Graphs/CV_Before.png)

#### Histogram of Frequency vs CV After Filtering
![Image of Yaktocat](https://github.com/cse185-sp18/cse185-final-project-AlexHakansson/blob/master/Graphs/CV_After.png)

Using the Holm-Bonferroni correction, 31 significant transcripts were found. The following table shows the ensemble id, p value, corrected p value, and gene name for the 30 genes where some gene ID was found. All significantly differentially expressed genes were expressed higher in high risk patients than low risk patients. 

#### Table of Significantly Differentially Expressed Genes

|Ensemble_ID|GENE_ID|P-Value|Corrected P-Value|  
|-|-|-|-|  
|ENSG00000234068|PAGE2|0|0|  
|ENSG00000158639|PAGE5|0|0|  
|ENSG00000166049|PASD1|0|0|  
|ENSG00000176076|KCNE5|0|0|  
|ENSG00000238269|PAGE2B|0|0|  
|ENSG00000268223|ARL14EPL|0|0|  
|ENSG00000046774|MAGEC2|0|0|  
|ENSG00000185247|MAGEA11|5.84E-94|2.10E-89|  
|ENSG00000230257|NFE4|1.32E-93|4.75E-89|  
|ENSG00000227234|SPANXB1|1.08E-91|3.87E-87|  
|ENSG00000162494|LRRC38|6.36E-90|2.29E-85|  
|ENSG00000096006|CRISP3|2.80E-61|1.01E-56|  
|ENSG00000261213|AC099786.3|6.16E-42|2.22E-37|  
|ENSG00000273388|AC005291.2|1.66E-32|5.96E-28|  
|ENSG00000261122|LINC02167|1.17E-28|4.21E-24|  
|ENSG00000167791|CABP2|1.67E-15|6.01E-11|  
|ENSG00000011677|GABRA3|9.93E-15|3.57E-10|  
|ENSG00000266711|AC021534.1|1.13E-13|4.07E-09|  
|ENSG00000242120|MDFIC2|2.41E-11|8.66E-07|  
|ENSG00000237767|LINC01370|4.14E-11|1.49E-06|  
|ENSG00000235180|LINC00601|5.80E-11|2.08E-06|  
|ENSG00000232765|AL158819.1|1.10E-10|3.94E-06|  
|ENSG00000256218|AC007848.2|5.24E-10|1.89E-05|  
|ENSG00000196364|PRSS29P|1.14E-09|4.09E-05|  
|ENSG00000083782|EPYC|1.96E-09|0.00037|  
|ENSG00000205777|GAGE1|1.44E-07|0.005189|  
|ENSG00000232325|AC093627.1|2.95E-07|0.010594|  
|ENSG00000227706|AL713998.1|5.70E-07|0.02049|  
|ENSG00000180066|C10orf91|8.64E-07|0.031071|  
|ENSG00000188624|IGFL3|1.05E-06|0.037776|   


The Genes were then uploaded to DAVID and Metascape, 2 gene ontology enrichment programs. Neither of the tools found any significantly enriched ontologies in the data. In their analysis DAVID and Metascape only identified 17 and 21 unique genes out of the set of 30 from the list given to them. Metascape returned nothing as nothing was significant, while DAVID returned a list ontologies that were not significantly enriched. The results of the DAVID can be found in David_Results.txt in the supplementary folder.

The top 10 enriched genes were then researched using UniProt and NCBI to determine their function and relation to cancer.

#### Table of Gene Function in Relation to Cancer
|Gene|Function|
|-|-|
|PAGE2|Related to demethylation of CpG of Cancer-Testis (CT) Genes leading to their expression. CT are thought to be good targets for immunotherapy|
|PAGE5|Cancer-Testis antigen. Thought to protect the cell from programmed cell death and is a possible target for immunotherapy|
|PASD1|Believed to function as a transcription factor and as cancer antigen that could be a potential target for immunotherapy|
|KCNE5|Is part of a voltage gated ion channel. Can regulate many processes from ion selectivity, voltage sensitivity, and plasma membrane anterograde recycling|
|PAGE2B|A paralog of PAGE2. Also related to demethylation of CpG of Cancer-Testis|
|ARL14EPL|ADP ribosylation factor|
|MAGEC2|Promotes ubiquitination of P53 and degradation. Is another Cancer-Testis gene|
|MAGEA11|Androgen Receptor that may play a role in tumor progression|
|NFE4|Transcription factor that up regulates gamma gene expression|
|SPANXB1|Transcription factor that upregulates CT genes.|

5 out of the top 10 genes are related to Cancer-Testis (CT) genes. This indicates that these genes play an important role in survival in patients with kidney cancer. Amongst the top 5 genes are also antigens that are believed to be good targets for immunotherapy, genes that degrade tumor supressors, and other genes pertinent to cancer survival.

## Discussion:

Looking at the differentially expressed genes, although they did not appear to be significantly related when looking at the gene ontology through DAVID and metascape, many of the genes were or were related to CT genes. These antigens are thought to be good targets for immunotherapy and so these results show a promising new treatment for high risk patients with renal carcinoma. Among the other top genes differentially expressed in high risk patients are other antigens believed to be good targets of immunotherapy (PASD1) and a gene the degrades p53, a tumor suppressor gene (MAGEC2). These genes could also be good candidates for immunotherapy or for new drug targets. Further research should be done to into testing the effect of immunotherapy on CT genes in renal cancer cells as a possible treatment. Further analysis should be done to differentiate patients on whether or not they are expressing these CT genes as this is a good indicator that they are at a higher risk and would also respond better to CT targeted immunotherapy.


## Citation

[1] Andy, Saurin. BioTools.  Web. 11 June 2018.

[2] Benson, Dennis A. et al. “GenBank.” Nucleic Acids Research 33.Database Issue (2005): D34–D38. PMC. Web. 11 June 2018.

[3] High-Throughput Tissue Microarray Analysis to Evaluate Genes Uncovered by cDNA Microarray Screening in Renal Cell Carcinoma
Moch, Holger et al. The American Journal of Pathology , Volume 154 , Issue 4 , 981 - 986

[4] Huang DW, Sherman BT, Lempicki RA. Systematic and integrative analysis of large gene lists using DAVID Bioinformatics Resources. Nature Protoc. 2009;4(1):44-57.  [PubMed]

[5] Joseph R. Nevins. "Oncogenic pathway signatures in human cancers as a guide to targeted therapies". Nature volume 439, pages 353–357 (19 January 2006) doi:10.1038/nature04296

[6] Li, Xiaohong et al. “A Comparison of per Sample Global Scaling and per Gene Normalization Methods for Differential Expression Analysis of RNA-Seq Data.” Ed. Zhi Wei. PLoS ONE 12.5 (2017): e0176185. PMC. Web. 11 June 2018.

[7] Orentas RJ, Yang JJ, Wen X, Wei JS, Mackall CL and Khan J (2012) Identification of cell surface proteins as potential immunotherapy targets in 12 pediatric cancers. Front. Oncol. 2:194. doi: 10.3389/fonc.2012.00194

[8] The UniProt Consortium. UniProt: the universal protein knowledgebase. Nucleic Acids Res. 45: D158-D169 (2017)

[9] Tripathi, Shashank et al. “Meta- and Orthogonal Integration of Influenza ‘OMICs’ Data Defines a Role for UBR4 in Virus Budding.” Cell host & microbe 18.6 (2015): 723–735. PMC. Web. 11 June 2018.

[10] Weinstein, John N. et al. “The Cancer Genome Atlas Pan-Cancer Analysis Project.” Nature genetics 45.10 (2013): 1113–1120. PMC. Web. 11 June 2018.

[11] Zhao, Hongjuan et al. “Gene Expression Profiling Predicts Survival in Conventional Renal Cell Carcinoma.” Ed. Francesco Marincola. PLoS Medicine 3.1 (2006): e13. PMC. Web. 11 June 2018.
