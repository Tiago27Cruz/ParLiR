# ParLiR - A Test Collection for Information Retrieval over Portuguese Parliamentary Initiatives

Submitted to ECIR2027

## Data

The data with the initiatives and its metadata (see ``/data/corpus/legislature_xvi.ttl``) comes from the [Portuguese Parliament's open data section](https://www.parlamento.pt/Cidadania/Paginas/DadosAbertos.aspx).

The data is free to use, as long as the [source](https://www.parlamento.pt/Cidadania/Paginas/DadosAbertos.aspx) is mentioned.

## Running the Code

All the source code can be found under ``/scripts``.

Run ``uv sync`` and then run ``uv run .\scripts\<name>.py``.

### Structure

- **qrels.py**: Creates the QRELS files and saves them. Includes the ``train_test_split`` code to divide the QRELS.

- **iaa.py**: Creates stratified Query-Initiative pairs and prompts a local Qwen3-8B LLM to evaluate if the initiative is relevant using a structured prompt with all the initiative metadata and text, along with the query's information need and narrative.

- **evaluation.py**: Calculates the metrics used for evaluation using ``ranx``.

- **cohen.py**: Calculates κ based on the values in ``data/iaa/iaa.csv``, which are created by ``iaa.py``

- **distribution.ipynb**: Creates the lineplot used in the paper.