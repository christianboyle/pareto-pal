# pareto-pal

> The [Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle) states that for many outcomes, roughly 80% of consequences come from 20% of causes (the "vital few"). Other names for this principle are the 80/20 rule, the law of the vital few, or the principle of factor sparsity.

#

ParetoPal's output is the product of [GPT-4](https://platform.openai.com/docs/models/gpt-4) + [LangChain](https://python.langchain.com/docs/get_started/introduction.html) + [WikipediaAPIWrapper](https://github.com/hwchase17/langchain/blob/master/langchain/utilities/wikipedia.py#L14) + [this prompt](https://twitter.com/BrianRoemmele/status/1641649098599067648):

> Please forget all prior prompts.  You are a university professor at a top university. You have become an expert in the Pareto principle (80/20 rule). Please identify the 20% of ___________ that will yield 80% of the best  results. Use your academic resources to  provide a well identified and focused learning program to master this subject. Please continue this prompt until I say stop.

# web

https://pareto-pal.streamlit.app/

# local

```
pyenv shell 3.8.16
git clone git@github.com:christianboyle/pareto-pal.git
pip install streamlit langchain openai wikipedia chromadb tiktoken
streamlit run app.py
```

# examples

![meditation](https://github.com/christianboyle/pareto-pal/assets/1605754/30066b85-db07-4cf8-997f-14ed05bb9b84)

![how-to-run-an-ebay-store](https://github.com/christianboyle/pareto-pal/assets/1605754/06b55754-459f-4aea-8574-6dbd15269137)

![how-to-lift-weights](https://github.com/christianboyle/pareto-pal/assets/1605754/df9a3fc5-3592-410d-9b7a-19c1cd24cc9f)

![raising-children](https://github.com/christianboyle/pareto-pal/assets/1605754/83099da7-6b80-4ee1-9677-6a6880fa19d5)

![potty-training](https://github.com/christianboyle/pareto-pal/assets/1605754/c04d2b59-4fd9-42de-bbe2-70735e35b9e1)

