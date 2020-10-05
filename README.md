# Forrest Gump Project
Retrieved-context models propose that the context at encoding helps guide memory search for later retrieval. These models account for phenomena such as the temporal proximity effect, where events that are encoded close in time are also more likely to be retrieved together later on. However, the association between two temporally adjacent memories can be weakened by an event boundary, which helps segment our continuous life experience into discrete episodes. We are interested in how episodic richness of naturalistic events is affected by temporal distance and the presence of event boundaries. <br/>
<br/>
This project was presented at *Context and Episodic Memory Symposium* and *Lake Ontario Visionary Establishment* in 2020. It is led by Bryan Hong, a PhD student from Memory & Perception Lab at University of Toronto. This repository contains implementations I work on as an undergraduate researcher under Bryan's supervision. It will be merged with the main repo in 2021. 

## Guide
The README is organized in sequential order. I hope this can help streamline the process if you are also using **naturalistic stimuli** for your project.

## Pre-processing Data
### Survival Analysis
Forrest Gump is a modern classic, so many participants came into the lab with previous knowledge of the movie. This is a common issue dealing with naturalistic stimuli. To account for this, you can use **survival analysis** to pre-process the data. You will need to record the time when they expose to the stimulus to perform **left censoring**. If this information is not available (sometimes people don't remember when they first watched Forrest Gump), you will use **left truncation** to remove it from the dataset. A big enough sample size is the key!

### Autobiographical Interview
We categorized the data into four memory types before proceeding to statistical analysis using a modified version of [Autobiographical Interview](https://psycnet.apa.org/record/2002-06812-014). A detailed explanation of our approach can be found [here](https://drive.google.com/file/d/1evNwjzXrLMWbc7vlZwrFxz0LD5B2G09j/view?usp=sharing) on page 3. We have a VBA script that counts the number of highlights if you are processing data in a word doc like us!

### Arc for Visualization
I used arc diagram for this project as it nicely presents all the data points on a horizontal line (which is a good analogy of the timeline of the movie). An arc connects two correlated events, and its weight represents the strength of correlation. Here I use chi-square test to adjust the line weights, but you can replace it with any statistical tool that you want to use.

## Statistical Analysis
### Linear Mixed Model
We are planning to release the script along with the data in 2021. A preview of our results can be found [here](https://drive.google.com/file/d/1evNwjzXrLMWbc7vlZwrFxz0LD5B2G09j/view?usp=sharing). Stay tuned for updates!

### Principal Component Analysis [In Progress]
On [studyforrest website](http://studyforrest.org/data.html), there are eight identified properties of the movie scenes: semantics, emotion, body contact, music, to name a few. I will be using this analysis to explore how much each of these properties contributes to the (re)consolidation of a particular scene. The results of this analysis can be hard to interpret, so you can also try **multiple regression** and **k-means clustering**.

### Semantic Analysis [In Progress]
We are planning to use pre-trained natural language processing models such as [GloVe](https://github.com/stanfordnlp/GloVe) and [word2vec](http://jalammar.github.io/illustrated-word2vec/). The models essentially examine individual words, and thus considered as "context-free." I will be exploring [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html) and its derivation [pQRNN](https://ai.googleblog.com/2020/09/advancing-nlp-with-efficient-projection.html) that capture the context around the words as a mini project for this part.

## Acknowledgement
Big thanks to [Bryan Hong](https://twitter.com/bryan_hong_) for being a supportive mentor! Special award goes to [Tianyu Lu](https://github.com/tianyu-lu) and [Ziyad Edher](https://github.com/ziyadedher) for writing the VBA script, and to Rui Liang, Michael Chen, [Adam Huang](https://github.com/meatMonkAdam), [Zhao Lian](https://github.com/zhaolian-devhaus), and Tianyu (thanks again!) for their support when I am exploring machine learning.
