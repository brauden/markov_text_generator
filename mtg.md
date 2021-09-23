## Markov Text Generator
#### Provide some example applications of your function in both deterministic and stochastic modes, for a few sets of seed words and a few different n.

```python
finish_sentence(['there', 'are', 'several'], 2, corpus, True)
out: ['there', 'are', 'several', 'minutes', ',', 'and', 'the', 'same', 'time', ',', 'and', 'the', 'same', 'time', ',']
```

```python
finish_sentence(['she', 'was', 'not'], 3, corpus, False)
out: ['she', 'was', 'not', 'uncheerful', '.']
```

```python
finish_sentence(['it', 'is', 'very', 'generous'], 4, corpus, False)
out: ['it', 'is', 'very', 'generous', 'spirit', '!']
```

```python
finish_sentence(['it', 'sdafs', 'nice'], 3, corpus, False)
out: ['it', 'sdafs', 'nice', 'comfortable', 'size', 'for', 'constant', 'use', ',', 'and', 'to', 'assist', 'him', '.']
```