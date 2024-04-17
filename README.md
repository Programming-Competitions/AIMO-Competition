# Transformers doing math 2: Math Olympiad

[competition](https://www.kaggle.com/competitions/ai-mathematical-olympiad-prize/overview)
Deadline: June 20th

baseline notebook: https://www.kaggle.com/vatsadev/aimo-zero-shot-sc-mmos-deepseekmath-augment-prompt

**LORA Finetune MMOS Deepseek RL on all the formatted instrutions(4-5k or less most likely, measure soon)** 

*16bit https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k ft*

*would do a full finetune, but im poor, no h100 sxm :(*
 - look into any inference/cot before doing so
 - build rajs checker thing now

## Goals
 - solve Olympiad level problems (AMC-12/AIME) with AI
 - Latex Math format understanding
 - good mathematical reasoning skill

## Data

 - get all the past AMC/AIME/Putnam/other math data
links:
 - ~~https://artofproblemsolving.com/wiki/index.php/IMO_Problems_and_Solutions~~
 - ~~http://markan.net/aime/syllabus.pdf IMPORTANT, Start with data categories/KG here~~
 - https://kskedlaya.org/putnam-archive/
 - https://drive.google.com/file/d/0B8JbOaFM5Xo_bnc2NUd0dDFLY1U/view?pref=2&pli=AIME&resourcekey=0-1tVMnKTLCkFlKuyljA_VyA
 - https://cdn.artofproblemsolving.com/attachments/9/3/9ed002bb3307e38c2e626fc7354d1fc28f231a.pdf
 - ~~https://davidaltizio.web.illinois.edu/CollectionOfAIMESolutions.pdf~~
 - https://cjquines.com/files/obscuregeothms.pdf
 - ~~https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions~~
 - ~~https://artofproblemsolving.com/wiki/index.php/AMC_12_Problems_and_Solutions~~
 - ~~https://artofproblemsolving.com/wiki/index.php/AMC_8_Problems_and_Solutions~~
 - ~~https://artofproblemsolving.com/wiki/index.php/AMC_10_Problems_and_Solutions~~
 - ~~https://artofproblemsolving.com/wiki/index.php/AHSME_Problems_and_Solutions~~
 - ~~https://huggingface.co/datasets/hendrycks/competition_math~~
 - ~~https://artofproblemsolving.com/wiki/index.php/USAJMO_Problems_and_Solutions~~
 - ~~https://artofproblemsolving.com/wiki/index.php/USAMO_Problems_and_Solutions~~
 - https://github.com/OpenBMB/OlympiadBench?scrlybrkr=4c9c022b
 - https://math.stackexchange.com/
 - https://www.math.northwestern.edu/undergraduate/prizes-competitions-organizations/putnam/putnam-selection-tests.html
 - https://www.math.northwestern.edu/documents/undergraduate/math-clubs-competitions-prizes/putnam/easy_putnam_problems.pdf
 - https://www.math.northwestern.edu/documents/undergraduate/math-clubs-competitions-prizes/putnam/training_problems.pdf
 - https://www2.math.upenn.edu/~wilf/gfologyLinked2.pdf
 - https://vjimc.osu.cz/problems
 - https://www.imc-math.org.uk/?year=1994&item=problems
 - https://huggingface.co/datasets/math-ai/TemplateGSM
 - https://huggingface.co/datasets/math-ai/StackMathQA
 - https://huggingface.co/datasets/nvidia/OpenMathInstruct-1

## Models/Frameworks

Baseline: Gemma 7b can get 3/50 problems

look into math selfplay, Q* geohot version

## Notes
Tools can probably figure out the math behind the problem, the problem needs to be interped first, Have a DB, ngram/vec-search it for the most similar Questions, see what methods they use to solve the problem, Give the LLM conceptual reasoning understanding, to workout the problem.
Try to find some form of CoT/ToT/MonteCarlo on problem search
Try to expand AlphaGeom logic solver to other domains
when the model calls on tools, have it call out an operation, and a place to store the variable. that way the model can quickly map out the problem in natural language all the way to answer, while the cpu does all the computation and supplies the final integer answer

```
Example:
use calc solve <<<{tool:integral(a),store:intl_a}>>>
add 10 <<<{tool:calcu(intl_a+10),store:ans}>>>
the answer is {ans}
```
*The model outputs this, cpu gives final answer*

## knowledge from papers

MathGLM - 2309.03241
 - Build synthetic data around Pemdas Operations (),x^y,x*y,x/y,x+y,x-y, inf possibilities, finishes arithmetic mostly
 - 500m-2b models can do intro high school math, 7b might be enough for olympiad level, start by testing scale from 500m to 2b though
 - more data = better, olympiads will probably need millions of questions, and billions of questions to build its baseline skills and reasoning
 - going step by step may hurt numerical acc, use tools here
 - can show errors between more than/less than, but most often a question misunderstanding error, needs work

Self consistency - 2203.11171
 - Sample through several CoT paths, then aggregate the most common answer to be the final answer

MiniCPM - 2404.06395
 - Model wind tunnel
   - using model scaling width/depth
   - optimal batchsize: bs = 1.21×10^9 / L^6.24, L(loss), bs(batch_size)
   - LR doesnt change with scal, 0.5b to 7b same lr
   - WSD LR schedule helps push smaller models to much larger level models loss
  
Olympiad Bench - 2402.14008
 - *Important, only other olympiad baseline?*
 - deepseek-7b-rl appears to be the base model to be using, only non-gpt-4 model somewhat successful at olympiads
 - Biggest mistakes by models:
    - lengthy reasoning proofs
    - Mistakes in simplifying and transforming algebraic equations
    - incorrect conclusions, too simple
    - Misunderstanding the questions
    - calculation errors
    - often introducing unnesc. vars/concepts

## building/work

Baseline Stage (S1):
 - Test the Gemma 7b baseline, see how that works, then a oh-2.5-pro-mistral/reg. mistral baseline
 - Looking into using the old Nanophi model/logic datasets from it to see if small LMs can do anything
 - Start building a universal format/scraping all the data to it
 - testing claude opus for a sympy format

**Lil ft boost**
 - *curriculum learning dataset format with the math questions sorted by difficulty*
 - try schedule-free optimizer by meta
 - All the tricks from MiniCPM uP, wind tunnel, etc, and olympiad bench
 - DPO for Math? Correct/Incorrect solutions?
 - FT like orca-math did, bascially just SFT once, then KTO, then KTO again, if no KTO then double DPO, (make synthetic pairs for DPO)

*Inference time boosts*
 - If the model can code verify with the same answer, give the answer a higher weightage in the sum
 - Uncertain gets no extra weight, False gets less weightage
 - prompt diversity helps, using `you are alan turing/einstien`, the famous `you just had two cold beers` or `you are a math professor`
 - find the aime equivalent versions of reasoning strats like `“using visualizations, working backwards, using direct calculation, method of elimination`
 - start with 10 examples for deepseek-math-rl, but examples have the diverse prompt additions, use a famous math personality depending on the question, ex. `you are {person}, an expert in {topic}, solve this:` otherwise just use `terence tao`

**hmm possible path forward**

 - self consistency search helps with answer consistency, but fails when the LLM fails to get the question misinterped?
 - Compiling a question to specific logical symbols and specific words we know the meaning to, means that we can format/rephrase any way we want
 - So compile a question into words and problem statements using the LLM (**This is the key part, the rest of it wont work if the LLM misinterprets questions, for more info, look into neurallambda issue #2**) (*also the right time to look into winds dspy compiler thing*)
 - Rephrase the question a couple times from that broken down version
 - Self consistent search trees on everything, the LLM using the sympy/nl(natural language) words approach to get the answers
 - return and format one answer
 - *Possible extra step:* We breakdown theorems/concepts/steps for all the questions we encounter, and put them into one vector db, and whenever doing a problem, fuzzy/ngram the question bank, pull out the most similar question
 - *Anything else from here is just whatever other papers have found on this, or if we pull more eureka*


*Deepseek math 7b instruct can do 15/50 with just self consistency and a model with math training, no tools, no special features, nothing, just gs8mk/math level train/eval* **all this extra stuff should push it several reasoning strides further**
